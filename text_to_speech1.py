import pyttsx3
friend = pyttsx3.init()

n = int(input("type msg length"))
for i in range(n):
    speak = input("say something")
    friend.say(speak)
    friend.runAndWait()

m = input("you want to continue, type yes or y")
if m=="yes"or"YES"or"Y"or"y":
    x=int(input("what is the length of message"))
    for i in range(x):
        speak = input("say something")
        friend.say(speak)
        friend.runAndWait()
else:
    speak = "good bye"
    friend.say(speak)
    friend.runAndWait()


'''


def tts():
    n = int(input("type msg length"))
    for i in range(n):
        speak = input("say something")
        friend.say(speak)
        friend.runAndWait()
    tts_rpt()



def tts_rpt():
    m = input("you want to continue, type 'yes'")
    if m == "yes":
        tts()
    else:
        speak = "good bye"
        friend.say(speak)
        friend.runAndWait()



tts()

'''