import os
import generater as gen
import random
from matplotlib import pyplot as plt
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Date(YYYY-MM-DD HH:MM:SS)", "No of Commits"]

dates = {}
commits = {}

plt.style.use('seaborn')

no_of_commits = int(input("Enter the number of commits to be made : "))

pltdata = gen.makeCommits(0)
os.system("git add .")
os.system('git commit -m "First Commit"')
table.add_row(pltdata)

for times in range(1, no_of_commits):
	
	days = random.randint(1, 368)
	date = f'{days} days ago'
	pltdata = gen.makeCommits(days)
	table.add_row(pltdata)
	if(pltdata[0][0:7] in dates.keys()):
		dates[pltdata[0][0:7]] += pltdata[1]
	else:
		dates[pltdata[0][0:7]] = pltdata[1]

	os.system("git add .")
	os.system('git commit --date="'+date+'" -m "Commit"')

os.system("git push")
print(table)

plt.bar(dates.keys(),dates.values())
plt.plot_date(dates.keys(),dates.values(), linestyle='solid')
plt.xlabel("Months [YYYY-MM]")
plt.ylabel("No of Commits")
plt.title("Distribution of Commits")
plt.show()