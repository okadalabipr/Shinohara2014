import numpy as np

from .name2idx import C, V

def signal(t, x):

    if t <= x[C.tdelay]:
        return x[C.sbase]
    elif x[C.tdelay] < t and t <= x[C.traise]+x[C.tdelay]:
        return (x[C.sinput]-x[C.sbase])*(t-x[C.tdelay])/x[C.traise] + x[C.sbase]
    elif x[C.traise]+x[C.tdelay] < t and t<= x[C.tpulse]+x[C.traise]+x[C.tdelay]:
        return x[C.sinput]
    else:
        return (x[C.sinput]-x[C.slate])*np.exp(-(t-x[C.tpulse]-x[C.traise]-x[C.tdelay])/x[C.tdecay]) + x[C.slate]


def diffeq(y, t, *x):

    dydt = [0] * V.NUM

    TAK1 = 1.0 - y[V.TAK1a]
    IKK1 = 1.0 - y[V.IKK2] - y[V.IKK3] - y[V.IKK4]

    dydt[V.TAK1a] = x[C.k5z]*TAK1 - x[C.k6t]*y[V.TAK1a]/(x[C.k6m]+y[V.TAK1a]) + x[C.k5ta]*signal(t,x)*TAK1/(x[C.k5ma]+TAK1) \
        + x[C.k5tb2]*y[V.IKK2]*TAK1/(x[C.k5mb2]+TAK1) + x[C.k5tb3]*y[V.IKK3]*TAK1/(x[C.k5mb3]+TAK1)

    dydt[V.IKK2] = x[C.k1ta]*y[V.TAK1a]*IKK1/(x[C.k1ma]+IKK1) - x[C.k1tb]*y[V.IKK2]/(x[C.k1mb]+y[V.IKK2]) - x[C.k2ta]*y[V.IKK2]/(x[C.k2ma]+y[V.IKK2]) \
        - x[C.k2tb]*y[V.IKK2]*y[V.IKK3]/(x[C.k2mb]+y[V.IKK2]) + x[C.k2tc]*y[V.IKK3]/(x[C.k2mc]+y[V.IKK3])

    dydt[V.IKK3] = x[C.k2ta]*y[V.IKK2]/(x[C.k2ma]+y[V.IKK2]) + x[C.k2tb]*y[V.IKK2]*y[V.IKK3]/(x[C.k2mb]+y[V.IKK2]) \
        - x[C.k2tc]*y[V.IKK3]/(x[C.k2mc]+y[V.IKK3]) - x[C.k3t]*y[V.IKK3]/(x[C.k3m]+y[V.IKK3])

    dydt[V.IKK4] = x[C.k3t]*y[V.IKK3]/(x[C.k3m]+y[V.IKK3]) - x[C.k4t]*y[V.IKK4]/(x[C.k4m]+y[V.IKK4])

    return dydt


def param_values():

    x = [0] * C.NUM

    x[C.k5z] = 4.15e+02
    x[C.k5ta] = 1.75e+03
    x[C.k5ma] = 5.52e-02
    x[C.k5tb2] = 9.36e+02
    x[C.k5mb2] = 1.02e-03
    x[C.k5tb3] = 2.76e+03
    x[C.k5mb3] = 1.02e-03
    x[C.k6t] = 4.31e+03
    x[C.k6m] = 1.43
    x[C.k1ta] = 9.61e-01
    x[C.k1ma] = 9.86e-01
    x[C.k1tb] = 2.59e-01
    x[C.k1mb] = 2.02e-01
    x[C.k2ta] = 1.12e-06
    x[C.k2ma] = 3.56
    x[C.k2tb] = 3.49e+01
    x[C.k2mb] = 1.56
    x[C.k2tc] = 6.41
    x[C.k2mc] = 1.76
    x[C.k3t] = 3.01e-01
    x[C.k3m] = 4.50e-01
    x[C.k4t] = 1.14e-01
    x[C.k4m] = 2.60

    #signal
    x[C.sinput] = 1.0
    x[C.sbase] = 0.1
    x[C.tpulse] = 0.075
    x[C.traise] = 1.0
    x[C.tdecay] = 1.5
    x[C.tdelay] = 0.0  # 2.0
    x[C.slate] = 0.27

    return x


def initial_values():

    y0 = [0] * V.NUM

    return y0