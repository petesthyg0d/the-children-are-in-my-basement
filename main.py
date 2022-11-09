import asyncio
import os
import random
import discord
import time
from Discord.ui import Button, View
import requests 
import tracemalloc
from discord.ext import commands
my_secret = os.environ['TOKEN1']
WeatherAPIKEY = os.environ['WeatherAPIKEY']


intents = discord.Intents.all()

helpCommand = commands.DefaultHelpCommand(no_category='Commands')

#Add your prefix as an ! for your bot commands
bot = commands.Bot(command_prefix = '!Petey ', intents = intents, helpCommand = helpCommand)

#print(requests.get("https://api.thecatapi.com/v1/images/search?limit=1").json()[0]['url'])
#print(requests.get("https://jisho.org/api/v1/search/words?keyword=ame").json()['data'][1]["senses"][0]["english_definitions"])
#Print a message to the console when your bot is online
@bot.event
async def on_connect():
  print("Your bot is online.")
  
@bot.command(brief="Syntax: Petey! Name ... Who made the bot?")
async def Name(ctx):
  await ctx.reply("This bot was created by Mr.Petey and Big Brian!")

@bot.command(aliases=["Math", "math", "arithmetic"], brief="Syntax: Petey! Arithmetic 1, 2, 3, or 4... Do basic operations. 1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division.")
async def Arithmetic(ctx, num1, num2, MathType):
  if (MathType == "1"):
    Answer = int(num1) + int(num2)
    ctx.send(Answer)
  if (MathType == "2"):
    Answer = int(num1) - int(num2)
    ctx.send(Answer)
  if (MathType == "3"):
    Answer = int(num1) * int(num2)
    ctx.send(Answer)
  if (MathType == "4"):
    Answer = int(num1) / int(num2)
    ctx.send(Answer)
  else:
    ctx.reply("I don't understand what you are trying to do... make sure you are using the proper syntax:")
    ctx.reply("!Petey Arithmetic, Variable1, Variable2, MathType (1 = 'Addition', 2 = 'Subtraction'), 3 = 'Multiplication' 4 = 'Division.'")

@bot.command(aliases=["date"])
async def Date(ctx):
  DateRandom = random.randint(1, 4)
  if (DateRandom == 1):
    ctx.send('https://www.liveeatlearn.com/wp-content/uploads/2018/12/date-fruit-photo-vert-650x860.jpg.webp')
  if (DateRandom == 2):
    ctx.send('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/first-date-1660910171.jpg?crop=0.6666666666666666xw:1xh;center,top&resize=980:*')
  if (DateRandom == 3):
    ctx.send('https://14509501.fs1.hubspotusercontent-na1.net/hubfs/14509501/Imported_Blog_Media/different-calendar-date-conventions.jpg')
  if (DateRandom == 4):
    ctx.send('DATED.PNG')

@bot.command(aliases=["8ball", "8Ball"])
async def Eightball(ctx, PREGUNTO):
  Eightball = random.randint(1, 5)
  if (Eightball == 1):
    ctx.send(str(PREGUNTO), str("Yes, 100% chance"))
  if (Eightball == 2):
    ctx.send(str(PREGUNTO), str("Work hard and it's possible! :D"))
  if (Eightball == 3):
    ctx.send(str(PREGUNTO), str("Yeah, sure."))
  if (Eightball == 4):
    ctx.send(str(PREGUNTO), str("Maybe..."))
  if (Eightball == 5):
    ctx.send(str(PREGUNTO), str("Theoretically..."))
  if (Eightball == 6):
    ctx.send(str(PREGUNTO), str("Possible, it's possible."))
  if (Eightball == 7):
    ctx.send(str(PREGUNTO), str("No, not in a million years."))
  if (Eightball == 8):
    ctx.send(str(PREGUNTO), str("no"))
@bot.command()

async def Spanish(ctx, word):
  ctx.send(spanishdict.com/translate/ + word)



