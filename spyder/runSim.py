#%%
%run -i ../model/setParamConst.py
%run -i ../model/setVarEnum.py
%run -i ../model/diffeq.py
%run -i ../model/initialValues.py
%run -i ../simulation.py
%run -i ../plotFunc.py
plt.savefig('./TAK1IKKmodel.png',bbox_inches='tight')