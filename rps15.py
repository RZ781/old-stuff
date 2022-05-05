import random

alpha = "abcdefghijklmno"

a = input("option (a-o)? ").lower()
if a not in alpha:
  exit("invalid choice")
b = input("option (a-o)? ").lower()
if b not in alpha:
  exit("invalid choice")

# finds numbers of choices
n = ord(a)-97
m = ord(b)-97

dist = (n-m+15)%15

if dist == 0:
  print("draw")
elif dist <= 7:
  print("player 1 wins")
else:
  print("player 2 wins")
