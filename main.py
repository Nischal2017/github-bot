import os
import generater as gen
from matplotlib import pyplot as plt

dates = {}
commits = {}

plt.style.use('seaborn')

for days in range(1,366):
	
	date = f'{days} days ago'
	pltdata = gen.makeCommits(days)
	if(pltdata[0][0:7] in dates.keys()):
		dates[pltdata[0][0:7]] += pltdata[1]
	else:
		dates[pltdata[0][0:7]] = 0


plt.bar(dates.keys(),dates.values())
plt.plot_date(dates.keys(),dates.values(), linestyle='solid')
plt.show()