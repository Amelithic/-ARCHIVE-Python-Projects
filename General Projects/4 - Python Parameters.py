#10/05/2020
def output_user_details(user_name, given_name, age):
	print("Username:", user_name)
	print("Given Name:", given_name)
	print("Age:", age)
	
output_user_details("ada", "Ada Lovelace", 36)

def triple_it(number):
	value = 3 * number
	return value

x = triple_it(5)
print(x)