from tkinter import *
from tkinter import messagebox
from multiprocessing import Process
import os
import random
import string




adjectives = ["attractive", "bald", "beautiful", "chubby", "clean" "dazzling", 'drab', "elegant", "fancy", "fit", "flabby", "glamorous",
"gorgeous", "handsome", "long", "magnificent", "muscular", "plain", "plump", "quaint", "scruffy", "shapely", "short", "skinny", "stocky", "ugly", "unkempt", "unsightly", "ashy",
"black", "blue", "gray", "green", "icy", "lemon", "mango", "orange", "purple", "red", "salmon", "white", "yellow", "annoying", "grotesque", "godlike", "smelly"
"heavy", "fantastic", "intelligent"

]

nouns = ["able", "achieve", "acoustics", "action", "activity", "aftermath", "afternoon", "afterthought","apparel", "appliance", "beginner",
 "believe", "bomb", "border", "boundary", "breakfast", "cabbage", "cable", "calculator", "calendar", "caption", "carpenter", "cemetery",
 "channel", "circle", "creator", "creature", "education", "faucet", "feather", "friction", "fruit", "fuel", "galley", "guide", "guitar",
 "health", "heart", "idea", "kitten", "laborer", "language", "lawyer", "linen", "locket", "lumber", "magic", "minister", "mitten", "money",
 "mountain", "music", "partner", "passenger", "pickle", "picture", "plantation", "plastic", "pleasure", "pocket", "police",  "pollution",
 "railway", "recess", "reward", "route", "scene", "scent", "squirrel", "stranger", "suit", "sweater", "temper", "territory", "texture",
 "thread", "treatment", "veil", "vein", "volcano", "wealth", "weather", "wilderness", "wren", "wrist", "writer", "monkey", "caveman", "simp",
 "yogurt", "gorilla", "bat", "spider", "centipede", "human", "scout", "heavy", "sniper", "spy", "medic", "soldier", "pyromaniac", "engineer", "instrument"

]


password = [

]










root = Tk()

root.geometry("500x500")

root.resizable(width='False', height='False')

root.title('Project PGen')


title = StringVar()
label = Label(root, text='Welcome to Project PGen!')
label.config(font=("Courier", 24))
label1 = Label(root, text="How strong would you like your password to be?")
label1.config(font=("Courier", 12))
label.pack()
label1.pack()

def choice():
    sel = NumInp.get()

def PReturn():
    psum.config(text=PGEN(), font=("Courier", 18))

NumInp = IntVar()

B1 = Radiobutton(root, anchor=CENTER, variable=NumInp, text="Basic", command=NumInp, value=1)

B2 = Radiobutton(root, anchor=CENTER, variable=NumInp, text="Medium", command=NumInp, value=2)

B3 = Radiobutton(root, anchor=CENTER, variable=NumInp, text="Strong", command=NumInp, value=3)


B1.pack()
B2.pack()
B3.pack()


NumInp.set(0)

label2 = Label(root)
label2.pack()

Gen = Button(root, text="Generate Password", command=PReturn)

Gen.pack()

password = str(PReturn)

psum = Label(root, text='')

psum.pack(side=BOTTOM)

def PGEN():
    num = random.randrange(1, 10000, 1)
    special = random.choice(string.punctuation)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    if NumInp.get() == 1:
        return adjective + noun
    if NumInp.get() == 2:
        return adjective + noun + str(num)
    if NumInp.get() == 3:
        return adjective + noun + special + str(num)


mainloop()





