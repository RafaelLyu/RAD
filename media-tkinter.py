from tkinter import *
Janela=Tk()
Janela.title('Media - Estacio')
Janela.geometry("235x318")
Janela.config(bg="#3b3b3b")

media_resultado = Frame(Janela,width=235,height=150 ,bg ="")
media_resultado.grid(row=1 , column= 0)

media_corpo = Frame(Janela,width=450,height=268)
media_corpo.grid(row=1 , column= 0)



## Funções

def calculo():
    EntryNome = nome.get()
    EntryMatricula = matricula.get()
    av1 = float(nota1.get())
    av2 = float(nota2.get())
    media = (av1 + av2) / 2
    if media >= 6:
        resultado = f"{EntryNome} Você foi aprovado !\n sua matricula é:{EntryMatricula}"
        Resultado.insert(END,str(resultado))
    elif media >=4:
        resultado = f" {EntryNome} Ficou De AV3 !! \n sua matricula  é: {EntryMatricula}"
        Resultado.insert(END,str(resultado))

    else:
        resultado = f"{EntryNome} Reprovado !!!\n sua matricula é: {EntryMatricula}"
        Resultado.insert(END,str(resultado))
                 
        

def limpar():
    nome.delete(0,END)
    matricula.delete(0,END)
    nota1.delete(0,END)   
    nota2.delete(0,END)
    Resultado.delete(0,END) 
    
##Criando Entrada de dados

##Nome
nomeLB = Label(media_corpo,text="Nome",fg ='black', font=('Ivy 10'))
nomeLB.place(x = 10, y = 10)

nome = Entry(media_corpo,text="Entre com seu nome" , bd = 1)
nome.place(x=70 , y = 10 )

##Matricula
matriculaLB = Label(media_corpo,text="Matricula",fg ='black', font=('Ivy 10'))
matriculaLB.place(x = 10 , y = 40)

matricula = Entry(media_corpo,text="Entre com sua Matricula" , bd = 1)
matricula.place(x = 70 , y = 40)

##Nota 1
nota1lb = Label(media_corpo,text="Sua AV1",fg ='black', font=('Ivy 10'))
nota1lb.place(x = 10 , y = 70)

nota1 = Entry(media_corpo,text="Sua AV1" , bd = 1 , width=5)
nota1.place(x = 70 , y = 70)

#Nota 2
nota2lb = Label(media_corpo,text="Sua AV2",fg ='black', font=('Ivy 10'))
nota2lb.place(x =110 , y = 70)

nota2 = Entry(media_corpo,text="Sua AV2" , bd = 1 , width=5)
nota2.place(x =175  , y = 70)


#Resultado
Resultado = Entry(media_corpo,text="", width=30 ,fg ='black', font=('Ivy 10'))
Resultado.place(x =10 , y = 100)


##Botoes
Calc = Button(media_corpo ,command=calculo,text="Calcular" , width=9 , height= 2, font=("Ivy 13 bold"),relief=RAISED, overrelief=RIDGE)
Calc.place(x=10 , y =150)

limparBTN = Button(media_corpo ,command=limpar, text="Limpar" , width=9 , height= 2, font=("Ivy 13 bold"),relief=RAISED, overrelief=RIDGE)
limparBTN.place(x = 130 , y =150)



Janela.mainloop()