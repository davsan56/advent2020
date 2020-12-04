with open("input.txt") as f:
  content = f.readlines()

allowedPasswords = []

for line in content:
  rule, password = line.split(": ")
  number, letter = rule.split(" ")
  minNum, maxNum = [int(x) for x in number.split("-")]
  # print(minNum, "to", maxNum, "of", letter)
  numOfChars = filter(lambda x: x == letter, password)
  count = len(list(numOfChars))
  # print(count, letter, "i ", password)
  if count >= minNum and count <= maxNum:
    allowedPasswords.append(password)

print(len(allowedPasswords), "allowed passwords")