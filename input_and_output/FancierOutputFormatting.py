# 7.1. Fancier Output Formatting
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
output = '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(output)