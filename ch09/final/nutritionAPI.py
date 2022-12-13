import requests

class Nutrition:
  def __init__(self, ingredient):
    self.api_url = f'https://api.edamam.com/api/nutrition-data?app_id=29419d8a&app_key=a0b2f22473dbf8b1af94e8f18ecf7c40&nutrition-type=logging&ingr={ingredient}'


  def getCalories(self):
    ''' returns calories '''
    response = requests.get(self.api_url)
    response = response.json()
    return response["calories"]

  def getProtein(self):
    ''' returns protein '''
    response = requests.get(self.api_url)
    response = response.json()
    proteinInfo = response['totalNutrients']['PROCNT']
    result = proteinInfo['quantity']
    return result
    
  def getCarbs(self):
    ''' returns carbs '''
    response = requests.get(self.api_url)
    response = response.json()
    carbsInfo = response['totalNutrients']['CHOCDF.net']
    result = carbsInfo['quantity']
    return result

  def getSugar(self):
    ''' returns sugar '''
    response = requests.get(self.api_url)
    response = response.json()
    sugarInfo = response['totalNutrients']['SUGAR']
    result = sugarInfo['quantity']
    return result

  def getSodium(self):
    ''' returns sodium amount '''
    response = requests.get(self.api_url)
    response = response.json()
    saltInfo = response['totalNutrients']['NA']
    result = saltInfo['quantity']
    return result

  def getFat(self):
    ''' returns fat amount'''
    response = requests.get(self.api_url)
    response = response.json()
    fatInfo = response['totalNutrients']['FAT']
    result = fatInfo['quantity']
    return result
