from tkinter import *
from tkinter import messagebox
import json

word = { 
            "dc":"Ciência de dados (em inglês: data science) é uma área interdisciplinar,que localiza-se em uma interface entre a estatística e a ciência da computação e utiliza o método científico.",
            "db":"Os databases são verdadeiras bibliotecas digitais para os seus processos,onde é possível armazenar e acessar registros importantes, como dados de fornecedores, clientes, produtos, e muito mais.",
            "ia":"A Inteligência Artificial é um campo de estudo multidisciplinar que abrange varias áreas do conhecimento."
        }


app=Tk()
app.title("Challenge task")
app.geometry("720x510")

def mostrarMsg(value):
    messagebox.showinfo(title="Informações da palavra selecionada",
                        message=value)

def selection(vbtn, word):
    value_word = vbtn.get()
    for k,v in word.items():
        if(k == value_word):
            mostrarMsg(v)


vbtn = StringVar()

bl_words=Label(app, text="Selecione as palavras que deseja saber:")
bl_words.pack()

rd_dc = Radiobutton(app, text="Data Science", value="dc", variable=vbtn)
rd_dc.pack()

rd_db = Radiobutton(app, text="Data Base", value="db", variable=vbtn)
rd_db.pack()

rd_IA = Radiobutton(app, text="Inteligência Artificial", value="ia", variable=vbtn)
rd_IA.pack()

btn_selection = Button(app, text="Pesquisar", command=lambda:selection(vbtn, word))
btn_selection.pack()



app.mainloop()
