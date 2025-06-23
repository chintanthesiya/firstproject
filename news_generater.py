# generate news and fake and funny and print there project using Python
import random
import pyttsx3

categories = {
    "Politics": ["Nirmala Sitharaman", "Prime Minister Modi"],
    "Bollywood": ["Shahrukh Khan"],
    "Sports": ["Virat Kohli"],
    "Animals": ["a Mumbai cat", "a group of monkeys"],
    "Public": ["an auto-rickshaw driver from Delhi"]
}
subjects=[
    "shahrukh khan",
    "virat kohli",
    "nirmala sitaraman",
    "a mumbai cat",
    "a group of monkeys",
    "prime minister modi",
    "auto rikshaw driver from delhi"
]
actions=["launches",
    "cancels",
    "dances with",
    "decalres war on",
    "eat",
    "orders",
    "celebration",
    ]
place_or_things=["at red fort",
    "in mumbai local train",
    "a plote of samosa",
    "inside parliment",
    "at ganga ghat",
    "suring ipl match",
    "india gate"]
with open("fake_news_log.txt", "a") as file:
    while True:
        category=random.choice(list(categories.keys()))
        subject=random.choice(subjects)
        action=random.choice(actions)
        place=random.choice(place_or_things)
        headline=f"{category} : BREAKING NEWS ------ {subject} {action} {place} \n"
        
   
        print("\n ",headline)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices') 
        engine.say(headline)
        engine.runAndWait()
        file.write(headline + "\n")
        user=input("do you want anoter headline ? (yes/no)").strip().lower() # strip is remove spaces in user input
       
        if user!="yes":
            break

print("\n thanks for using the fake news headline generator. have a fun day")

  



