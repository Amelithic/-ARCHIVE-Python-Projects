#10/05/2020 - Using Processing.py?
# amelithic 2020: amazon challenge 5 [chat bot designer]
# but i made a better bot outside of this course lol
import random as rnd
import string as strg

greetings = ["hello", "hi", "howdy"]
goods = ["great", "not too shabby", "good", "pretty good"]
bads = ["bad", "not very good", "sad"]

compl = {'1':'You have lovely eyes', '2':'You are probably a very nice person', '3':'You\'re a not-stupid person', '4':'Your face is like my emoji cushion \n(very smiley)', '5':'My pet cat likes you (you\'re lucky!)'}

help_menu = "<<Help Menu>> \n \t \'hello\'  -- bot greets you \n \t \'good\'  -- response 1 to greeting \n \t \'bad\'  -- response 2 to greeting \n \t \'compliment me\'  -- bot gives you a \n compliment after you type a number \n \t \'random\'  -- returns random string \n (like minecraft\' obfuscated text) \n \t"


def ran_strng(stringLength=8): #8 by default, but can change when you call function: e.g ran_strg(10) prints 10 characters
    all_chars = strg.ascii_letters + strg.digits
    return ''.join((rnd.choice(all_chars) for i in range(stringLength)))

def setup():
	size(400,400)
	print('it\'s now setup')


def draw():
	background(96, 45, 145)

	def message_options():
		fill(211, 167, 250)
		rect(25, 120, 350, 35)
		if Message.text.lower() in greetings:
			fill(0,0,0)
			text("Hello, how are you?", 35, 145)
		elif Message.text.lower() in goods:
			fill(0,0,0)
			oop = "That\'s " + goods[0] + "!"
			text(str(oop), 35, 145)
		elif Message.text.lower() in bads:
			fill(0,0,0)
			text("Hope you get better soon!", 35, 145)
		elif Message.text.lower() == 'compliment me': #using in so that you don't have to type the full thing
			fill(0,0,0)
			text('Choose a number (1-5)', 35, 145)
	
		elif Message.text == '1':
			fill(0,0,0)
			text(compl['1'], 35, 145)
		elif Message.text == '2':
			fill(0,0,0)
			text(compl['2'], 35, 145)
		elif Message.text == '3':
			fill(0,0,0)
			text(compl['3'], 35, 145)		
		elif Message.text == '4':
			fill(211, 167, 250)
			rect(25, 120, 350, 70)
			fill(0,0,0)
			text(compl['4'], 35, 145)
		elif Message.text == '5':
			fill(0,0,0)
			text(compl['5'], 35, 145)				

		elif Message.text.lower() == 'Gibberish'.lower() or Message.text.lower() == 'random':
			fill(0,0,0)
			text(ran_strng(20), 35, 145)
		elif Message.text.lower() == 'HELP'.lower():
			fill(161, 107, 200)
			rect(25, 120, 350, 245)		
			fill(255,255,255)
			text(help_menu, 35, 145)
		elif Message.text.lower() == "":
			fill(171, 117, 210)
			text("Type \'help\' to see what I can do", 35, 145)
		else:
			fill(0,0,0)
			text("nope, type something else", 35, 145)

	message_options()