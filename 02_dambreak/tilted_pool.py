# type: ignore
# pylint: disable=invalid-name

from meshtool import RegionMarker
from meshtool.factories import RectangularMeshFactory

# Instantiate the factory. The helper used also defines the mesh domain
factory = RectangularMeshFactory(
    width=100.0, height=10.0, midpoint_offset=(50, 5))

# Define the elevation function to use


@factory.set_elevation_func
def slope(point):
    x, y = point
    slope = 0.1
    return -slope * x


# Set the matID
# Add region markers
factory.regions = [
    RegionMarker(1.0, 1.0, max_area=2.0, attribute=1)
]


# Generate the mesh
mesh, _ = factory.build()

# Export the mesh
mesh.save('tilted_pool.2dm')