import json
import requests

def main():
  response = requests.get('https://excuser.herokuapp.com/v1/excuse').json()
  print(response)

main()
