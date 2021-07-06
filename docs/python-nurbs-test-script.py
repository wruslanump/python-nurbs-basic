# Importing NURBS module
from geomdl.core import NURBS

# Importing visualization module
from geomdl.visualization import VisMPL as vis

# Creating a curve instance
crv = NURBS.Curve()

# Make a quadratic curve
crv.degree = 2

#######################################################
# Skipping control points and knot vector assignments #
#######################################################

# Set the visualization component and render the curve
crv.vis = vis.VisCurve3D()
crv.render()

