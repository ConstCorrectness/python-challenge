import csv
import os


filename = os.path.join('Resources', 'budget_data.csv')

profits = []
months = []

with open(filename) as f:
  reader = csv.reader(f)
  
  header_line, *rest = reader
  for line in rest:
    months.append(line[0])
    profits.append(int(line[1]))


total_profits = sum(profits)
total_months = len(months)
average_changes = [profits[i + 1] - profits[i] for i in range(len(months) - 1)]
average_change = sum(average_changes) / len(average_changes)

greatest_increase = max(average_changes)
greatest_decrease = min(average_changes)

greatest_month_increase = greatest_month_decrease = ""

for idx, change in enumerate(average_changes):
  if change == greatest_increase:
    greatest_month_increase = idx
  if change == greatest_decrease:
    greatest_month_decrease = idx

greatest_month = months[greatest_month_increase + 1]
least_month = months[greatest_month_decrease + 1]


print('Financial Analysis')
print('-' * 28)
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profits))
print('Average Change: ${0:.2f}'.format(average_change))
print("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + least_month + " ($" + str(greatest_decrease) + ")")

s = """
Financial Analysis
----------------------------
Total Months: {0}
Total: ${1}
Average Change: ${2:.2f}
Greatest Increase in Profits: Aug-16 ({3})
Greatest Decrease in Profits: Feb-14 ({4})
""".format(total_months, total_profits, average_change, 4, 5)
