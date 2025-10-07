# type: ignore
# pylint: disable=invalid-name

import meshtool
from meshtool import Node, Segment


class FlatChannelFactory(meshtool.AbstractFactory):
    def __init__(self, width_upstream, width_downstream, channel_length, slope):
        super().__init__()  # Instantiate AbstractFactory

        self.width_upstream = width_upstream
        self.width_downstream = width_downstream
        self.channel_length = channel_length
        self.slope = slope

        # Add nodes
        top_left = Node((0, width_upstream / 2))
        top_right = Node((channel_length, width_downstream / 2))
        bottom_left = Node((0, -width_upstream / 2))
        bottom_right = Node((channel_length, -width_downstream / 2))
        self.nodes = [top_left, top_right, bottom_left, bottom_right]

        # Add segments
        top = Segment(top_left, top_right)
        left = Segment(top_left, bottom_left)
        right = Segment(top_right, bottom_right)
        bottom = Segment(bottom_left, bottom_right)
        self.segments = [top, left, right, bottom]

    def elevation_at(self, point):
        # Sloping in x direction, flat in y direction 
        x, y= point
        return -self.slope * x


my_factory = FlatChannelFactory(width_upstream=20.0, width_downstream=40.0, channel_length=50.0, slope=0.01)
mesh, _ = my_factory.build(max_area=1, min_angle=30)
elevations = meshtool.calculate_element_elevation(mesh, my_factory)

# Export the mesh
mesh.save('widening_open_channel.2dm')