@bot.command(aliases=["rps", "RockPaperScissors", "rockpaperscissors"])
async def RPS(ctx, word):
  ListOfMessages = ["YOU DARE CHALLENGE THE BEST ROCK PAPER SCISSORS BOT EVER?", "YOU FOOL, YOU MORON, YOU ABSOLUTE BAFOON! I AM THE KING OF ROCKER PAPER SCISSORS." "HAHAHAHAHAHAHAHAHAHAHA WHAT A FOOL YOU ARE, TRYING TO CHALLENGE THE BEST ROCK PAPER S CISSORS PLAYER EVER.", "Abosolute bozo you are, thinking you can beat the undefeated rock paper scissors robot." "Sad, it's sad, very sad that your monkey brain believes that you can beat a rock paper scissors GOD."]
  ctx.send(ListOfMessages[random.randint(1, 5)])
  
  if (word.lower() == "rock"):
    ctx.send("I see that you chose rock...")
    await asyncio.sleep(1)
    ctx.send("As a result, I choose...")
    await asyncio.sleep(1)
    ctx.send("PAPER MUWAHAHAHAHA.")
    await asyncio.sleep(0.5)
    ctx.send("I win again.")
    
  if (word.lower() == "paper"):
    ctx.send("Paper, what an interesting option...")
    await asyncio.sleep(1)
    ctx.send("Because of your choice of paper, I choose,")
    await asyncio.sleep(1)
    ctx.send("SCISSORSSSSS")
    await asyncio.sleep(0.5)
    ctx.send("I win as per usual.")    
    
  if (word.lower() == "scissors"):
    ctx.send("Scissors, what a great choice... for a... FOOOL")
    await asyncio.sleep(1)
    ctx.send("I know what to choose, I have ran the calculations.")
    await asyncio.sleep(1)
    ctx.send("I CHOOSE, ROOCK.")
    await asyncio.sleep(0.5)
    ctx.send("I win baby.")    
    
  else:
    ctx.send("That is not an option, you lose, and I win, fool!")

#Use a Joke API to get a joke setup, wait a few seconds
#and deliver the punchline.
@bot.command(brief="Syntax: Petey! Joke ... Gives funny jokes and punchlines gratuitously.")
async def Joke(ctx):
  #Variable to hold the URL
  URL = "https://official-joke-api.appspot.com/random_joke"
  #Ask our bot to go to the URL
  req = requests.get(URL)

  #Date variable that holds the JSON data, that the API holds.
  data = req.json()

  #Pull the joke setup from the JSON data
  setup = data["setup"]

  punchline = data["punchline"]

  await ctx.send(setup)
  #import asyncio
  #Pause ytour bot, but allow it to execute other functions.
  await asyncio.sleep(3)
  await ctx.send(punchline)

@bot.command(brief="Syntax: Petey! Weather YourZIP celsiusORfarenheit ... Displays the weather")
async def Weather(ctx, zip, type):
  #Variable to hold the URL
  global WeatherAPIKEY
  URL = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&appid=" + WeatherAPIKEY
  #Ask our bot to go to the URL
  req = requests.get(URL)
  
  #Date variable that holds the JSON data, that the API holds.
  data = req.json()

  desc = data["weather"][0]["description"]
  temp = data["main"]["temp"]
  if (type == "celsius"):
    temp -= 273.15
    await ctx.send(desc + " " + str(temp) + " degrees celsius.")
  if (type == "farenheit"):
    temp = (temp - 273.15) * 9/5 + 32
    await ctx.send(desc + " " + str(temp) + " degrees farenheit.")


@bot.command(aliases=["JapanesetoEnglish"], brief="Syntax: Petey! JapanesetoEnglish JapaneseWord ... Translates Anime Language to English.")
async def JtE(ctx, SEARCHWORD):
   #Variable to hold the URL
   URL = "https://jisho.org/api/v1/search/words?keyword=" + str(SEARCHWORD)
   slug = (requests.get("https://jisho.org/api/v1/search/words?keyword=" + str(SEARCHWORD)).json()['data'][0]["senses"][0]["english_definitions"])
   slug3 = (requests.get("https://jisho.org/api/v1/search/words?keyword=" + str(SEARCHWORD)).json()['data'][0]["senses"][0]["parts_of_speech"])
   #Ask our bot to go to the URL
   req = requests.get(URL)

   #Date variable that holds the JSON data, that the API holds.
   data = req.json()
   #Pull the joke setup from the JSON data
   
   await ctx.send("===================================")
   await ctx.send("The Japanese word: " + str(SEARCHWORD) + ", in English is:")
   await ctx.send("ㅤㅤㅤㅤㅤ")
   await ctx.send(str(slug) + " (Meaning of word)")
   await ctx.send(str(slug3) + " (Part of speech of word)")
   await ctx.send("===================================")

@bot.command(aliases=["EnglishtoJapanese"], brief="Syntax: Petey! EnglishtoJapanese EnglishWord ... Translates English to Anime Language.")
async def EtJ(ctx, SEARCHWORD):
   #Variable to hold the URL
   URL = "https://jisho.org/api/v1/search/words?keyword=" + str(SEARCHWORD)
   slug = (requests.get("https://jisho.org/api/v1/search/words?keyword=" + str(SEARCHWORD)).json()['data'][0]["japanese"][0]["word"])
   slug2 = (requests.get("https://jisho.org/api/v1/search/words?keyword=" + str(SEARCHWORD)).json()['data'][0]["japanese"][0]["reading"])
   slug3 = (requests.get("https://jisho.org/api/v1/search/words?keyword=" + str(SEARCHWORD)).json()['data'][0]["senses"][0]["parts_of_speech"])
   #Ask our bot to go to the URL
   req = requests.get(URL)

   #Date variable that holds the JSON data, that the API holds.
   data = req.json()
   #Pull the joke setup from the JSON data
   
   await ctx.send("===================================")
   await ctx.send("The English word: " + str(SEARCHWORD) + ", in Japanese is:")
   await ctx.send("ㅤㅤㅤㅤㅤ")
   await ctx.send(str(slug) + " (Kanji of word)")
   await ctx.send(str(slug2) + " (Phonetic reading of word)")
   await ctx.send(str(slug3) + " (Part of speech of word)")
   await ctx.send("===================================")

