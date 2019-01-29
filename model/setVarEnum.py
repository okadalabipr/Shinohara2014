variable = [\
    'TAK1a',
    'IKK2',
    'IKK3',
    'IKK4'\
]

for i,name in enumerate(variable):
  exec('%s=%d'%(name,i))