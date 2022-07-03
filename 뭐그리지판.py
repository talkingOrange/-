
from tkinter import *
from tkinter.colorchooser import*   #컬러색 표를 보여주며 컬러를 띄어준다.
from tkinter.simpledialog import* #질문창을 띄울 때 필요하다.(새 창을 띄우는 방법)
from PIL import ImageGrab
import random



#색을 바꾸는 함수
def getColor():
    global myColor
    color = askcolor()
    myColor = color[1]


#선 두께
def getWidth():
    global penWidth
    penWidth = askinteger("펜 굵기","펜 굵기 1~20을 입력하세요.", minvalue = 1, maxvalue = 20)

def paint(event):
    global x1, y1, x2, y2, penWidth, myColor
    x1, y1 = ( event.x-1 ), ( event.y+1 )
    x2, y2 = ( event.x-1 ), ( event.y+1 )
    canvas.create_oval( x1, y1, x2, y2,  width = penWidth, fill = myColor, outline = myColor)

def change_color0():
    global myColor
    myColor="black"

def change_color1():
    global myColor
    myColor="red"

def change_color2():
    global myColor
    myColor="blue"

def change_color3():
    global myColor
    myColor="white"



#전역변수#    
myColor = 'black'
penWidth= 3
x1, y1, x2, y2 = None, None, None, None


def save():
  if messagebox.askokcancel("Save", "저장하시겠습니까?"):
    a= window.winfo_rootx()
    b=window.winfo_rooty()
    c= window.winfo_width()+a
    d=window.winfo_height()+b

    windowsize = [a,b,c,d]
    img=ImageGrab.grab(windowsize)
    file = "capture.png"
    img.save(file)
    messagebox.showinfo("Information", "capture.png로 저장되었습니다. ")

def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()


window = Tk()
window.title("뭐 그리지판")
window.geometry("1000x1200")


menu = Menu(window)
window.config(menu=menu)
filemenu =Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="저장", command=save)
filemenu.add_command(label="종료", command=exit)



#####따라 그릴 그림(참고할 그림)########




p1=PhotoImage(file="파일//스폰지밥.png")
p2=PhotoImage(file="파일//피카츄.png")
p3=PhotoImage(file="파일//호빵맨.png")
p4=PhotoImage(file="파일//둘리.png")
p5=PhotoImage(file="파일//루피.png")
p6=PhotoImage(file="파일//뽀로로.png")
p7=PhotoImage(file="파일//뿌까.png")
p8=PhotoImage(file="파일//액션토끼.png")
p9=PhotoImage(file="파일//짱구.png")
p10=PhotoImage(file="파일//펭수.png")

imgcollection = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]


def imgchoice():
 for i in range(1):
    computer_choice = random.choice(imgcollection)
    if computer_choice == p1:
        labelImage.configure(image=p1)
    elif computer_choice == p2:
        labelImage.configure(image=p2)
    elif computer_choice == p3:
        labelImage.configure(image=p3)
    elif computer_choice == p4:
        labelImage.configure(image=p4)
    elif computer_choice == p5:
        labelImage.configure(image=p5)
    elif computer_choice == p6:
        labelImage.configure(image=p6)
    elif computer_choice == p7:
        labelImage.configure(image=p7)
    elif computer_choice == p8:
        labelImage.configure(image=p8)
    elif computer_choice == p9:
        labelImage.configure(image=p9)
    else:
        labelImage.configure(image=p10)



buttonok=Button(window, text="random",command=imgchoice)


labelImage=Label(window,width=1000,height=280,image=None, bg="white")


buttonok.pack()
labelImage.pack()



####그림판#####



canvas = Canvas(window,width=1000,height=1000,bg="white")
canvas.pack()
canvas.bind("<B1-Motion>", paint)
button0 = Button(window, text="펜 색상", command=getColor)
button1 = Button(window, text="검정색", command=change_color0)
button2= Button(window, text="빨간색", command=change_color1)
button3 = Button(window, text="파란색", command=change_color2)
button4 = Button(window, text="펜 굵기", command=getWidth)
button5 = Button(window, text="지우개", command=change_color3)

button0.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button4.pack()

button0.place(x=650, y=900)
button1.place(x=750, y=900)
button2.place(x=800, y=900)
button3.place(x=850, y=900)
button4.place(x=550, y=900)
button5.place(x=920, y=900)


window.mainloop()
