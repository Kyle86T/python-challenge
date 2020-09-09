import os
import csv
​
#Locating the file
Bankresults = os.path.join("Resources","budget_data.csv")
​#declaring the variables/lists
tot_mos = 0
tot_net = 0
net_chg_max = 0
net_chg_min = 0
sumpl = 0
prev_pl = 0
curr_chg_per = 0
diff = 0
difflist = []
​
​#opening the file to read
with open(Bankresults, newline = "") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #below is to skip the header row​   
    csvheader=next(csvfile)
    
    firstrow=next(csvreader)
    prev_pl=int(firstrow[1])
​
    for row in csvreader:
        tot_mos = tot_mos + 1
        sumpl = sumpl + int(row[1])
        curr_chg_per = int(row[1])
        diff = curr_chg_per - prev_pl
        difflist.append(diff)
        prev_pl=curr_chg_per
        if curr_chg_per > net_chg_max:
            net_chg_max=curr_chg_per
            max_month = row[0]
        if curr_chg_per < net_chg_min:
            net_chg_min=curr_chg_per
            min_month=row[0]
​
listaverage=(sum(difflist)/tot_mos)
​
print("Financial Review")
print(f"Total Months:{tot_mos}")
print(f"Total:{sumpl}")
print(f"Average Change:{listaverage}")
print(f"Greatest Increase in Profits:{net_chg_max}")
print(f"Greatest Decrease in Profits:{net_chg_min}")
​
new_file = open("bankresults.txt","w")
​
new_file.write("Fin Anal\n")
new_file.write("---------------------------------------------- \n")
new_file.write(f"Total Months:{tot_mos}\n")
new_file.write(f"Total:{sumpl}")
new_file.write(f"Average Change:{listaverage}")
new_file.write(f"Greatest Increase in Profits:{net_chg_max}")
new_file.write(f"Greatest Decrease in Profits:{net_chg_min}")