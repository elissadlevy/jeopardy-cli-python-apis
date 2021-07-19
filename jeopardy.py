import requests
import random

categoriesRequested = 100
categories = requests.get(f'http://jservice.io/api/categories?count={categoriesRequested}').json()

categoriesOffered = 5
categories = random.choices(categories, k=categoriesOffered)

print("Your available categories are:")
for category in categories:
    print(category["title"])

choice = input("Which of these categories do you choose? ")
choiceID = 0
while choiceID == 0:
    for category in categories:
        if category["title"] == choice:
            choiceID = category["id"]
    if choiceID == 0:
        choice = input("Please try again.  Which category do you choose? ")

response = requests.get(f'http://jservice.io/api/clues?category={choiceID}').json()

print("Your first question is...")
userAns = input(response[0]["question"] + "... ")
if userAns == response[0]["answer"]:
    print("You got it right!")
else:
    print("Sorry, that was incorrect.")

# for i in response:
#     print(i["category"]["title"])
# print(len(response))
# print(response[0]["category"]["title"])

# for i in response:
#     userAns = input(i["question"] + " ")
#     if userAns == i["answer"]:
#         print("Hooray!")
#     else:
#         print("WRONG")