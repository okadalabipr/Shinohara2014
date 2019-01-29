constant = [\
    'k5z',
    'k5ta',
    'k5ma',
    'k5tb2',
    'k5mb2',
    'k5tb3',
    'k5mb3',
    'k6t',
    'k6m',
    'k1ta',
    'k1ma',
    'k1tb',
    'k1mb',
    'k2ta',
    'k2ma',
    'k2tb',
    'k2mb',
    'k2tc',
    'k2mc',
    'k3t',
    'k3m',
    'k4t',
    'k4m',
    #signal
    'sinput',
    'sbase',
    'tpulse',
    'traise',
    'tdecay',
    'tdelay',
    'slate'\
]

for i,name in enumerate(constant):
  exec('%s=%d'%(name,i))

def setParamConst():
    x = [0]*len(constant)

    x[k5z] = 4.15e+02
    x[k5ta] = 1.75e+03
    x[k5ma] = 5.52e-02
    x[k5tb2] = 9.36e+02
    x[k5mb2] = 1.02e-03
    x[k5tb3] = 2.76e+03
    x[k5mb3] = 1.02e-03
    x[k6t] = 4.31e+03
    x[k6m] = 1.43
    x[k1ta] = 9.61e-01
    x[k1ma] = 9.86e-01
    x[k1tb] = 2.59e-01
    x[k1mb] = 2.02e-01
    x[k2ta] = 1.12e-06
    x[k2ma] = 3.56
    x[k2tb] = 3.49e+01
    x[k2mb] = 1.56
    x[k2tc] = 6.41
    x[k2mc] = 1.76
    x[k3t] = 3.01e-01
    x[k3m] = 4.50e-01
    x[k4t] = 1.14e-01
    x[k4m] = 2.60

    #signal
    x[sinput] = 1.0
    x[sbase] = 0.1
    x[tpulse] = 0.075
    x[traise] = 1.0
    x[tdecay] = 1.5
    x[tdelay] = 0.0#2.0
    x[slate] = 0.27

    return x
