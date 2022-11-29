import requests
from random import choice
import pyfiglet 

header = pyfiglet.figlet_format("DAD JOKE 3000!")
print(header)

jtopic = input ("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url, headers = {"Accept":"application/json"}, 
	params={"term":jtopic}).json()

num_jokes = res["total_jokes"] # print (len(res["results"]))
results = res ["results"]

if num_jokes > 1:
	print (f"THERE ARE {num_jokes} JOKES! HERE'S ONE: ")
	print (choice(results)["joke"]) # random.choice returns a random element from a list
elif num_jokes == 1: # NECESSARY for the print statement plural or singular
	print (f"I found one joke about {jtopic}")
	print (results[0]["joke]"])# 0 to access the list and joke to access the joke
else:
	print (f"there are no jokes with: {jtopic}")






# jokes = res.json()
# jokes1 = jokes["results"]



# print(f"I've got on joke about cat: {jokes1}")
