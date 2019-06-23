#PyPoll

import os
import csv

csv_path = os.csv.join("..","PyPoll","election_data.csv")
 

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#taking out the header row
    csv_header = next(csvfile)

    votes = []
    candidates = []

    for row in csvfile:
        votes.append(row[0])
        candidates.append(row[2])

    #counting all the votes
    total_votes = len(votes) 

    #getting the names of all unique candidates
    transfer_to_unique = set(candidates)
    unique_candidates = list(transfer_to_unique) 

    #counting how many votes each candidate received
    unique_candidates_tally = dict([x, candidates.count] for x in transfer_to_unique)

    #finding percentage of votes each candidate received
    unique_candidates_percentage = dict([x, (candidates.count/total_votes)*100] for x in transfer_to_unique)

    #finding winner of election
    winner = max(zip(unique_candidates_tally.keys, unique_candidates_tally.values))

    #taking values of dictionaries and puting them into lists
    tally = [v for v in unique_candidates_tally.values]
    percentage = [v for v in unique_candidates_percentage.values]

    # to be used in dictionary
    tally_percentage = zip(tally, percentage)
    
    #dictionary where each candidate has their total and percentage as values
    candidates_tally_percentage_dict = dict(zip(unique_candidates,tally_percentage))

    #printing the results
    print("Election Results")
    print("------------------------")
    print("Total Votes: " total_votes)
    print(candidates_tally_percentage_dict)
    print("Winner" winner)

     with open (PyPollFinal.csv, 'w') as csvfile
  csvwriter = csv.writer(csvfile, delimiter = '', quotchar = '"', 
    quoting = csv.QUOTE_NONNUMERIC)

  csvwriter.writerow(["Election Results"])
  csvwriter.writerow(["------------------------------"])
  csvwriter.writerow([""])
  csvwriter.writerow([""])
  csvwriter.writerow([""])
  csvwriter.writerow([""])
  csvwriter.writerow([""])















