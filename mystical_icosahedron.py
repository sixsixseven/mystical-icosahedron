#	Python 3; Written by github.com/sixsixseven, the world's first fully-autonomous underwater coputer programmer.

import time
import random as r
from os import system

def number_to_fortune(x):
	fortune = {0:"As I see it, yes.",
	1:"Ask again later.",
	2:"Better not tell you now.",
	3:"Cannot predict now.",
	4:"Concentrate and ask again.",
	5:"Don’t count on it.",
	6:"It is certain.",
	7:"It is decidedly so.",
	8:"Most likely.",
	9:"My reply is no.",
	10:"My sources say no.",
	11:"Outlook not so good.",
	12:"Outlook good.",
	13:"Reply hazy, try again.",
	14:"Signs point to yes.",
	15:"Very doubtful.",
	16:"Without a doubt.",
	17:"Yes.",
	18:"Yes – definitely.",
	19:"You may rely on it."
	}
	return fortune[x]

def mystical_icosahedron(x):
	if x == "q":
		exit()
	
	print("\n")
	print("Passing your question to the ether...\n")
	time.sleep(r.randrange(4))
	system("clear")
	print("\n")
	print(number_to_fortune(r.randrange(20)))
	print("\n")
	again()
	
def exit():
	system("clear")
	raise SystemExit

def again():
	while True:
		again = input("Again? (Y/N): ").lower()
		if again == "n":
			exit()
		elif again == "y":
			break
		else:
			system("clear")
			continue

while True:
	system("clear")
	print("\n")
	mystical_icosahedron(input("Seek your answer with the Oracle, or enter \"Q\" to immediately seal your fate: ").lower())
