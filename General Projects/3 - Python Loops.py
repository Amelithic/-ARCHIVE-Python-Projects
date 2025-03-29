#08/05/2020
#example by amazon python course 2020
affirmations = {
	"loved": "You love and accept yourself exactly as you are.",
	"valuable": "You are a valuable person with many good qualities.",
	"courageous": "You are strong and face difficulties with courage.",
	"capable": "You are capable of achieving anything you want.",
	"deserving": "You are loved and loving. You deserve to receive love.",
	"positive": "You are a positive person and you attract positive events to your life.",
	"responsible": "You are responsible for yourself and your own future.",
	"generous": "You look at everyone and everything with kind and generous eyes.",
	"perfect": "You are perfect exactly as you are. You accept yourself fully.",
	"healthy": "You are healthy and allow life to flow through you.",
	"respectful": "You respect all creatures you come into contact with.",
	"intelligent": "You are an intelligent person and you learn from everybody.",
	"thankful": "You are thankful for every day of your life.",
	"relatable": "You strive to maintain good relationships with others.",
	"intuitive": "You listen to your intuition.",
	"grateful": "You are grateful for all your blessings.",
	"strong": "You live your life fully with strength and joy."
	}

the_keys = ""
for key in affirmations:
	the_keys = the_keys + key + " "
print("The following words are recognised by the Affirmation Bot:")
print(the_keys)

while True:
	message_output = False
	sentence = input("How are you feeling? ")
	sentence = sentence.lower()
	
	if sentence == "q":
		break
		
	words = sentence.split(" ")
	
	for word in words:
		if word in affirmations:
			print(affirmations[word])
			message_output = True
			
	if not message_output:
		print("Keep on going you will eventually find what you are seeking.")
			  
print("Bye!")