import os
import generater as gen
import random
import time
from matplotlib import pyplot as plt
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Date(YYYY-MM-DD HH:MM:SS)", "No of Commits"]

dates = {}
commits = {}

plt.style.use('seaborn')

no_of_commits = int(input("Enter the number of commits you want to make : "))

pltdata = gen.makeCommits(0)
os.system("git add .")
os.system('git commit -m "First Commit"')
dates[pltdata[0][0:7]] = 1


print("Making atleast 1 commit for each day of the year.\nYou have 5 seconds to abort before operation starts.\nPress Ctrl+C to abort.")
time.sleep(5)

for days in range(1, 368):
	
	date = f'{days} days ago'
	pltdata = gen.makeCommits(days)

	if(pltdata[0][0:7] in dates.keys()):
		dates[pltdata[0][0:7]] += 1
	else:
		dates[pltdata[0][0:7]] = 1

	os.system("git add .")
	os.system('git commit --date="'+date+'" -m "Commit"')

print("Randomizing the number of commits on different days.\nDo not abort now!!")
time.sleep(3)

for days in range(1, no_of_commits-367):
	
	days = random.randint(1,368)
	date = f'{days} days ago'
	pltdata = gen.makeCommits(days)
	
	dates[pltdata[0][0:7]] += 1
	
	os.system("git add .")
	os.system('git commit --date="'+date+'" -m "Commit"')

for item in dates.items():
	table.add_row(item)

os.system("git push")
print(table)
print("Total commits made :" + str(sum(dates.values())))

print("Choose the which graph needs to be generated")
print("Enter 1 for Bar Chart")
print("Enter 2 for Line Chart")
print("Enter 3 for a Bar/Line Chart")
graph = int(input("Make your choice : "))

if graph < 2 or graph > 2:
	plt.bar(dates.keys(),dates.values())
if graph > 1 or graph > 2:
	plt.plot_date(dates.keys(),dates.values(), linestyle='solid')

plt.xlabel("Months [YYYY-MM]")
plt.ylabel("No of Commits")
plt.title("Distribution of Commits")
plt.show()