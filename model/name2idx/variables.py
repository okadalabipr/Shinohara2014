var_names = [
    'TAK1a',
    'IKK2',
    'IKK3',
    'IKK4',
]

for idx, name in enumerate(var_names):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

len_f_vars = len(var_names)