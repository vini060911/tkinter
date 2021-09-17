from tkinter import *
from tkinter import messagebox as msg
import webbrowser as web

msg.showinfo("Robô", "Um robô (ou robot) é um dispositivo,[1] ou grupo de dispositivos, eletromecânicos capazes de realizar trabalhos de maneira autônoma ou pré-programada. Os robôs são comumente utilizados na realização de tarefas em locais mal iluminados, ou na realização de tarefas sujas ou perigosas para os seres humanos. Os robôs industriais utilizados nas linhas de produção são a forma mais comum de robôs, uma situação que está mudando recentemente com a popularização dos robôs comerciais limpadores de pisos e cortadores de gramas. Outras aplicações são: tratamento de lixo tóxico, exploração subaquática e espacial, cirurgias, mineração, busca e resgate, e localização de minas terrestres. Os robôs também aparecem nas áreas do entretenimento e tarefas caseiras.")
msg.showwarning("Fonte", "Acesse:\nhttps://pt.wikipedia.org/wiki/Robô")
bt = Button(text="Abrir site da origem da informação", command=lambda:[Fonte()])
bt.grid(row=0, column=0)

def Fonte():
    web.open("https://pt.wikipedia.org/wiki/Robô")
