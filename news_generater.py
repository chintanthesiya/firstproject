# generate news and fake and funny and print there project using Python
import random
import pyttsx3


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
        subject=random.choice(subjects)
        action=random.choice(actions)
        place=random.choice(place_or_things)
        headline=f" BREAKING NEWS {subject} {action} {place}"
        engine = pyttsx3.init()
        engine.say(headline)
        engine.runAndWait()
   
        print("\n ",headline)
        file.write(headline + "\n")
        user=input("do you want anoter headline ? (yes/no)").strip().lower() # strip is remove spaces in user input
       
        if user=="no":
            break

print("\n thanks for using the fake news headline generator. have a fun day")

  



