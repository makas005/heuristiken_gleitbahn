import tkinter as tk
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from Code.Eval import Eval
from Optimizer.IOptimizer import IOptimizer

def add_text_input(text, x1, y1, x2, y2):
    Label = tk.Label()
    Label.configure(text=text,
                    fg="white",
                    bg="black",
                    font="Arial 12")
    Label.place(x=x1, y=y1)

    outputvar = tk.StringVar(window)
    Input = tk.Entry()
    Input.configure(fg="black",
                    bg="white",
                    width=10,
                    font="Arial 12",
                    textvariable=outputvar)
    Input.place(x=x2, y=y2)
    return outputvar

def add_label(text, x, y, font_size):
    Label= tk.Label()
    Label.configure(text=text,
                    fg="white",
                    bg="black",
                    font="Arial "+font_size)
    Label.place(x=x, y=y)
    return Label

def add_dropdown(text,x1,y1,x2,y2):
    Label = tk.Label()
    Label.configure(text=text,
                    fg="white",
                    bg="black",
                    font="Arial 12")
    Label.place(x=x1, y=y1)

    dummy = ""
    outputvar = tk.StringVar(window)
    Dropdown = tk.OptionMenu(window, outputvar, dummy)
    #Get Algorithm names
    file_list=os.listdir("./Optimizer")
    
    Dropdown['menu'].delete(0, 'end')
    for i in range(len(file_list)):
        name = file_list[i]
        if(name!="__pycache__")and(name!="IOptimizer.py"):
            name = name[:name.rfind(".")]
            Dropdown['menu'].add_command(label=name, command=tk._setit(outputvar, name))

    Dropdown.configure(font="Arial 12")
    Dropdown.place(x=x2,y=y2)
    return outputvar

def add_button(text, x, y):
    Button = tk.Button()
    Button.configure(text=text,
                     bg="white",
                     fg="black",
                     font="Arial 14 bold",
                     activebackground="#FF0000",
                     command=Start)
    Button.place(x=x,y=y)

def add_text_output(label, x1, y1, x2, y2, width, height):
    Label = tk.Label()
    Label.configure(text=label,
                    fg="white",
                    bg="black",
                    font="Arial 12")
    Label.place(x=x1, y=y1)

    Output = tk.Text()
    Output.configure(fg="black",
                    bg="white",
                    width=width,
                    height=height,
                    font="Arial 12",
                    state="disabled")
    Output.place(x=x2, y=y2)
    return Output

def Start():
    #check inputs
    all_good = True
    try:
        h = float(HInput.get())
        l = float(LInput.get())
        n = int(NInput.get())
        a = AInput.get()
        if((h<=0)or(l<=0)or(n<0)or(a=="")):
            all_good = False
    except(ValueError):
        all_good=False

    if(all_good):
        eval = Eval(h, l/(n+1))
        if(n>0):
            opt = IOptimizer(n, -h, h,eval.evaluate, a)
            node_arr = opt.Optimize()
        else:
            node_arr = []
        t = eval.evaluate(node_arr)
        node_str = '\n'.join(map(str, node_arr))
        #Output
        TOutput.configure(state="normal")
        TOutput.delete('1.0',tk.END)
        TOutput.insert(tk.END,t)
        TOutput.configure(state="disabled")
        HOutput.configure(state="normal")
        HOutput.delete('1.0',tk.END)
        HOutput.insert(tk.END,node_str)
        HOutput.configure(state="disabled")

        node_arr.insert(0,h)
        node_arr.append(0)
        y=node_arr
        x=[0]
        for i in range(1,len(node_arr)):
            x.append((l/(n+1))*i)

        figure = plt.Figure(figsize=(6, 4.5), dpi=100)
        ax=figure.add_subplot(111)
        bar = FigureCanvasTkAgg(figure, window)
        bar.get_tk_widget().place(x=435, y=50)
        ax.plot(x,y)
        ax.grid("-")
    else:
        #Error
        TOutput.configure(state="normal")
        TOutput.delete('1.0',tk.END)
        TOutput.insert(tk.END,"-1")
        TOutput.configure(state="disabled")
        HOutput.configure(state="normal")
        HOutput.delete('1.0',tk.END)
        HOutput.insert(tk.END,"")
        HOutput.configure(state="disabled")

##Setup Window
window = tk.Tk()
window.title("Berechnung der optimalen Gleitbahn")
window.geometry("1056x594")
window.configure(bg="black")
titel = add_label("Berechnung der optimalen Gleitbahn", 5, 5, "20") #Setup Titel

##Setup Inputs
x1 = 10
x2 = 200
inputTitel = add_label("Eingabewerte:", 5, 50, "16")    #Titel
HInput = add_text_input("Höhe:", x1, 80, x2, 80)       #Höhe
LInput = add_text_input("Länge:", x1, 105, x2, 105)    #Länge
NInput = add_text_input("Anzahl der Stützstellen:", x1, 130, x2, 130)  #Anzahl der Stützstellen
AInput = add_dropdown("Auswahl des Alogithmus:",x1,155,x2,155)#Algorithmus

##Setup Start Button
StartButton = add_button("START", 960, 540)

##Setup Outputs
#Graph
dummy_data = {'x': [0],
            'y': [0]}
df = pd.DataFrame(dummy_data)
figure = plt.Figure(figsize=(6, 4.5), dpi=100)
ax=figure.add_subplot(111)
bar = FigureCanvasTkAgg(figure, window)
bar.get_tk_widget().place(x=435, y=50)

#Text
outputTitel = add_label("Ausgabewerte:", 5, 200, "16")    #Titel
TOutput = add_text_output("Benötigte Zeit =", x1 , 230, x2, 230, 10, 1) #Zeit Output
HOutput = add_text_output("Höhenvektor = ", x1, 255, 120, 255, 30, 18)

window.mainloop()