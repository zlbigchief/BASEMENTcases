"""This script creates a small, trapezoidal channel mesh.

Do do this, it first uses the BASEchange channel generator factories to
create the 1D channel representation of the geometry, and then exports
it as a 2DM mesh for easy viewing in QGIS or similar tools.
"""

from basechange import factories


factory = factories.TrapezoidalChannelWidening(
    # Basic channel geometry
    dist_cs=10,
    num_cs=20,
    bed_width=20,
    height=10,
    bed_slope=0.05,
    bank_slope=0.5,

    # Frictions
    friction_bed=40,
    friction_bank=30,

    # Widening geometry
    widening_bed_width=30,
    widening_friction=20,
    widening_dist_cs=10,
    widening_num_cs=4,
    transition_dist_cs=5,
    transition_num_cs=3,

    # Offset to keep elevations positive
    raise_by=10)

# Generate the channel geometry
channel = factory.build_channel()

# Build a mesh using the channel geometry
mesh = channel.to_mesh(max_area=5.0)

# Export the mesh as 2DM
mesh.save('trapezoidal_channel_mesh.2dm')
