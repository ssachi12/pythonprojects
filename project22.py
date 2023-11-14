import requests
response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
cocktails=response.json()['drinks'][0]
name=cocktails['strDrink']
glass=cocktails['strGlass']
alcohol=cocktails['strAlcoholic']
instructions=cocktails['strInstructions']

print(f"Name: {name}")
print(f"Type of glass: {name}")
if alcohol=="Alcoholic":
    print("Alcoholic : Yes")
else:
    print("Alcoholic : No")
print(f"Instructions: {instructions}")