@bot.command(aliases=["cat"], brief="Syntax: Petey! Cat ... Displays a random cat image.")
async def Cat(ctx):
  # #Variable to hold the URL
  # URL = 
  # #Ask our bot to go to the URL
  # req = requests.get("https://api.thecatapi.com/v1/images/search?limit=1").json()[0]['url']

  # #Date variable that holds the JSON data, that the API holds.
  # data = req.json()

  # #Pull the joke setup from the JSON data
  # # CATPIC = 
  # print(data[0]["url"])
  CATPIC = requests.get("https://api.thecatapi.com/v1/images/search?limit=1").json()[0]['url']
  # punchline = data["punchline"]

  Mess = random.randint(1, 15)
  if (Mess == 1):
    MESSAGE = "Generating C A T..."
  elif (Mess == 2):
    MESSAGE = "CAT GLORY IN CREATION..."
  elif (Mess == 3): 
    MESSAGE = "Making the purriest of felines..."  
  elif (Mess == 4):
    MESSAGE = "The purfect image is in the making..."
  elif (Mess == 5): 
    MESSAGE = "Paws for just a second and loot at the image..." 
  elif (Mess == 6):
    MESSAGE = "Meowsers! You're about to see an amazing creation..."
  elif (Mess == 7): 
    MESSAGE = "Developing purfection..."
  elif (Mess == 8):
    MESSAGE = "The kitten is fittin in the screen..."
  elif (Mess == 9): 
    MESSAGE = "Translating tumultuous tabbies thoughtfully..."   
  elif (Mess == 10):
    MESSAGE = "Fabulous feline friends in the making..."
  elif (Mess == 11): 
    MESSAGE = "Creating an almagination of cutness..."   
  elif (Mess == 12):
    MESSAGE = "Sculpting the perfect Abyssinian."
  elif (Mess == 13): 
    MESSAGE = "The only animal that cannot taste sweetness, in an image..."
  elif (Mess == 14):
    MESSAGE = "'Meow meow meow,' they say in the cat."
  elif (Mess == 15): 
    MESSAGE = "VIVA LA FELINE REVOLUTION!"
    
  await ctx.send(MESSAGE)
  await asyncio.sleep(3)
  await ctx.send(CATPIC)

@bot.command(aliases=["FindWesbite", "website", "Website"], brief="Syntax: Petey! findWebsite websiteURL ... Displays a summary of a website.")
async def findWebsite(ctx, search):
  #Variable to hold the URL
  REDDITA = requests.get("https://list.ly/api/v4/meta?url=http://" + str(search)).json()['metadata']["url"]
  REDDITB = requests.get("https://list.ly/api/v4/meta?url=http://" + str(search)).json()['metadata']["name"]
  REDDITC = requests.get("https://list.ly/api/v4/meta?url=http://" + str(search)).json()['metadata']["description"]
  #REDDITD = requests.get("https://list.ly/api/v4/meta?url=http://" + str(search)).json()['metadata']["images"]
  
  await ctx.send("===================================")
  await ctx.send("Website: " + str(REDDITA) + " Information: **B E L O W**")
  await ctx.send("ㅤㅤㅤㅤㅤ")
  await ctx.send("Name of website: " + str(REDDITB))
  await ctx.send("Description of website: " + str(REDDITC))
  #await ctx.send("Available images: " + str(REDDITD))
  await ctx.send("===================================")
  
@bot.command(aliases=["Message"], brief="Syntax: Petey! Message ... B U T T O N S")
async def message(ctx):
  button1 = Button(label = "Click Me!", style = discord.ButtonStyle.orange, emoji = "💪")
  button2 = Button(label = "Go to Petey's school website!", url="https://petersheiniscodehsme-4526095.codehs.me/", emoji = "🤓")
  button3 = Button(label = "Go to Big Sean's school website!", url="https://brianzhang247codehsme-4526119.codehs.me/index.html", emoji = "😎")
bot.run(my_secret) 

#Copy your bot token from discord developer

#Mr.Willis code :O below:


#async def Time(ctx, time1, time2):
#  resp="yo"
#  if "am" in time2.lower():
#    resp="Good Morning!"
#  elif "pm" in time2.lower():
#    if int(time1) < 5:
#      resp="Good Afternoon!"
#    else:
#      resp="Good evening!"
#  else:
#    resp="Cannot compute...but have a great day!"
#  await ctx.send(resp)
#139590106688







