# Enter csv budget data file
import csv
# Path to the csv file
csv_file_path = "./Resources/budget_data.csv"
output_file = "output.txt"

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["" , 99999999999]
total_net = 0

# open csv file
with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    first_row = next(csvreader)
    total_months+=1
    total_net = int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net

        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change +=[row[0]]


        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0]
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0]
net_average = sum(net_change_list) / len(net_change_list)
print(f"{greatest_increase}\n{greatest_decrease}\n{round(net_average,2)}\n")

# create output
output = f"""Financial Analysis
---------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(net_average, 2)}
Greatest Increase in Profits: {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease}"""

print(output)

with(open("output_Dennis.txt", 'w') as f):
    f.write(output)