# type: ignore
# pylint: disable=invalid-name

import meshtool
from meshtool import Node, Segment
from meshtool import RegionMarker
from meshtool.factories import RectangularMeshFactory

class TwoRegionBasinFactory(RectangularMeshFactory):
    def __init__(self, width: float, height: float,
                 midpoint_offset: tuple = (0.0, 0.0),
                 control_nodes: list = [(-50, 0), (50, 0)]) -> None:
        super().__init__(width=width, height=height, midpoint_offset=midpoint_offset)  # Instantiate AbstractFactory

        # Create a rectangular basin using the parent class
        factory = RectangularMeshFactory(
            width=width, height=height, midpoint_offset=midpoint_offset)

        # Add nodes from the rectangular factory
        self.nodes = factory.nodes
        self.segments = factory.segments

        # Add control nodes separating the two regions
        control_node1 = Node(control_nodes[0])
        control_node2 = Node(control_nodes[1])
        self.nodes.extend([control_node1, control_node2])

        # Add a segment between the control nodes
        control_segment = Segment(control_node1, control_node2)
        self.segments.append(control_segment)

    def elevation_at(self, point):
        # Constant bed elevation

        x, y = point
        return 0.0


# Instantiate the factory
my_factory   = TwoRegionBasinFactory(width=15.0, height=1.0, midpoint_offset=(7.5, 0.5), control_nodes=[(5.0, 0), (5.0, 1.0)])

# Set the matID
# Add region markers
my_factory.regions = [
    RegionMarker( 1.0, 0.5, max_area=0.1, attribute=0),
    RegionMarker(6.0, 0.5, max_area=0.1, attribute=1)
]

# Generate the mesh
mesh, _ = my_factory.build()

elevations = meshtool.calculate_element_elevation(mesh, my_factory)

# Export the mesh
mesh.save('two_region_basin.2dm')
