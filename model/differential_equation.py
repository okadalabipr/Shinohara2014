def signal(t,x):
    if t <= x[tdelay]:
        return x[sbase]
    elif x[tdelay] < t and t <= x[traise]+x[tdelay]:
        return (x[sinput]-x[sbase])*(t-x[tdelay])/x[traise] + x[sbase]
    elif x[traise]+x[tdelay] < t and t<= x[tpulse]+x[traise]+x[tdelay]:
        return x[sinput]
    else:
        return (x[sinput]-x[slate])*np.exp(-(t-x[tpulse]-x[traise]-x[tdelay])/x[tdecay]) + x[slate]

def diffeq(y,t,*args):
    dydt = [0]*len(PARAM_VAR)

    TAK1 = 1.0 - y[TAK1a]
    IKK1 = 1.0 - y[IKK2] - y[IKK3] - y[IKK4]

    dydt[TAK1a] = x[k5z]*TAK1 - x[k6t]*y[TAK1a]/(x[k6m]+y[TAK1a]) + x[k5ta]*signal(t,x)*TAK1/(x[k5ma]+TAK1) +\
                x[k5tb2]*y[IKK2]*TAK1/(x[k5mb2]+TAK1) + x[k5tb3]*y[IKK3]*TAK1/(x[k5mb3]+TAK1)

    dydt[IKK2] = x[k1ta]*y[TAK1a]*IKK1/(x[k1ma]+IKK1) - x[k1tb]*y[IKK2]/(x[k1mb]+y[IKK2]) - x[k2ta]*y[IKK2]/(x[k2ma]+y[IKK2]) -\
                x[k2tb]*y[IKK2]*y[IKK3]/(x[k2mb]+y[IKK2]) + x[k2tc]*y[IKK3]/(x[k2mc]+y[IKK3])

    dydt[IKK3] = x[k2ta]*y[IKK2]/(x[k2ma]+y[IKK2]) + x[k2tb]*y[IKK2]*y[IKK3]/(x[k2mb]+y[IKK2]) - x[k2tc]*y[IKK3]/(x[k2mc]+y[IKK3]) -\
                x[k3t]*y[IKK3]/(x[k3m]+y[IKK3])

    dydt[IKK4] = x[k3t]*y[IKK3]/(x[k3m]+y[IKK3]) - x[k4t]*y[IKK4]/(x[k4m]+y[IKK4])

    return dydt