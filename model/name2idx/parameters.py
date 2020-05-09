param_names = [
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
    'slate',
]

for idx, name in enumerate(param_names):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

len_f_params = len(param_names)
