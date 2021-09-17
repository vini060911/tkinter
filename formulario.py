import tkinter as tk
from tkinter import messagebox

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry('200x100')
       self.root.title("Formulário")
       self.root["background"] = "#cc00ff"
       
       self.Nome = tk.Label(self.root, text="Digite o seu nome:")
       self.Nome.pack()
       self.Nome["background"] = "#cc00ff"
       
       self.NomeTXT = tk.Entry()
       self.NomeTXT.pack()

       self.Idade = tk.Label(self.root, text="Digite a sua idade:")
       self.Idade.pack()
       self.Idade["background"] = "#cc00ff"
       
       self.IdadeTXT = tk.Entry()
       self.IdadeTXT.pack()

       self.Pais = tk.Label(self.root, text="Digite o país onde você mora:")
       self.Pais.pack()
       self.Pais["background"] = "#cc00ff"
       
       self.PaisTXT = tk.Entry()
       self.PaisTXT.pack()

       self.Regiao = tk.Label(self.root, text="Digite a região do\nlugar onde você mora:")
       self.Regiao.pack()
       self.Regiao["background"] = "#cc00ff"
       
       self.RegiaoTXT = tk.Entry()
       self.RegiaoTXT.pack()

       self.Estado = tk.Label(self.root, text="Digite o estado onde você mora:")
       self.Estado.pack()
       self.Estado["background"] = "#cc00ff"
       
       self.EstadoTXT = tk.Entry()
       self.EstadoTXT.pack()

       self.Cidade = tk.Label(self.root, text="Digite a cidade onde você mora:")
       self.Cidade.pack()
       self.Cidade["background"] = "#cc00ff"
       
       self.CidadeTXT = tk.Entry()
       self.CidadeTXT.pack()

       self.Bairro = tk.Label(self.root, text="Digite o bairro onde você mora:")
       self.Bairro.pack()
       self.Bairro["background"] = "#cc00ff"
       
       self.BairroTXT = tk.Entry()
       self.BairroTXT.pack()
       
       self.bt = tk.Button(self.root, text = 'Enviar', command=lambda:[self.Enviar()])
       self.bt.pack()
       self.bt["background"] = "#00ff00"

       self.L1 = tk.Label(self.root, text="")
       self.L1.pack()
       self.L1["background"] = "#cc00ff"
       
       self.labelA = tk.Label(self.root, text="")
       self.labelA.pack()
       self.labelA["background"] = "#cc00ff"

       self.labelB = tk.Label(self.root, text="")
       self.labelB.pack()
       self.labelB["background"] = "#cc00ff"

       self.labelC = tk.Label(self.root, text="")
       self.labelC.pack()
       self.labelC["background"] = "#cc00ff"

       self.labelD = tk.Label(self.root, text="")
       self.labelD.pack()
       self.labelD["background"] = "#cc00ff"

       self.labelE = tk.Label(self.root, text="")
       self.labelE.pack()
       self.labelE["background"] = "#cc00ff"

       self.labelF = tk.Label(self.root, text="")
       self.labelF.pack()
       self.labelF["background"] = "#cc00ff"

       self.labelG = tk.Label(self.root, text="")
       self.labelG.pack()
       self.labelG["background"] = "#cc00ff"
       
       self.root.mainloop()

   def Enviar(self):
       self.L1["text"] = "Dados recebidos:"
       self.labelA["text"] = "Nome: " + self.NomeTXT.get()
       self.labelB["text"] = "Idade: " + self.IdadeTXT.get()
       self.labelC["text"] = "País: " + self.PaisTXT.get()
       self.labelD["text"] = "Região: " + self.RegiaoTXT.get()
       self.labelE["text"] = "Estado: " + self.EstadoTXT.get()
       self.labelF["text"] = "Cidade: " + self.CidadeTXT.get()
       self.labelG["text"] = "Bairro: " + self.BairroTXT.get()
       messagebox.showinfo(
                           'Dados recebidos',
                           'Nome: '+self.NomeTXT.get()
                           +"\nIdade: "+self.IdadeTXT.get()
                           +"\nPaís: "+self.PaisTXT.get()
                           +"\nRegião: "+self.RegiaoTXT.get()
                           +"\nEstado: "+self.EstadoTXT.get()
                           +"\nCidade: "+self.CidadeTXT.get()
                           +"\nBairro: "+self.BairroTXT.get()
       )
       
app = Test()
