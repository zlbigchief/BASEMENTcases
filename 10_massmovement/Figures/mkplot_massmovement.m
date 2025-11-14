%% Initialization
clear; clc; close all;

%% Paths
% assume current folder is 10_massmovement/Figures
addpath('./private_mfiles');

%% Load data
% Load model results from CSV files
modelData = cell(4, 1);
for i = 1:4
    modelData{i} = readtable(fullfile('../ParaView', sprintf('p%d.csv', i)));
end

% Load experimental results from MAT file
load(fullfile('../Ref', 'experiment.mat'));

%% Parameters (for nondimensionalization)
b = 122;        % half-width of movable bed [m]
h = 10;         % still water depth [m]
g = 9.81;       % gravitational acceleration [m/s^2]
x_probe_nd = [0, 20, 180, 400]; % non-dim probe locations
x_probe = x_probe_nd * h + b;   % probe locations [m]

%% Prepare figure
fig = figure;
SetFigureSize(fig, 8, 12)

subplotRows = 4;
subplotCols = 1;
tld = tiledlayout(subplotRows, subplotCols, 'TileSpacing', 'tight', 'Padding', 'tight');

% Preallocate space for nondimensionalized data
nondimModelData = cell(4, 1);

%% Process data and create subplots (one tile per probe)
for i = 1:4
    % Nondimensionalize model data
    xModel = modelData{i}.Time * sqrt(g/h) - (x_probe(i) - b) / h ; 
    yModel = (modelData{i}.avg_water_surface_ - h) / h ; 
    nondimModelData{i} = [xModel, yModel];
    
    % Nondimensionalize experimental data
    xExp = ExpData.(['P' num2str(i)])(:, 1); 
    yExp = ExpData.(['P' num2str(i)])(:, 2); 
    
    % Create subplot
    nexttile
    hold on; box on;
    plot(nondimModelData{i}(:, 1), nondimModelData{i}(:, 2), '-k', 'LineWidth', 1.5, 'DisplayName', 'Model');
    scatter(xExp, yExp, 'ok','DisplayName', 'Experiment', 'SizeData', 20);
    
    % Set labels using LaTeX
    ylabel('$\eta / h$', 'Interpreter', 'latex');
    title(sprintf('Probe P%d Comparison, $(x - b) / h$ = %d', i, x_probe_nd(i)), 'Interpreter', 'latex');
    if i == 4
        legend('show', 'Location','best');
        xlabel('$t\sqrt{g/h} - (x -b ) /h$', 'Interpreter', 'latex');
    end
    grid on;
    hold off;

    % set axis limits for better visualization
    xlim([-20 140])
    ylim([-8 2] / 100)
end

%% Labels, annotations and finalize layout
fontsize(tld, 8, 'points');
addTileLabels(tld, 8)
sgtitle('Model-Experiment Comparison for Probes P1 to P4');

%% Save figure
disp('Saving figure as PNG...');
exportgraphics(fig, 'model_experiment_comparison.png', 'Resolution', 300);
disp('Figure saved.');