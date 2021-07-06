from geomdl import BSpline

# Create the curve instance
crv = BSpline.Curve()

# Set degree
crv.degree = 2

# Set control points
crv.ctrlpts = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]

# Set knot vector
crv.knotvector = [0, 0, 0, 1, 1, 1]

# Set evaluation delta
crv.delta = 0.005

# Get evaluated points
points_a = crv.evalpts

# Update delta
crv.delta = 0.1

# The curve will be automatically re-evaluated
points_b = crv.evalpts

