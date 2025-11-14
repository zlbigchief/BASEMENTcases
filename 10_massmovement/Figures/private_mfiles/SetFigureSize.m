function fig = SetFigureSize(fig, width_cm, height_cm)
    % SetFigureSize sets the size of a figure in centimeters and centers it on the screen.
    % 
    % Inputs:
    %   - fig: Handle to the figure (must be a valid figure handle).
    %   - width_cm: Desired width of the figure in centimeters.
    %   - height_cm: Desired height of the figure in centimeters.
    %
    % Outputs:
    %   - fig: Handle to the resized figure.

    % Validate the figure handle
    if ~ishandle(fig) || ~strcmp(get(fig, 'Type'), 'figure')
        error('Input must be a valid figure handle.');
    end

    % Default width and height if not provided
    if nargin < 2, width_cm = 15; end
    if nargin < 3, height_cm = 10; end

    % Set figure units to centimeters
    set(fig, 'Units', 'centimeters');

    % Get screen size and convert to centimeters
    screenSize = get(0, 'ScreenSize');
    screenPPI = get(0, 'ScreenPixelsPerInch');
    if isempty(screenPPI) || screenPPI <= 0
        warning('Screen PPI not detected accurately; assuming 96 DPI.');
        screenPPI = 96; % Default PPI
    end
    screenSize = screenSize / screenPPI * 2.54;

    % Calculate position to center the figure
    pos_left = (screenSize(3) - width_cm) / 2;
    pos_bottom = (screenSize(4) - height_cm) / 2;

    % Set figure position
    set(fig, 'Position', [pos_left, pos_bottom, width_cm, height_cm]);
end
