#janela
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter
 
#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("500x500")

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text = "Conversor de Moedas", font=("times", 28))
texto_moeda_origem = customtkinter.CTkLabel(janela, text = "Selecione a moeda de origem", font=("gotham", 17))
texto_moeda_destino = customtkinter.CTkLabel(janela, text = "Selecione a moeda de destino", font=("gotham", 17))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values = ["USD", "EUR", "BRL", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values = ["USD", "EUR", "BRL", "BTC"])

def converter_moeda():
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text = "Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dólar americano", "EUR: Euro", "BRL: Real Brasileiro", "BTC: Bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text = moeda)
    texto_moeda.pack()

#colocar os elementos criados na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=40, pady=0)
campo_moeda_origem.pack(padx=40, pady=10)
texto_moeda_destino.pack(padx=40, pady=0)
campo_moeda_destino.pack(padx=40, pady=10)
botao_converter.pack(padx=40, pady=10)
lista_moedas.pack(padx=0, pady=50)

#rodar a janela
janela.mainloop()




