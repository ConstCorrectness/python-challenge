import csv
import os


filename = os.path.join('Resources', 'budget_data.csv')
output_filename = 'analysis/pybank_financial_analysis.txt'

output_results = ''

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


output_results += 'Financial Analysis' + '\n'
output_results += ('-' * 28) + '\n'
output_results += ("Total Months: " + str(total_months)) + '\n'
output_results += ("Total: $" + str(total_profits)) + '\n'
output_results += ('Average Change: ${0:.2f}'.format(average_change)) + '\n'
output_results += ("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_increase) + ")") + '\n'
output_results += ("Greatest Decrease in Profits: " + least_month + " ($" + str(greatest_decrease) + ")") + '\n'

print(output_results)


with open(output_filename, 'w') as f:
  f.write(output_results)
