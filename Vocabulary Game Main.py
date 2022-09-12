from tkinter import *
from PIL import ImageTk,Image
import pygame

root = Tk()
root.title("English Word Quiz")
##Sound
pygame.mixer.init()
pygame.mixer.music.load("Sneaky-Snitch.mp3")
pygame.mixer.music.play(loops=10)

#opening sample txt file and creating new dictionary
f=open("sample.txt","r")
data=f.readlines()
word_Count=len(data)
#Creating new words list and answer list
words_list=[]
answer_list=[]
for line in data:
    every_word=''
    for letter in line:
        if(letter==' '):
            break
        every_word=every_word+letter
    words_list.append(every_word)
for line in data:
    every_word=''
    for letter in line[::-1]:
        if(letter==' '):
            break
        every_word=every_word+letter
    answer_list.append(every_word[::-1])
    
#This dictionary collects words and answers
my_dict=dict(zip(words_list,answer_list))

#Screen details
app_width=1200
app_height=800
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.configure(bg="#ab9cf7")

#Creating user's answer list which we can store any answer
user_answer_list=["None"]*(word_Count+1)
number=0

#Welcome Page                
label_word=Label(root,bg="#ab9cf7",text="WELCOME TO THE ENGLISH WORD QUIZ GAME",font=("Helvetica",32,"bold"))

#Answer's checkbuttons
checkbutton_list = []

#Creating forward Button
def forward(word_number):
    global label_word
    global next_btn
    global back_btn
    global my_button1
    global return_main_btn
    global user_answer_list
    global number
    number=word_number
    #forgetting 1 st page widgets
    label_word.place_forget()
    my_button1.place_forget()
    next_btn.place_forget()
    back_btn.place_forget()
    
    return_menu_btn.place(relx=0,rely=0)
    label_word=Label(root,bg="#ab9cf7",text=words_list[word_number],font=("Helvetica",34,"bold"))
    next_btn=Button(root,text="NEXT",font=('Bold',20),bg='#1877f2',fg='white',width=12,command=lambda: forward(word_number+1))
    back_btn=Button(root,text="BACK",font=('Bold',20),bg='#1877f2',fg='white',width=12,command=lambda: backward(word_number-1))
    if word_number==word_Count-1:
        next_btn=Button(root,text="NEXT",font=('Bold',20),bg='#1877f2',fg='white',width=12,state=DISABLED)    
    label_word.place(relx=0.5,rely=0.45,anchor=CENTER)    
    next_btn.place(relx=0.5,rely=0.94)
    back_btn.place(relx=0.3,rely=0.94)
    Input.place(relx=0.5,rely=0.55,anchor=CENTER)
    finish_btn.place(relx=0.805,rely=0)
    user_answer_list[word_number]=Input.get()
    Input.delete(0,END)

#Creating backword button
def backward(word_number):
    global label_word
    global next_btn
    global back_btn
    global return_main_btn
    global number
    number=word_number
    #forgetting last widgets
    label_word.place_forget()
    next_btn.place_forget()
    back_btn.place_forget()
    Input.place_forget()
    return_menu_btn.place(relx=0,rely=0)
    label_word=Label(root,bg="#ab9cf7",text=words_list[word_number],font=("Helvetica",34,"bold"))
    next_btn=Button(root,text="NEXT",font=('Bold',20),bg='#1877f2',fg='white',width=12,command=lambda: forward(word_number+1))
    back_btn=Button(root,text="BACK",font=('Bold',20),bg='#1877f2',fg='white',width=12,command=lambda: backward(word_number-1))
    if word_number==0:
        back_btn=Button(root,text="BACK",font=('Bold',20),bg='#1877f2',fg='white',width=12,state=DISABLED)    
    label_word.place(relx=0.5,rely=0.45,anchor=CENTER)    
    next_btn.place(relx=0.5,rely=0.94)
    back_btn.place(relx=0.3,rely=0.94)
    Input.place(relx=0.5,rely=0.55,anchor=CENTER)
    finish_btn.place(relx=0.805,rely=0)
    user_answer_list[word_number]=Input.get()
    Input.delete(0,END)
    
