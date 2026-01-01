import numpy as np
from matplotlib import pyplot as plt

import sys
sys.path.append("..")

#from animation_interpolation_expressions import ease_out_quad  # absolute import
from animation_interpolation_expressions import _ease_out_quad

x = np.linspace(0, 1, 20)

y = [_ease_out_quad(t) for t in x]


fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
