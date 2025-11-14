# type: ignore
# pylint: disable=invalid-name

import meshtool
from meshtool import Node, Segment
from meshtool import RegionMarker
from meshtool.factories import RectangularMeshFactory

class TwoRegionBasinFactory(RectangularMeshFactory):
    def __init__(self, width: float, height: float,
                 midpoint_offset: tuple = (0.0, 0.0),
                 control_nodes: list = [(0, 0), (0, 0),(0, 0),(0, 0)]) -> None:
        super().__init__(width=width, height=height, midpoint_offset=midpoint_offset)  # Instantiate AbstractFactory

        # Create a rectangular basin using the parent class
        factory = RectangularMeshFactory(
            width=width, height=height, midpoint_offset=midpoint_offset)

        # Add nodes from the rectangular factory
        self.nodes = factory.nodes
        self.segments = factory.segments

        # Add control nodes separating the two regions
        # Create Node objects for each control node and store in a list
        control_node_objs = [Node(pt) for pt in control_nodes]

        # Add the control nodes to the mesh node list
        self.nodes.extend(control_node_objs)

        # Add segments between the control nodes 1 and 2 also 3 and 4
        self.segments.append(Segment(control_node_objs[0], control_node_objs[1]))
        self.segments.append(Segment(control_node_objs[2], control_node_objs[3]))

    def elevation_at(self, point):
        # Constant bed elevation

        x, y = point
        return 0.0


# Instantiate the factory
[b, flume_width, flume_length] = [122, 50, 10000]
my_factory   = TwoRegionBasinFactory(width=flume_length, height=flume_width, midpoint_offset=(0, 0), 
                                    control_nodes=[
                                        ( b, -flume_width/2),
                                        ( b,  flume_width/2),
                                        (-b, -flume_width/2),
                                        (-b,  flume_width/2)
                                    ])

# Set the matID
# Add region markers
my_factory.regions = [
    RegionMarker( (b+flume_length/2)/2, 0, max_area=15, attribute=0),
    RegionMarker(-(b+flume_length/2)/2, 0, max_area=15, attribute=0),
    RegionMarker(                   0, 0, max_area=15, attribute=1)
]

# Generate the mesh
mesh, _ = my_factory.build()

elevations = meshtool.calculate_element_elevation(mesh, my_factory)

# Export the mesh
mesh.save('massmovement.2dm')
