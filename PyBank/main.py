import os
import csv

#initialize variables
total_months = 0
total = 0
greatest_increase = [0,0]
greatest_decrease = [0,0]
mom_change = 0
curr_pnl = 0
prev_pnl = 0
total_change = 0

#set file path
file_path = os.path.join("Resources", "budget_data.csv")

#open file
with open(file_path) as csvfile:
    reader = csv.reader(csvfile)

    #skip header
    header = next(reader)

    for row in reader:
        #get profit/loss for current month
        #increment counter for total number of months
        #add current profit/loss to running total
        curr_pnl = int(row[1])
        total_months += 1
        total += int(row[1])

        #if previous month profit/loss is 0,
        #that means we are on the first month
        #and can't calculate month-over-month change, so it's 0
        #else, month-over-month is current profit/loss - previous month profit/loss
        if prev_pnl == 0:
            mom_change = 0
        else:
            mom_change = curr_pnl - prev_pnl

        #determine if current values exceed previously determined min/max values
        if mom_change > int(greatest_increase[1]):
             greatest_increase = [row[0], mom_change]
        if mom_change < int(greatest_decrease[1]):
             greatest_decrease = [row[0], mom_change]

        #add current month-over-month change to running total
        total_change += mom_change
        #finished processing current month, so store data in prev month
        #variable before moving on to next row
        prev_pnl = int(row[1])

#print data to terminal
print("Financial Analysis")
print("""
--------------------------------------
""")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${total_change/(total_months - 1):.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

out_file_path = os.path.join("analysis", "output.txt")

#print data to file
with open(out_file_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("""
    --------------------------------------
    \n""")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${total_change/(total_months - 1):.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    





