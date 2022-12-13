import requests

class FitnessCalculator:
  def __init__(self, function):
    self.api_url = f'https://fitness-calculator.p.rapidapi.com/{function}'
  
    querystring = {"activityid":"bi_1","activitymin":"25","weight":"75"}
  
    self.headers = {
  	"X-RapidAPI-Key": "6ed4c8b152msh6f472c5401097ecp149b80jsn6bd3c118890a",
  	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
  }

  def getBMI(self, age, weight, height):
    ''' calculates bmi based off of age, weight, and height'''
    query = {"age": age, "weight": weight, "height": height}
    response = requests.request("GET", self.api_url, headers=self.headers, params=query).json()
    return response['data']['bmi']

  def getMacros(self, age, gender, weight, height):
    ''' gets needed daily macros based off of BMI '''
    query = {"age":age,"gender":gender,"height":height,"weight":weight,"activitylevel":"3","goal":"maintain"}
    response = requests.request("GET", self.api_url, headers=self.headers, params=query).json()
    return response['data']