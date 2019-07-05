F_V = [\
    'TAK1a',
    'IKK2',
    'IKK3',
    'IKK4',
    #
    'len_f_vars'\
]

for i,name in enumerate(F_V):
  exec('%s=%d'%(name,i))