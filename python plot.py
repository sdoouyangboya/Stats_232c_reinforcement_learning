
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pylab as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
from matplotlib.ticker import LogLocator, LogFormatterSciNotation as LogFormatter
import matplotlib.colors as mcolors
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import matplotlib.font_manager as font_manager

fig=plt.figure(figsize=(8,7))
ax=plt.axes()
    #画出两条中位数曲线
train_sizes=[]
for i in range (1,31):
    train_sizes.append(i)

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="g",label='Standard deviation')
plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    #画出两条中位数曲线
plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training set")
plt.plot(train_sizes, test_scores_mean, 'o-', color="black",
             label="Test set")

 
    #绘制图例，参数loc表示图例放置的位置，best表示自适应
ax.minorticks_on()
ax.tick_params('both',top=True,right=True, length=18, width=2, which='major',labelsize=25)
ax.tick_params('both', top=True,right=True,length=9,width=2,  which='minor')
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.spines['bottom'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
plt.rc('legend',fontsize=25) 
plt.ylim(4,5.5)
plt.xlim(0,35)
font = font_manager.FontProperties(family='Helvetica',size=25)
ax.legend(labelspacing=0.2,prop=font,frameon=False,loc='upper right')
plt.xlabel("Number of neurons",fontsize=25,family='Helvetica')
plt.ylabel("RMSE (MPa)",fontsize=25,family='Helvetica')
plt.text(4, 4.8, 'Optimal number of neurons \n                    = 9',fontsize=25,family='Helvetica')
plt.plot([9,9],[4.4,4.88],'--',color='black',)
plt.tight_layout()
fig.savefig('a.pdf')