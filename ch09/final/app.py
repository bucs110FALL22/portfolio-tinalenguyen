import nutritionAPI
import fitnesscalcAPI
import pygame

class nutriMacro:  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((500,500))
    self.age = 0
    self.height = 0
    self.weight = 0
    self.bmiDone = False
    self.mealTrackerDone = False
    self.nutritionDict = {'Fat (g): ': 0, 'Carbs (g): ': 0, 'Protein (g): ': 0, 'Sugar (g): ': 0, 'Sodium (mg): ': 0, 'Calories: ': 0}
    
  def main(self):
   self.screen.fill("white")
    
   logo = pygame.image.load("assets/logo.png")
   logo = pygame.transform.scale(logo, (420, 160))
   self.screen.blit(logo, (0 , -10))
  
   leaf = pygame.image.load("assets/leaf.png")
   leaf = pygame.transform.scale(leaf, (40, 80))
   self.screen.blit(leaf, (409, 30))
  
   bmiCalcBtn = pygame.image.load("assets/bmiCalcBtn.png")
   bmiCalcBtn = pygame.transform.scale(bmiCalcBtn, (215, 60))
   self.screen.blit(bmiCalcBtn, (130 , 150))
  
   proteinBtn = pygame.image.load("assets/proteinBtn.png")
   proteinBtn = pygame.transform.scale(proteinBtn, (215, 60))
   self.screen.blit(proteinBtn, (130 , 225))
  
   mealTrackerBtn = pygame.image.load("assets/mealTrackerBtn.png")
   mealTrackerBtn = pygame.transform.scale(mealTrackerBtn, (215, 60))
   self.screen.blit(mealTrackerBtn, (130 , 300))
  
   statsBtn = pygame.image.load("assets/statsBtn.png")
   statsBtn = pygame.transform.scale(statsBtn, (215, 60))
   self.screen.blit(statsBtn, (130 , 400))
  
   pygame.display.flip()
  
   running = True
   while running:
     for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x < 345 and x > 130 and y < 210 and y > 150:
          self.bmiCalc()
        elif x < 345 and x > 130 and y < 285 and y > 225:
          self.proteinLookup()
        elif x < 345 and x > 130 and y < 360 and y > 300:
         self.mealTracker()
        elif x < 345 and x > 130 and y < 460 and y > 400:
          self.getStats()
   
  
  
  def bmiCalc(self):
   ''' calculates BMI based off of age weight and height '''
   self.age = input("What is your age?")
   self.weight = input("What is your weight in kilograms?")
   self.height = input("What is your height in centimeters?")
   self.gender = input("What was your assigned sex at birth? (female/male) ")
   fitnessCalc = fitnesscalcAPI.FitnessCalculator(function="bmi")
   answer = fitnessCalc.getBMI(self.age, self.weight, self.height)
   print("Your BMI is " + str(answer))
    
   statSaved = pygame.image.load("assets/statisticSaved.png")
   statSaved = pygame.transform.scale(statSaved, (150, 30))
   self.bmiDone = True
   self.screen.blit(statSaved, (5, 470))
  
   pygame.display.flip()
  
  def proteinLookup(self):
    food = input("What food would you like to input?")
    nutrition = nutritionAPI.Nutrition(ingredient=food)
    results = nutrition.getProtein()
    print("Protein amount (grams):" + str(results))
  
  def mealTracker(self):
    ''' Keeps track of fat, carbs, protein, sugar, sodium, and calories '''
    
    meals = []
 
    
    running = True
    while running:
      meal = input("Please input a food you had today with its amount. If you are finished inputting meals, please type 'done'.")
      if meal == "Done" or meal == "done":
        running = False
        self.mealTrackerDone = True
      else:
        meals.append(meal)
        nutrition = nutritionAPI.Nutrition(ingredient=meal)
        self.nutritionDict['Fat (g): '] += nutrition.getFat()
        self.nutritionDict['Carbs (g): '] += nutrition.getCarbs()
        self.nutritionDict['Protein (g): '] += nutrition.getProtein()
        self.nutritionDict['Sugar (g): '] += nutrition.getSugar()
        self.nutritionDict['Sodium (mg): '] += nutrition.getSodium()
        self.nutritionDict['Calories: '] += nutrition.getCalories()

    self.screen.fill("white")

    mealOverview = pygame.image.load("assets/mealOverview.png")
    self.screen.blit(mealOverview, (70, 30))
    
    text = str(meals)
    font = pygame.font.SysFont(None, 15)
    mealsTxt = font.render(text, True, "black")
    self.screen.blit(mealsTxt, (0, 100))
    quit = "Press enter/return to go back to the main page"
    font2 = pygame.font.SysFont(None, 20)
    quit = font2.render(quit, True, "black")
    self.screen.blit(quit, (0, 2))
    pygame.display.flip()


    
    spacing = 50
    for element in self.nutritionDict:  
      rowText = str(element) + " " + str(self.nutritionDict[element]) 
      font1 = pygame.font.SysFont(None, 40)
      info = font1.render(rowText, True, "black")
      self.screen.blit(info, (0, 100+spacing))
      spacing+=40
      pygame.display.flip()
                     

    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
          running = False   
          self.main()
      
  def getStats(self):
    ''' Tells user if they met their maintenance macro goals or not '''
    self.screen.fill("white")
    if self.mealTrackerDone and self.bmiDone:
      fitnessCalc = fitnesscalcAPI.FitnessCalculator(function="macrocalculator")
      msg = "Here are your maintenance stats: " 
      font3 = pygame.font.SysFont(None, 40)
      msg = font3.render(msg, True, "black")
      self.screen.blit(msg, (0, 2))
      print( fitnessCalc.getMacros(self.age, self.gender, self.weight, self.height))
      data = fitnessCalc.getMacros(self.age, self.gender, self.weight, self.height)
      msg2 = "Protein (g): " + str(data['balanced']['protein'])
      font4 = pygame.font.SysFont(None, 30)
      if data['balanced']['protein'] > self.nutritionDict['Protein (g): ']:
        color = "red"
      else:
        color = "green"
      msg2 = font4.render(msg2, True, color)
      self.screen.blit(msg2, (0, 100))
      pygame.display.flip()

      msg3 = "Carbs (g): " + str(data['balanced']['carbs'])
      font4 = pygame.font.SysFont(None, 30)
      if data['balanced']['carbs'] > self.nutritionDict['Carbs (g): ']:
        color = "red"
      else:
        color = "green"
      msg3 = font4.render(msg3, True, color)
      self.screen.blit(msg3, (0, 150))
      pygame.display.flip()

      msg4 = "Fat (g): " + str(data['balanced']['fat'])
      font4 = pygame.font.SysFont(None, 30)
      if data['balanced']['fat'] > self.nutritionDict['Fat (g): ']:
        color = "red"
      else:
        color = "green"
      msg4 = font4.render(msg4, True, color)
      self.screen.blit(msg4, (0, 200))
      pygame.display.flip()

      msg5 = "The stats are green if they were met today and red if they were not." 
      font3 = pygame.font.SysFont(None, 20)
      msg5 = font3.render(msg5, True, "black")
      self.screen.blit(msg5, (0, 250))
      pygame.display.flip()

      msg6 = "Press enter to return to the main page." 
      font3 = pygame.font.SysFont(None, 20)
      msg6 = font3.render(msg6, True, "black")
      self.screen.blit(msg6, (0, 400))
      pygame.display.flip()
      
      running = True
      while running:
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            running = False   
            self.main()
      
    else:
      error = "Please fill out the BMI and meal tracker information."
      font3 = pygame.font.SysFont(None, 20)
      error = font3.render(error, True, "black")
      self.screen.blit(error, (0, 2))
      quit = "Press enter to go to the main page."
      font3 = pygame.font.SysFont(None, 20)
      quit = font3.render(quit, True, "black")
      self.screen.blit(quit, (0, 100))
      pygame.display.flip()
      running = True
      while running:
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            running = False   
            self.main()
      



  