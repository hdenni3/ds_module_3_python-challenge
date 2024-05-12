# Enter csv election data file
import csv
# Path to the csv file
csv_file_path = "./Resources/election_data.csv"
output_file = "output.txt"

total_votes = 0
candidates_dict = {}

# Open csv file with UTF-8 encoding
with open(csv_file_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read the csv header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row after the header
    for row in csvreader:
        # print(row)

        # count votes total
        total_votes += 1

        # add to dict
        row_candidate = row[2]
        if row_candidate in candidates_dict.keys():
            candidates_dict[row_candidate] += 1
        else:
            candidates_dict[row_candidate] = 1

print(total_votes)
print(candidates_dict)

# create output
output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n"""

max_candidate = ""
max_votes = 0

for candidate in candidates_dict.keys():
    # get the votes
    votes = candidates_dict[candidate]
    percent = 100 * (votes / total_votes)

    line = f"{candidate}: {round(percent, 3)}% ({votes})\n"
    output += line

    if votes > max_votes:
        max_candidate = candidate
        max_votes = votes

last_line = f"""---------------------------
Winner: {max_candidate}
--------------------------"""

output += last_line

print(output)

with(open("output_Dennis.py", 'w') as f):
    f.write(output)


