#08/05/2020

with open('languages.txt', 'r+') as f:
    x = f.read().splitlines() 
    print(x)
    y = f.write(x)
    x = f.read()
    print(x)