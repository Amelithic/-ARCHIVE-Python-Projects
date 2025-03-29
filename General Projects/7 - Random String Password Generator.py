#07/07/2020
#python 3.7.1

import random as rnd
import string as stg

def RandPass():
  stringLength = 8
  chars = stg.ascii_letters + stg.digits + stg.punctuation
  password = rnd.choice(stg.ascii_lowercase)
  password += rnd.choice(stg.ascii_uppercase)
  password += rnd.choice(stg.punctuation)
  password += rnd.choice(stg.digits)

  for i in range(stringLength):
    password += rnd.choice(chars)
  passwordList = list(password)
  rnd.SystemRandom().shuffle(passwordList)
  password = ''.join(passwordList)
  return password
    
def AskPass():
  q1 = 'Want a password? y/n'
  print(q1)
  a1 = input()
  if a1 == 'y':
    print("Your password is... ", RandPass())
    print()
    AskPass()
  elif a1 == 'n':
    print("fine then...")
    exit()
  else:
    print("nope, choose a letter: y/n")
    print()
    AskPass()
 
x = 1
def SpamPass():
	print(RandPass() + ' ' + RandPass() + RandPass() + ' ' + RandPass())
	print(x)

y = 5000
while x < y:
	SpamPass()
	x = x + 1
if x == (y - 1):
  print('DONE')