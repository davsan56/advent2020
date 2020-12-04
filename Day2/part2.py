with open("input.txt") as f:
  content = f.readlines()

allowedPasswords = []

for line in content:
  rule, password = line.split(": ")
  number, letter = rule.split(" ")
  firstIndex, secondIndex = [int(x) - 1 for x in number.split("-")]
  # print(firstIndex, "index or", secondIndex, "index should be", letter)
  if password[firstIndex] == letter:
    if not password[secondIndex] == letter:
      allowedPasswords.append(password)
  
  if password[secondIndex] == letter:
    if not password[firstIndex] == letter:
      allowedPasswords.append(password)
      
print(len(allowedPasswords), "allowed passwords")