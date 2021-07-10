import pyttsx3
#
# from kivy.lang import builder
# from kivymd.app import MDApp
#
# class Test(MDApp):
#     def build(self):
#         self.title = "Kids Help"
#         self.theme_cls.primary_palette = "Blue"
#         return builder.load_string('''
#         ''')


friend = pyttsx3.init()
"""VOICE"""
voices = friend.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
friend.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#REVISION Last Phase  might be 5/6.



def add_new():
    op = input("Enter yor file name")
    try:
        open(f"{op}.txt",'rb')
    except:
        open(f"{op}.txt", 'a')
    ques = input("enter your question")

    file_open = open(f'{op}.txt','a')
    file_open.write(f"Question - {ques}")
    ans = input("Enter your answer")
    file_open = open(f"{op}.txt",'a')
    file_open.write(f"\nAnswer - {ans}\n\n")
    file_open.close()


def called():
    n = int(input("type msg length"))
    for i in range(n):
        speak = input("revise you answer")
        friend.say(speak)
        friend.runAndWait()
    m = input("you want to continue, type yes or y")
    if m == "y" or m=="Y" or m=="yes" or m=="YES" or m=="Yes"  :
        called()
    else:
        speak = "good bye"
        friend.say(speak)
        friend.runAndWait()

def Revision():
    ans_sheet = ()
    rd_ex = input("Enter File Name")
    try:
        data  = open(f"{rd_ex}.txt",'r')
        data = list(data)
        inp = input("enter your question key")
        inp.strip()
        inp = list(inp.split(" "))
        r = 0
        for i in data:
            for j in inp:
                if j in i:
                    if data[r] in ans_sheet:
                        pass
                    else:
                        ans_sheet = (data[r], data[r + 1])
                        for k in ans_sheet:
                            print(k)
                            friend.say(k)
                            friend.runAndWait()
                        continue
            else:
                r = r + 1

    except:
        if FileNotFoundError:
            print(f"{rd_ex}.txt >>> Such Of This File Is Not Exist ! Try Different Name.")
        print("Thank You For Visit")


if __name__ == '__main__':
    print("Choose one of them : ")
    print("Press 1 for Calling Text \nPress 2 for Add More Practice Set. \nPress 3 for Revision \n")
    choice = int(input("What you want to do : "))
    if choice==1:
        print("hello")
        called()
    elif choice==2:
        add_new()
    elif choice==3:
        Revision()
    else:
        print("Enter Correct Choice")








