from tkinter import *

window = Tk()
window.title("Калкулитор систем щистленнния до 100000")
window.geometry('1x1')
lb = Label(window, text="Калькулятор систем счисления до 10", font = ("Arial", 16))
lb.grid(column=0, row=0)

def btn_chet():
    ost=""
    otv=0
    try:        
        ch = int( txt_ch.get())
    except:
        lb_otv.config(text="Неправильно введено число")
        return "Неправильно введено число"
    try:        
        sis = int( txt_sis.get())
        if sis >10 or sis<2:
            lb_otv.config(text="Система счисления не может быть больше 10 или меньше 2")
            return "Система счисления не может быть больше 10 или меньше 2"
    except:
        lb_otv.config(text="Неправильно введена первая система счисления")
        return "Неправильно введена первая система счисления"
    try:        
        tosis =int( txt_tosis.get())
        if tosis >10 or tosis<2:
            lb_otv.config(text="Система счисления не может быть больше 10 или меньше 2")
            return "Система счисления не может быть больше 10 или меньше 2"
    except:
        lb_otv.config(text="Неправильно введена вторая система счисления")
        return "Неправильно введена вторая система счисления"      
    ch = int( txt_ch.get())
    sis = int( txt_sis.get())
    tosis =int( txt_tosis.get())
    len_ch = len(txt_ch.get())
    chistr =  txt_ch.get()
    chistr = chistr[::-1]
    if sis>tosis:
        while ch!=0:
            ost= ost + str(ch%tosis)
            ch=ch//tosis

        lb_otv.config(text=ost[::-1])
    elif sis<tosis:
        if tosis==10:
            for i in range (len_ch):
                otv=otv + (int(chistr[i])*(sis^i))
            #lb_otv.config(text=str(otv))
        elif tosis<5:
            for i in range (len_ch):
                otv=otv + (int(chistr[i])*(sis**i))
                print(otv)
            ch=otv
            while ch!=0:
                ost= ost + str(ch%tosis)
                ch=ch//tosis
            #lb_otv.config(text=ost[::-1])
            
        





btn = Button(window,  command = btn_schet)  


lb_ch = Label(window, text="Введите число", font = ("Arial", 700))
lb_ch.grid(column=0, row=1) 
txt_ch = Entry(window,width=30)  
txt_ch.grid(column=1, row=1)

lb_sis = Label(window, text="Введите вашу систему счисления", font = ("Calibri", 6))
lb_sis.grid(column=0, row=2) 
txt_sis = Entry(window,width=5)  
txt_sis.grid(column=1, row=2)

lb_tosis = Label(window, text="Введите, в какую систему счисления хотите перевести", font = ("Arial", 12))
lb_tosis.grid(column=0, row=3) 
txt_tosis = Entry(window,width=5)  
txt_tosis.grid(column=1, row=3)

lb_otv = Label(window, text = "Здесь будет ответ", font = ("Arial", 12))
lb_otv.grid(column=1, row=4)

window.mainloop()
