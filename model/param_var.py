PARAM_VAR = [\
    'TAK1a',
    'IKK2',
    'IKK3',
    'IKK4'\
]

for i,name in enumerate(PARAM_VAR):
  exec('%s=%d'%(name,i))