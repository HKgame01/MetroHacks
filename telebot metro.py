import cohere
import telebot

API_KEY = ""

bot = telebot.TeleBot("")
print("Bot is running!")
@bot.message_handler(commands=['start'])
def greet(message):
  bot.send_message(message.chat.id, "Hello, Welcome to the Disease detector bot. Please write /help to see the commands available.")

@bot.message_handler(commands=['help'])
def hello(message):
  bot.send_message(message.chat.id, """Available Commands :-
    `i got` - to get the disease name
    `/hospital_near_me` - to get hosptitals near you
    `/consult` - TO consult to a real doctor
    `/addme` To add you as a doctor(where our staff will autheticate you)
    `/about` - This bot helps people to get around with diseases in a better way
"""

  )
@bot.message_handler(commands=['about'])
def greet(message):
  bot.send_message(message.chat.id, "Hello, I'm ")
  
@bot.message_handler(commands=['hospital_near_me'])
def greet(message):
  bot.send_message(message.chat.id, "You got https://www.google.com/maps/search/hospital+near+me/")

@bot.message_handler(commands=['consult'])
def greet(message):
  bot.send_message(message.chat.id, "To consult go to t.me/docbot123_bot.")

@bot.message_handler(commands=['addme'])
def greet(message):
  bot.send_message(message.chat.id, "you will be contacted by our staff soon for verification of yours as a doctor.")


def disease_request(message):
  request = message.text.split()
  if len(request) < 3 or request[0].lower() not in "i got":
    return False
  else:
    return True

@bot.message_handler(func=disease_request)
def send_disease(message):
    gg = message.text.split()[2:]
    co = cohere.Client("")
    response = co.generate(
        model='xlarge',
        prompt=f"This program will generate deasease name based on symptoms -- Chest Pain\nAortic Dissection\n\nChest Tightness (Tightness in Chest)\nHeart Attack\n\nChest Tightness (Tightness in Chest)\nHeart Attacks in Women\n\nChronic Pain\nInsomnia\n\nDiarrhea, Dizziness\nJet Lag\n\nExcessive Yawning (Yawning)\nNarcolepsy\n\nExcessive Yawning (Yawning)\nSleep and Sleep Disorders in Children and Teenagers\n\nDistended Stomach (Abdominal Distention)\nAscites\n\nBleeding and Enlarged finger tips, Blue colored skin and Enlarged finger tips, Brittle hair, Change in hair texture, Curved fingernails and Dry skin\nEmphysema\n\nBreast Discharge, Breast Pain\nBreastfeeding\n\nShoulder Pain\nRadiculopathy\n\nSore Tongue\nBurning Mouth Syndrome \n\nChest Pain\nBath Salts\n\n{gg}\n",
        max_tokens=30,
        temperature=1,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    hh=response.generations[0].text
    if "\n" in hh:
        bb=hh.split("\n")
        for i in bb:
            if "" in bb:
                bb.remove("")
    disclamer = "DISCLAIMER: This might be totally wrong as it is guessed by a NLP program, we always recommend to consult to a doctor before going on any medication"

    bot.send_message(message.chat.id, f"Here you go:\n\nWe detected {bb[1]}\n\n\n{disclamer}")
    print(f"symp:{gg}\nresponse:{hh}")
    

bot.polling()
