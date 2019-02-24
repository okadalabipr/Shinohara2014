import numpy as np
from scipy.integrate import odeint

ta = np.linspace(-2,10,1201)
Ya = np.empty((3,len(ta),len(PARAM_VAR)))
y0 = set_initial_condition()

for i in range(3):
    x = set_param_const()
    if i == 0:  # WT
        pass
    elif i == 1:  # feedback(-)
        x[k5tb2] = 0.
        x[k5tb3] = 0.
    elif i == 2:  # feedback(-) & P668(↓)
        x[k5ta] = 8.76e+02
        x[k5tb2] = 0.
        x[k5tb3] = 0.
        x[k2tb] = 0.

    Ya[i,:,:] = odeint(diffeq,y0,ta,args=tuple(x))


# The IKKβ inhibitor BAY11-7085 (BAY) was added 2 min after stimulation
t1 = np.linspace(-2,2,401)
t2 = np.linspace(2,10,801)
tb = np.append(t1,t2)

y0 = set_initial_condition()
x = set_param_const()

Y1 = odeint(diffeq,y0,t1,args=tuple(x))
x[k1ta] = 0.
x[k2ta] = 0.
x[k2tb] = 0.
Y2 = odeint(diffeq,Y1[-1,:],t2,args=tuple(x))
Yb = np.vstack((Y1,Y2))
