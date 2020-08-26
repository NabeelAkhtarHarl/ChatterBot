from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *


bot=ChatBot("my bot")
convo=[
    'helo',
    'hi there!',
  'what is your name?',
  'my name is BOt,created by Ali',
  'how are you ?',
  'i am fine.',
  'in which city you live?',
  'i live in sialkot',
    'in which language you talk?',
    'i talk in english'
]


trainer=ListTrainer(bot)

trainer.train(convo)
#answer=bot.get_response("what is your name?")
#print(answer)
#print("Talk with Bot")
#while True:
#    query=input()
 #   if query=='exit':
  #      break
   # answer=bot.get_response(query)
    #print("bot : ",answer)

#start GUI
main = Tk()
#box size
main.geometry("500x650")
#page title
main.title("My Chat bot")
#image on page
img = PhotoImage(file="bot.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)
#function for asking to bot
def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    textF.delete(0,END)
    msgs.yview(END)

#creat frame
frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

#creating text field
textF = Entry(main, font=("verdana",20))
textF.pack(fill=X, pady=10)
#button on field
btn = Button(main,text="Ask from bot",font=("verdana",20),command= ask_from_bot)
btn.pack()

#creat enter function
def enter_function(event):
    btn.invoke()

#going to bind main window when enter key..
main.bind('<Return>', enter_function)


main.mainloop()








