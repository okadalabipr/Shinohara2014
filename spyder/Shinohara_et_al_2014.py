#%%
%run -i ../model/setParamConst.py
%run -i ../model/setVarEnum.py
%run -i ../model/diffeq.py
%run -i ../model/initialValues.py
%run -i ../runSim.py
%run -i ../plot.py
plt.savefig('./TAK1IKKmodel.png',bbox_inches='tight')