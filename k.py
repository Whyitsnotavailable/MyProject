import tkinter
from tkinter import * 

logs = tkinter.Tk()
logs.title('kalkulators')
logs.geometry('500x500+600+100') #размер и расположение окна

def input_info_entry(symbol):
    entry.insert(END, symbol)

def clear():
    entry.delete(0, END)

def result():
    text = entry.get()
    result=0
    try:
        if '+' in text:
            splitted_text = text.split('+')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first + second
        elif '-' in text:
            splitted_text = text.split('-')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first - second
        elif '*' in text:
            splitted_text = text.split('*')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first * second
        elif '/' in text:
            splitted_text = text.split('/')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            if second == 0: 
                raise ZeroDivisionError('Dalisana ar 0 nav atlauta')
            result = first / second
        clear()
        entry.insert(0, result)

    except ZeroDivisionError:
        clear()
        entry.insert(0, 'Error(0)')
    except Exception as e:
        clear()




entry = Entry(logs, width=15, font=('', 20))
entry.place(x = 125, y = 50)

btnC = Button(logs, bg= 'purple', fg='white', font=('', 20), text='C', command=clear)
btnC.place(x = 125, y =100, width=50, height=50)

btn2 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='/', command= lambda: input_info_entry('/'))
btn2.place(x = 185, y =100, width=50, height=50)

btn3 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='*', command= lambda: input_info_entry('*'))
btn3.place(x = 245, y =100, width=50, height=50)

btn_sum = Button(logs, bg= 'purple', fg='white', font=('', 20), text='-', command= lambda: input_info_entry('-'))
btn_sum.place(x = 305, y =100, width=50, height=50)

btn4 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='7', command= lambda: input_info_entry('7'))
btn4.place(x = 125, y =160, width=50, height=50)

btn5 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='8', command= lambda: input_info_entry('8'))
btn5.place(x = 185, y =160, width=50, height=50)

btn6 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='9', command= lambda: input_info_entry('9'))
btn6.place(x = 245, y =160, width=50, height=50)

btn_min = Button(logs, bg= 'purple', fg='white', font=('', 20), text='+', command= lambda: input_info_entry('+'))
btn_min.place(x = 305, y =160, width=50, height=50)

btn7 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='4', command= lambda: input_info_entry('4'))
btn7.place(x = 125, y =220, width=50, height=50)

btn8 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='5', command= lambda: input_info_entry('5'))
btn8.place(x = 185, y =220, width=50, height=50)

btn9 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='6', command= lambda: input_info_entry('6'))
btn9.place(x = 245, y =220, width=50, height=50)

btn13 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='.', command= lambda: input_info_entry('.'))
btn13.place(x = 305, y =220, width=50, height=50)

btn10 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='1', command= lambda: input_info_entry('1'))
btn10.place(x = 125, y =280, width=50, height=50)

btn11 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='2', command= lambda: input_info_entry('2'))
btn11.place(x = 185, y =280, width=50, height=50)

btn_dal = Button(logs, bg= 'purple', fg='white', font=('', 20), text='3', command= lambda: input_info_entry('3'))
btn_dal.place(x = 245, y =280, width=50, height=50)

btnRavno = Button(logs, bg= 'purple', fg='white', font=('', 20), text='=', command=result)
btnRavno.place(x = 305, y =280, width=50, height=110)

btn12 = Button(logs, bg= 'purple', fg='white', font=('', 20), text='0', command= lambda: input_info_entry('0'))
btn12.place(x = 125, y =340, width=170, height=50)



logs.mainloop()