#03/12/2019

print('Hello!')
print('I will tell you whether your number is greater than 10.')

def outroon():
  print('...Did I get it right?')
  print('Regardless, this was my first Python program...')
  print('Hope you liked it!!')

x = int(input('Enter your number: '))
y = 10

if x > y:
  print('Your number is greater than 10')
  outroon()
elif x < y:
  print('Your number is less than 10')
  outroon()
elif x == y:
  print('Your number is equal to 10')
  outroon()
else:
  print('Enter a proper number!!')


