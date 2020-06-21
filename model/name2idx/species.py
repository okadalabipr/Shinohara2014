NAMES = [
    'TAK1a',
    'IKK2',
    'IKK3',
    'IKK4',
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)