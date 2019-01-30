#%%
%run -i ../model/setParamConst.py
%run -i ../model/setVarEnum.py
%run -i ../model/diffeq.py
%run -i ../model/initialValues.py
%run -i ../runSim.py
%run -i ../plot.py
plt.savefig('../Shinohara_et_al_2014.png',bbox_inches='tight')