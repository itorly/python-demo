# 8.8. Predefined Clean-up Actions
# After the statement is executed, the file f is always closed,
# even if a problem was encountered while processing the lines.
with open('cats.txt') as f:
    for line in f:
        print(line.rstrip())