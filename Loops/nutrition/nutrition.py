cal_of_fruits =[
    {"fruit":"apple", "calorie":"130"},
    {"fruit":"avocado", "calorie":"50"},
    {"fruit":"banana", "calorie":"110"},
    {"fruit":"cantaloupe", "calorie":"50"},
    {"fruit":"grapefruit", "calorie":"60"},
    {"fruit":"grapes", "calorie":"90"},
    {"fruit":"honeydew melon", "calorie":"50"},
    {"fruit":"kiwifruit", "calorie":"90"},
    {"fruit":"lemon", "calorie":"15"},
    {"fruit":"lime", "calorie":"20"},
    {"fruit":"nectarine", "calorie":"60"},
    {"fruit":"orange", "calorie":"80"},
    {"fruit":"peach", "calorie":"60"},
    {"fruit":"pear", "calorie":"100"},
    {"fruit":"pineapple", "calorie":"50"},
    {"fruit":"plums", "calorie":"70"},
    {"fruit":"strawberries", "calorie":"50"},
    {"fruit":"sweet cherries", "calorie":"100"},
    {"fruit":"tangerine", "calorie":"50"},
    {"fruit":"watermelon", "calorie":"80"},
]
  
name = input("Item: ")

for fruits in cal_of_fruits:
	if name.lower() == fruits["fruit"]:
		print("Calories:", fruits["calorie"])
	else:
		None
		# print("", sep="", end="")
