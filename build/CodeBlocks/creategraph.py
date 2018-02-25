import matplotlib.pyplot as plt
import sys
import csv

x=[]
y=[]
yerror=[]
input_file = sys.argv[1]
f=open(input_file)
with f as csvfile:
    reader = csv.DictReader(csvfile)
    i=1
    for row in reader:
    	x.append(i)
    	i=i+1
    	y.append(float(row['Mean Return']))
    	yerror.append(float(row['Standard Deviation']))

f.close()

plt.xlabel("Episode number")
plt.ylabel("Mean Return")
plt.title("Graph for Incremental Natural Actor Critic on Acrobot")
plt.errorbar(x,y,yerr=yerror,color='r',ecolor='b')
plt.show()
