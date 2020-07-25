from tkinter import *

'''
Vamos entender o código: primeiro importamos todos os componentes do módulo Tkinter. Logo após, criamos uma classe chamada Application, que no momento ainda não possui nenhuma informação. 
É nela que criaremos os controles que serão exibidos na tela.

Depois instanciamos a classe TK() através da variável root, que foi criada no final do código. Essa classe permite que os widgets possam ser utilizados na aplicação.

Em Application(root) passamos a variável root como parâmetro do método construtor da classe Application. E para finaliza
'''
class Application:
    def __init__(self, master=None):
        pass
root = Tk()
Application(root)
root.mainloop()

'''Veja na linha 4 do código que criamos o primeiro container chamado widget1 e passamos como referência o container pai.

O frame master é o nosso top level, que é o elemento máximo da hierarquia, ou seja, é a nossa janela de aplicação, que contém o título, e botões de maximizar, minimizar e fechar.

Na linha 5 informamos o gerenciador de geometria pack e usamos um widget label para imprimir na tela as palavras "Primeiro widget" e informamos que o container pai é o widget1, que foi passado como parâmetro, conforme a linha
'''
class Application:
	def __init__(self, master=None):
		self.widget1 = Frame(master) #esta na maior hierarquia
		self.widget1.pack() #responsavel por ajustar o tamanho da interface
		self.msg = Label(self.widget1, text="Primeiro widget") #exibe como um titulo, desde que é o container pai
		self.msg.pack () #responsavel por exibir a mensagem
root = Tk() #pre definido pelo pacote tkinter
Application(root)
root.mainloop()

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master) #define como container pai
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget") #salva o texto que sera exibido
        self.msg["font"] = ("Verdana", "10", "italic", "bold") #define a fonte, o tamanho e estilo de letra
        self.msg.pack ()
        self.sair = Button(self.widget1) #cria um botao no corpo do container pai
        self.sair["text"] = "Sair" #define o texto
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit #command assume o valor de sair 
        self.sair.pack ()
  
root = Tk()
Application(root)
root.mainloop()

  
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT) #define a posicao do texto
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT) #define a posição
root = Tk()
Application(root)
root.mainloop()

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto) #ao receber o clique pelo comando .bind o subprograma mudarTexto é chamado e analisa o que esta escrito, e com isso altera a cada clique
        self.sair.pack ()
  
    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget": #verifica se o texto é esse, caso sim altera os textos
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
  
  
root = Tk()
Application(root)
root.mainloop()
#outra maneira de mudar o texto
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair["command"] = self.mudarTexto #o comando é recebido aqui e chama o mudarTexto
        self.sair.pack ()
  
    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
  
  
  
root = Tk()
Application(root)
root.mainloop()