#Returning main menu page
def return_main_menu():
    global label_word
    global next_btn
    global back_btn
    global Input
    global result_btn
    result_btn.place_forget()
    back_btn.place_forget()
    next_btn.place_forget()
    return_menu_btn.place_forget()
    label_word.destroy()
    Input.place_forget()
    finish_btn.place_forget()
    back_btn=Button(root,text="BACK",font=('Bold',20),bg='#1877f2',fg='white',width=12,state=DISABLED)
    label_word=Label(root,bg="#ab9cf7",text="WELCOME TO THE ENGLISH WORD QUIZ GAME",font=("Helvetica",32,"bold"))
    label_word.place(relx=0.5, rely=0.4,anchor=CENTER)
    my_button1.place(relx=0.5, rely=0.5,anchor=CENTER)
    for x in range(word_Count):
        checkbutton_list[x].destroy()
    checkbutton_list.clear()

var=[]
#Last page
def result_page():
    global label_word
    global next_btn
    global back_btn
    global Input
    global correct_button
    global label_word
    global result_btn
    finish_btn.place_forget()
    back_btn.place_forget()
    next_btn.place_forget()
    result_btn.place_forget()
    # return_menu_btn.place_forget()
    label_word.place_forget()
    Input.place_forget()
    result_btn.pack_forget()
    result=0
    for x in range(word_Count):
        if var[x].get()==1:
            result=result+1
    label_word=Label(root,bg="#ab9cf7",text=f"YOUR RESULT {result/5*100}",font=("Helvetica",32,"bold"))
    label_word.pack(side=TOP,expand=YES)
    for x in range(word_Count):
        checkbutton_list[x].destroy()
    checkbutton_list.clear()
    var.clear()

#Creating finish button    
def finish_page():
    global label_word
    global next_btn
    global back_btn
    global Input
    global correct_button
    global result_btn
    finish_btn.place_forget()
    back_btn.place_forget()
    next_btn.place_forget()
    # return_menu_btn.place_forget()
    label_word.place_forget()
    Input.place_forget()
    user_answer_list[number+1]=Input.get()
    Input.delete(0,END)
    
    for x in range(word_Count):
        temp=IntVar()
        correct_button=Checkbutton(root,font=('Bold',18),bg="#ab9cf7",text=words_list[x]+"   "+my_dict[words_list[x]]+" Your answer=  "+user_answer_list[x+1],variable=temp)
        correct_button.pack(side=TOP,expand=YES)
        checkbutton_list.append(correct_button)
        var.append(temp)
    result_btn=Button(root,font=('Bold',20),bg='red',fg='black',text="Result",width=12,command=result_page)
    result_btn.place(relx=0.805,rely=0)
    # finish_btn.place(relx=0.5,rely=0.5)

#pages 
Input=Entry(root,width=30,borderwidth=5,font=("Arial",28,"bold"))
back_btn=Button(root,text="BACK",font=('Bold',20),bg='#1877f2',fg='white',width=12,state=DISABLED)
next_btn=Button(root,text="NEXT",font=('Bold',20),bg='#1877f2',fg='white',width=12,command= lambda: forward(1))
# next_btn.bind('<Return>',forward(1))
return_menu_btn=Button(root,text="MENU",font=('Bold',20),bg='#1877f2',fg='white',width=12,command=return_main_menu)
finish_btn=Button(root,text="FINISH",font=('Bold',20),bg='#1877f2',fg='white',width=12,command=finish_page)
correct_button=Checkbutton(root,text="CHeck this box",variable=var,onvalue=1,offvalue=0)
result_btn=Button(root,font=('Bold',20),bg='red',fg='black',text="Result",width=12,command=result_page)

    
#Game's 1st Page 

my_button1=Button(root,text="START",padx=250,pady=15,bg="#f7ff59",activebackground="yellow",command=lambda: forward(0))
label_word.place(relx=0.5, rely=0.4,anchor=CENTER)
my_button1.place(relx=0.5, rely=0.5,anchor=CENTER)


root.mainloop()
