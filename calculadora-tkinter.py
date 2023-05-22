from tkinter import *

Janela=Tk()
Janela.title('Calculadora')
Janela.geometry("235x318")
Janela.config(bg="#3b3b3b")

tela_resultado = Frame(Janela,width=235,height=60 ,bg ="")
tela_resultado.grid(row=0 , column= 0)

tela_corpo = Frame(Janela,width=235,height=268)
tela_corpo.grid(row=1 , column= 0)

#
valor_texto = StringVar()
valores = ""

#criando label

app_label = Label(tela_resultado, textvariable=valor_texto,width=16, height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 18 '),bg="#0ec4ba",fg="#FFFFFF")
app_label.place(x=0 , y=0)


#Funções

def entrada_valores(evento):
    global valores
    valores = valores +  str(evento)
  
    #passando valor para tela
    valor_texto.set(valores)

#Calcular
def calcular():
    global valores
    resultado = eval(valores)
    valor_texto.set(resultado)

#Limpa tela
def limpa_tela():
    global valores
    valores = " "
    valor_texto.set("")

# Criando os botoes

#Primeira Row
btn_c = Button(tela_corpo,command= limpa_tela,text="C", width= 11, height=2 , font=("Ivy 13 bold"),relief=RAISED, overrelief=RIDGE) ##
btn_c.place(x = 0 , y = 0)

btn_modulo = Button(tela_corpo,command= lambda: entrada_valores("%"),text="%", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_modulo.place(x = 118 , y = 0)

btn_div = Button(tela_corpo,command= lambda: entrada_valores("/"),text="/", width= 5, height=2, bg= "#ffa500" , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_div.place(x = 177 , y = 0)

#Segunda Row

btn_7 = Button(tela_corpo,command= lambda: entrada_valores("7"),text="7", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_7.place(x = 0 , y = 52)

btn_8 = Button(tela_corpo,command= lambda: entrada_valores("8"),text="8", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_8.place(x = 59 , y = 52)

btn_9 = Button(tela_corpo,command= lambda: entrada_valores("9"),text="9", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_9.place(x = 118 , y = 52)

btn_mul = Button(tela_corpo,command= lambda: entrada_valores("*"),text="*", width= 5, height=2, bg= "#ffa500" , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_mul.place(x = 177 , y = 52)

#Terceira row

btn_4 = Button(tela_corpo,command= lambda: entrada_valores("4"),text="4", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_4.place(x = 0 , y = 104)

btn_5 = Button(tela_corpo,command= lambda: entrada_valores("5"),text="5", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_5.place(x = 59 , y = 104)

btn_6 = Button(tela_corpo,command= lambda: entrada_valores("6"),text="6", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_6.place(x = 118 , y = 104)

btn_sub = Button(tela_corpo,command= lambda: entrada_valores("-"),text="-", width= 5, height=2, bg= "#ffa500" , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_sub.place(x = 177 , y = 104)

#Quarta row

btn_3 = Button(tela_corpo,command= lambda: entrada_valores("1"),text="1", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_3.place(x = 0 , y = 156)

btn_2 = Button(tela_corpo,command= lambda: entrada_valores("2"),text="2", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_2.place(x = 59 , y = 156)

btn_1 = Button(tela_corpo,command= lambda: entrada_valores("3"),text="3", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_1.place(x = 118 , y = 156)

btn_add = Button(tela_corpo,command= lambda: entrada_valores("+"),text="+", width= 5, height=2, bg= "#ffa500" , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_add.place(x = 177 , y = 156)

#Quinta row
btn_0 = Button(tela_corpo,command= lambda: entrada_valores("0"),text="0", width= 11, height=2 , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE) ##
btn_0.place(x = 0 , y = 208)
btn_1 = Button(tela_corpo,command= lambda: entrada_valores("."),text=".", width= 5, height=2  , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_1.place(x = 118 , y = 208)
btn_equal = Button(tela_corpo,text="=",command= calcular, width= 5, height=2, bg= "#ffa500" , font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
btn_equal.place(x = 177 , y = 208)

Janela.mainloop()