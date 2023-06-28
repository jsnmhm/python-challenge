import os
import csv

#initialize variable to hold results
total_votes = 0
results = {}

input = os.path.join("Resources", "election_data.csv")
#create context manager to handle file
with open(input) as file:
    reader = csv.reader(file)

    #skip header row
    header = next(reader)

    #loop through file
    for row in reader:
        #increment total vote counter
        total_votes += 1
        name = row[2]
        #if name is in results, increment value
        #else, add name key to results with value of 1
        if name in results:
            results[name] += 1
        else:
            results[name] = 1
#get key that has the maximum value
winner = max(results, key = results.get)

#output to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for name in results:
    print(f"{name}: {results[name]/total_votes:.3%} ({results[name]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

out_file_path = os.path.join("analysis", "results.txt")

#output to file
with open(out_file_path, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for name in results:
        file.write(f"{name}: {results[name]/total_votes:.3%} ({results[name]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
