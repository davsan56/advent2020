import itertools

with open("input.txt") as f:
  content = [int(x) for x in f.readlines()]

for num1, num2, num3 in itertools.combinations(content, 3):
  sum = num1 + num2 + num3
  if sum == 2020:
    print(num1 * num2 * num3)