from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

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