function addTileLabels(tiledLayout, fontsize, varargin)
 % Validate input
 if ~isa(tiledLayout, 'matlab.graphics.layout.TiledChartLayout')
     error('Input must be a tiledlayout object.');
 end
 
 % Set default text position
 textX = 0.05;
 textY = 0.95;
 
 % Parse optional input arguments for text position
 if nargin > 2
     textX = varargin{1};
 end
 if nargin > 3
     textY = varargin{2};
 end
 
 % Get the children of the tiledlayout (axes)
 tiles = findobj(tiledLayout.Children, 'Type','axes');
 
 % Generate labels (a), (b), (c), ...
 numTiles = numel(tiles);
 labels = arrayfun(@(x) sprintf('(%c)', 'a' + x - 1), 1:numTiles, 'UniformOutput', false);
 
 % Loop through each tile and add the label
 for i = 1:numTiles
     currentTile = tiles(numTiles - i + 1); % Tiles are in reverse order
     if isa(currentTile, 'matlab.graphics.axis.Axes')
         % Add the label to the specified position of the axes
         text(currentTile, ...
             textX, textY, labels{i}, ... % Position (normalized coordinates)
             'Units', 'normalized', ...
             'HorizontalAlignment', 'left', ...
             'VerticalAlignment', 'top', ...
             'FontSize', fontsize)
     end
 end
end