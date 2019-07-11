from matplotlib import pyplot as plt

from model.name2idx import f_variable as V
def timecourse(sim):
    plt.figure(figsize=(16,12))
    plt.rcParams['font.size'] = 18
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 2

    plt.subplots_adjust(wspace=0.4, hspace=0.5)

    #IKK activity (Fig.2E)
    plt.subplot(2,2,1)
    plt.plot(sim.ta[200:],102*sim.Ya[0,200:,V.IKK2]+305*sim.Ya[0,200:,V.IKK3],color='navy',label='IKK2+IKK3')
    plt.plot(sim.ta[200:],102*sim.Ya[0,200:,V.IKK2],color='tomato',label='IKK2')
    plt.plot(sim.ta[200:],305*sim.Ya[0,200:,V.IKK3],color='brown',label='IKK3')
    plt.xlim(-0.5,9.5)
    plt.xticks([0,1.5,3,4.5,6,7.5,9])
    plt.ylim(0,120)
    plt.xlabel('Time (min)')
    plt.ylabel('IKK activity\n(relative % max.)')
    plt.yticks([0,20,40,60,80,100])
    plt.legend(loc='upper left',frameon=False)

    #BAY (Fig.3D right)
    plt.subplot(2,2,2)
    plt.plot(sim.ta[200:],115*sim.Ya[0,200:,V.TAK1a],color='navy',label='WT')
    plt.plot(sim.tb[200:],115*sim.Yb[200:,V.TAK1a],color='brown',label='BAY')
    plt.xlim(-0.5,9.5)
    plt.xticks([0,3,6,9])
    plt.ylim(0,120)
    plt.xlabel('Time (min)')
    plt.ylabel('TAK1 activity\n(relative % max.)')
    plt.yticks([0,50,100])
    plt.legend(ncol=2,loc='upper left',frameon=False)

    #Feedback(-) (Fig.3F right)
    plt.subplot(2,2,3)
    plt.plot(sim.ta[200:],115*sim.Ya[0,200:,V.TAK1a],color='navy',label='Intact')
    plt.plot(sim.ta[200:],115*sim.Ya[1,200:,V.TAK1a],color='lime',label='Feedback(-)')
    plt.xlim(-0.5,9.5)
    plt.xticks([0,3,6,9])
    plt.ylim(0,120)
    plt.xlabel('Time (min)')
    plt.ylabel('TAK1 activity\n(relative % max.)')
    plt.yticks([0,50,100])
    plt.legend(ncol=2,loc='upper right',frameon=False)

    #Feedback(-)+P668(↓) (Fig.3G right)
    plt.subplot(2,2,4)
    plt.plot(sim.ta[200:],115*sim.Ya[0,200:,V.TAK1a],color='navy',label='Intact')
    plt.plot(sim.ta[200:],115*sim.Ya[2,200:,V.TAK1a],color='orchid',label='Feedback(-)+\nP668(↓)')
    plt.xlim(-0.5,9.5)
    plt.xticks([0,3,6,9])
    plt.ylim(0,120)
    plt.xlabel('Time (min)')
    plt.ylabel('TAK1 activity\n(relative % max.)')
    plt.yticks([0,50,100])
    plt.legend(ncol=2,loc='upper right',frameon=False)

    plt.show()