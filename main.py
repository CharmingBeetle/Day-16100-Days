print("***FAMOUS QUOTES OF HISTORY***")
print()
print("Fill in the blank words for each quote and see how much you know your history!")
attempt = 1
while True:
  q1 = input("To be or ____ to be, that is the question.")
  if q1 == "not":
    print("You are correct! You made", attempt, "attempts to answer.")
  else:
    print("Nope. Try again!")
    attempt += 1
  if q1 == 'not':
    break
