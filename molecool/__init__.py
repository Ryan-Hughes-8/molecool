"""A python package to visualize molecules given their Cartesian coordinates.
This was created for the Python Best Practices Workshop"""

# Add imports here
from molecool.functions import canvas
from molecool.measure import calculate_angle, calculate_distance
from molecool.atom_data import atomic_weights, atom_colors
from molecool.molecules import build_bond_list, bond_histogram, compute_molecular_mass
from molecool.visualization import draw_molecule

# different ways to import and/or organize the same functions ========

# from molecool.io import open_pdb, open_xyz, write_xyz

# from molecool.io.pdb import open_pdb
# from molecool.io.xyz import open_xyz, write_xyz

from molecool import io
# ====================================================================

from ._version import __version__
