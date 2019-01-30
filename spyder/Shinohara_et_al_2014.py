#%%
%run -i ../model/setParamConst.py
%run -i ../model/setVarEnum.py
%run -i ../model/diffeq.py
%run -i ../model/initialValues.py
%run -i ../runSim.py
%matplotlib inline
%run -i ../plot.py
plt.savefig('../Shinohara_al_2014.png',bbox_inches='tight')