import sys
import requests
import datetime

app_id = '6e86cc3f'
app_key: str = '74e448ffe9620af5d263a6f098a20647'
ingredient = input("Enter an ingredient: ")
dietary_reqs = input("Do you have any dietary requirements? Enter yes or no: ")
if dietary_reqs == "yes":
    d_info = input("Please enter one of the following options: \nVegan\nVegetarian\nPescatarian\nDairy-free\n")
    d_info_2 = "user mistake"
    if d_info.lower() not in ["vegan", "vegetarian", "pescatarian", "dairy-free"]:
        d_info_2 = input("Error. Please enter one of the following options: "
                        "\nVegan\nVegetarian\nPescatarian\nDairy-free\n")

    if d_info_2 != "user mistake":
        if d_info_2.lower() not in ["vegan", "vegetarian", "pescatarian", "dairy-free"]:
            print("Error, the program will end now")
            sys.exit()

save = input('Do you want to save your search, enter yes or no : ')
#url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'
now = datetime.datetime.now()
recipe_details = []
#not yet done error handling for all user questions


def recipe_search(ingredient):
    if dietary_reqs.lower().strip() == 'no':
        url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient.lower().strip(),
                                                                               app_id, app_key)
    if dietary_reqs.lower().strip() == "yes":
        try:
            url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}'.format(
                ingredient.lower().strip(), app_id, app_key, d_info.lower().strip())
        finally:
            url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}'.format(
                ingredient.lower(), app_id, app_key, d_info_2.lower().strip())

    result = requests.get(url)
    data = result.json()
    total = len(data['hits'])
    #print(url) to check using correct parameters
    if total == 0:
        print("No recipes found")
    else:
        print("{} recipes found".format(total))
        return data['hits']


def run():
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        details = recipe['label'] + " " + recipe['url']
        recipe_details.append(details)
        print(details)
        print()


def saving():
    save_statement = "This search was performed on {}".format(now.strftime("%d%m%y_%H%M"))
    if save.lower() == "yes":
        file_name = "{}_recipe_search.txt".format(ingredient,)

        with open(file_name, 'w') as new_file:
            for item in recipe_details:
                new_file.write(item + '\n')

        with open(file_name, 'a') as new_file:
            new_file.write(save_statement)
            #new file saved with search results and a timestamp at the end

        print("This search has been saved")
    else:
        print("This search has not been saved")


recipe_search(ingredient)
run()
saving()



repeat = input("Do you want to search for another recipe? Enter yes or no: ")
if repeat.lower() == "yes":
    ingredient = input("Enter an ingredient: ")
    dietary_reqs = input("Do you have any dietary requirements? Enter yes or no: ")
    if dietary_reqs == "yes":
        d_info = input("Please enter one of the following options: \nVegan\nVegetarian\nPescatarian\nDairy-free\n")
        d_info_2 = "user mistake"
        if d_info.lower() not in ["vegan", "vegetarian", "pescatarian", "dairy-free"]:
            d_info_2 = input("Error. Please enter one of the following options: "
                             "\nVegan\nVegetarian\nPescatarian\nDairy-free\n")

        if d_info_2 != "user mistake":
            if d_info_2.lower() not in ["vegan", "vegetarian", "pescatarian", "dairy-free"]:
                print("Error, the program will end now")
                sys.exit()

    recipe_search(ingredient)
    run()
    saving()

else:
    if repeat == "no":
        pass




#second search saving to original search file - unsure how to resolve yet
#cant make it run now with with dietary options
#printing number of recipes twice
