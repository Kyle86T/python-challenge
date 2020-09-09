import os
import csv
#Locating the file
financial_data = os.path.join("..", "Resources", "budget_data")
#declaring the variables and list
total_months=0
total_net=0
max_change=0
net_change_max=0
net_change_min=0
min_change=0
sum_profits_losses=0
previous_profits_losses=0
current_change_per=0
difference=0
difference_list = []
#opening and reading the file:
with open(financial_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skipping the first header row
    csvheader=next(csvfile)
    firstrow=next(csvreader)
    previous_profits_losses = int(firstrow[1])

    for row in csvreader:
        #count the rows to get total months
        total_months = total_months + 1
        #start from 0, and sum the integer in the 1 index column to get sum of profits/losses
        sum_profits_losses = sum_profits_losses + int(row[1])
        #The following is to take the change per line, and average it out over the length of months
        current_change_per = int(row[1])
        #getting the differnce from the previous profit/loss
        difference = current_change_per - previous_profits_losses
        #appending the list to add the value
        difference_list.append(difference)
        #took this code from Gunjan, as I'm not quite sure how it works
        previous_profits_losses=current_change_per
        if current_change_per > net_change_max:
            net_change_max=current_change_per
            max_month = row[0]
        if current_change_per < net_change_min:
            net_change_min=current_change_per
            min_month=row[0]

#Code breaks herea and don't know why...

listaverage=(sum(difference_list)/total_months)
​#printing the results
print("Financial Review")
print(f"Total Months:{total_months}")
print(f"Total:{sum_profits_losses}")
print(f"Average Change:{listaverage}")
print(f"Greatest Increase in Profits:{net_change_max}")
print(f"Greatest Decrease in Profits:{net_change_min}")

output_file = os.path.join('..', 'analysis', 'financial_data.txt')
#writing the text file
with open(output_file, 'w') as txtfile:
        txtfile.writelines('Financial Analysis')
        txtfile.writelines('\n----------------------------------- \n')
        txtfile.writelines('Total Months: ' + str(total_months)')
        txtfile.writelines('Net Total P/L: ' + str(total_months)')     
        txtfile.writelines('Avg Change of P/L: ' + str(total_months)')
        txtfile.writelines('Greatest Increase: ' + str(total_months)') 
        txtfile.writelines('Greatest Decrease: ' + str(total_months)')     

#printing the file
with open(output_file, 'r') as readfile:
    print(readfile.read())              