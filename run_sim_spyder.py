#%%
%run -i model/param_const.py
%run -i model/param_var.py
%run -i model/differential_equation.py
%run -i model/initial_condition.py
%run -i simulation.py
%run -i plot_func.py
plt.savefig('./TAK1IKKmodel.png',bbox_inches='tight')