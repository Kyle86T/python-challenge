#Gunjan deserves all the credit for helping me. I was having trouble with the script so she sent me over her script.
#I went thru it piece by piece understanding what she did, and why she did it. I updated things that I found could be
#I made comments on why she put everything in here, and if I didn't understand them. I noticed that her txt file saves
#in the folder Pybank, so I updated mine to save to the analysis folder. Gunjan helped me out a ton.

import os
import csv
#locating the file 
xfile = os.path.join("..", "Resources", "election_data.csv")
#declaring variable lists
election_results = {}
number_of_votes = []
total_votes=0
candidates=[]
vote_percent=[]
winner_list =[]
#opening and reading in file
with open(xfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #Testing #print(f"Help: {header}")
    #Since rows are equal to 1 vote, just add the rows
    for row in csvreader:
        total_votes = total_votes + 1
        #if row 2 candidate is the same as row 2+1, add one to the candidates votes    
        if row[2] in election_results.keys():
            election_results[row[2]] = election_results[row[2]] + 1
        else:
            election_results[row[2]] = 1
#appending the election results with each/new candidates and new counts as it loops           
for key, value in election_results.items():
    candidates.append(key)
    number_of_votes.append(value)
#Taking the number of votes and turning it into a percent of the total #, then appending to the list
for n in number_of_votes:
    vote_percent.append(round(n/total_votes*100,1))
    #store the values in a list to recall later
    election_results_data = list(zip(candidates,number_of_votes, vote_percent))
#Taking the above list, if the max votes = the name of #1 on above list, append the winner list with their name
for name in election_results_data:
    if max(number_of_votes) == name[1]:
        winner_list.append(name[0])
#Grabbing the winner of the election
winner = winner_list[0]
#adding the remaining candidates to the list in the order that they end up in, ie 1st,2nd,3rd, etc.
if len(winner_list) > 1:
    for w in range(1,len,(winner_list[w])):
        winner = winner + "," + winner_list[w]

#creating the output location for the txt file
output_file = os.path.join('..', 'analysis', 'election_results.txt')
#writing the text file
with open(output_file, 'w') as txtfile:
    txtfile.writelines('election Results \n----------------------------------- \nTot Votes: ' + str(total_votes) +'\n--------------------------------\n')
    for entry in election_results_data:
        txtfile.writelines(entry[0] + ":" + str(entry[2]) + '% (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------ \nWinner: ' + winner + '\n-----------------------')

#printing the file
with open(output_file, 'r') as readfile:
    print(readfile.read())

