import numpy as np
from scipy.integrate import odeint

from model.set_model import *


class Simulation(object):
    ta = np.linspace(-2, 10, 1201)
    Ya = np.empty((3, len(ta), V.len_f_vars))
    y0 = initial_values()

    for i in range(3):
        x = f_params()
        if i == 0:  # WT
            pass
        elif i == 1:  # feedback(-)
            x[C.k5tb2] = 0.
            x[C.k5tb3] = 0.
        elif i == 2:  # feedback(-) & P668(↓)
            x[C.k5ta] = 8.76e+02
            x[C.k5tb2] = 0.
            x[C.k5tb3] = 0.
            x[C.k2tb] = 0.

        Ya[i, :, :] = odeint(diffeq, y0, ta, args=tuple(x))


    # The IKKβ inhibitor BAY11-7085 (BAY) was added 2 min after stimulation
    t1 = np.linspace(-2, 2, 401)
    t2 = np.linspace(2, 10, 801)
    tb = np.linspace(-2, 10, 1201)

    y0 = initial_values()
    x = f_params()

    Y1 = odeint(diffeq, y0, t1, args=tuple(x))
    x[C.k1ta] = 0.
    x[C.k2ta] = 0.
    x[C.k2tb] = 0.
    Y2 = odeint(diffeq, Y1[-1, :], t2, args=tuple(x))
    
    Yb = np.vstack((np.delete(Y1, -1, axis=0), Y2))
