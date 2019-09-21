var_names = [\
    'TAK1a',
    'IKK2',
    'IKK3',
    'IKK4',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
  exec('%s=%d'%(name,idx))