import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from random import shuffle
import os


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.title("NatureQuizz")
        self.configure(bg="#4caf50")

        self.tela_inicial = tk.Frame(self, bg="#4caf50")
        self.tela_inicial.pack(expand=True)
        
        self.label_titulo = tk.Label(self.tela_inicial, text="Bem-vindo ao NatureQuiz!", font=("Arial", 24), bg="#4caf50", fg="#333333")
        self.label_titulo.pack(pady=10)

        #self.imagem_pil = Image.open("C:/Users/João Pedro/Downloads/logo/logo.png")
        #self.imagem_tk = ImageTk.PhotoImage(self.imagem_pil)
        #self.label_imagem = tk.Label(self.tela_inicial, image=self.imagem_tk)
        #self.label_imagem.pack(pady=50)

        self.botao_iniciar = tk.Button(self.tela_inicial, text="Iniciar Quiz", font=("Arial", 24), bg="#81c784", fg="#ffffff", activebackground="#4caf50", activeforeground="#ffffff", command=self.iniciar_quiz)
        self.botao_iniciar.pack(pady=10)

        self.update_idletasks()

    def iniciar_quiz(self):
        self.tela_inicial.pack_forget()
        self.botao_iniciar.pack_forget()

        self.perguntas =  [
            {
                "pergunta": "Qual é o principal gás responsável pelo aquecimento global?",
                "opcoes": [
                    "Dióxido de carbono (CO2)",
                    "Metano (CH4)",
                    "Óxido nitroso (N2O)",
                    "Monóxido de carbono (CO)"
                ],
                "resposta": "Dióxido de carbono (CO2)",
                "dica": "Esse gás é liberado principalmente pela queima de combustíveis fósseis.",
                "dica_eliminar_opcoes_usada": False,
                "dica_adicional_usada": False
            },
            {
                "pergunta": "Qual é a maior fonte de poluição dos oceanos?",
                "opcoes": [
                    "Plástico",
                    "Petróleo",
                    "Metais pesados",
                    "Produtos químicos industriais"
                ],
                "resposta": "Plástico",
                "dica": "É um material muito utilizado na fabricação de embalagens e objetos descartáveis.",
                "dica_eliminar_opcoes_usada": False,
                "dica_adicional_usada": False
            },
            {
                "pergunta": "O que significa a sigla 'CO2'?",
                "opcoes": [
                    "Carcinogênico de oxigênio",
                    "Carbono",
                    "Dióxido de carbono",
                    "Composto oxigenado",
                ],
                "resposta": "Dióxido de carbono",
                "dica": "Essa sigla representa a combinação de dois elementos químicos.",
                "dica_eliminar_opcoes_usada": False,
                "dica_adicional_usada": False
            },
            {
                "pergunta": "Qual é a importância das florestas para o meio ambiente?",
                "opcoes": [
                "Produção de oxigênio",
                "Fornecimento de alimentos",
                "Absorção de poluentes",
                "Regulação do clima"
                ],
                "resposta": "Produção de oxigênio",
                "dica": "Esse fenômeno está relacionado à retenção de calor na atmosfera.",
                "dica_eliminar_opcoes_usada": False,
                "dica_adicional_usada": False
            },
            {
    "pergunta": "O que é o efeito estufa?",
    "opcoes": [
        "Aumento da temperatura global causado por gases poluentes",
        "Aumento da temperatura local causado pelo desmatamento",
        "Diminuição da temperatura global causada pela poluição",
        "Diminuição da temperatura local causada pela urbanização"
    ],
    "resposta": "Aumento da temperatura global causado por gases poluentes",
    "dica": "Esse fenômeno está relacionado à retenção de calor na atmosfera.",
    "dica_eliminar_opcoes_usada": False,
    "dica_adicional_usada": False
},
            {   
                "pergunta": "Qual é a principal causa da perda de biodiversidade?",
                "opcoes": [
                    "Desmatamento",
                    "Poluição do ar",
                    "Mudanças climáticas",
                    "Caça excessiva",
                ],
                "resposta": "Desmatamento",
                "dica": "Consiste na remoção ou destruição de florestas.",
                "dica_eliminar_opcoes_usada": False,
                "dica_adicional_usada": False
            },
            {
                "pergunta": "O que é energia renovável?",
                "opcoes": [
                    "Energia obtida a partir de fontes inesgotáveis",
                    "Energia gerada a partir de combustíveis fósseis",
                    "Energia produzida a partir de resíduos nucleares",
                    "Energia proveniente da queima de biomassa",
                ],
                "resposta": "Energia obtida a partir de fontes inesgotáveis",
                "dica": "São fontes de energia que não se esgotam ou se regeneram naturalmente.",
                "dica_eliminar_opcoes_usada": False,
                "dica_adicional_usada": False
            }
        ]
        

        self.pergunta_atual = 0
        self.respostas_corretas = 0

        self.label_pergunta = tk.Label(self, text="", font=("Arial", 24), bg="#4caf50", fg="#333333")
        self.label_pergunta.pack(pady=10)

        self.botoes_opcoes = []
        for i in range(4):
            botao_opcao = tk.Button(self, text="", font=("Arial", 20), bg="#81c784", fg="#ffffff", activebackground="#4caf50", activeforeground="#ffffff", command=lambda index=i: self.verificar_resposta(index))
            botao_opcao.pack(pady=5)
            self.botoes_opcoes.append(botao_opcao)

        self.label_pontuacao = tk.Label(self, text="Pontuação: 0", font=("Arial", 20), bg="#4caf50", fg="#333333")
        self.label_pontuacao.pack(pady=10)

        self.label_dica = tk.Label(self, text="", font=("Arial", 16), bg="#f1f1f1", fg="#333333")
        self.label_dica.pack(pady=10)

        self.botao_dica_eliminar = tk.Button(self, text="Eliminar 2 opções", font=("Arial", 16), bg="#f44336", fg="#ffffff", activebackground="#e53935", activeforeground="#ffffff", command=self.usar_dica_eliminar)
        self.botao_dica_eliminar.pack(pady=10)

        self.botao_dica_adicional = tk.Button(self, text="Dica adicional", font=("Arial", 16), bg="#fbc02d", fg="#333333", activebackground="#f9a825", activeforeground="#333333", command=self.usar_dica_adicional)
        self.botao_dica_adicional.pack(pady=10)

        self.atualizar_pergunta()

        self.update_idletasks()

    def atualizar_pergunta(self):
        if self.pergunta_atual < len(self.perguntas):
            pergunta = self.perguntas[self.pergunta_atual]
            self.label_pergunta.config(text=pergunta["pergunta"])
            opcoes = pergunta["opcoes"]
            shuffle(opcoes)
            for i, opcao in enumerate(opcoes):
                self.botoes_opcoes[i].config(text=opcao, state=tk.NORMAL, bg="#81c784")

            if pergunta["dica_eliminar_opcoes_usada"]:
                resposta_correta = pergunta["resposta"]
                for botao in self.botoes_opcoes:
                    if botao["text"] != resposta_correta:
                        botao.config(state=tk.DISABLED, bg="#f44336")

            if pergunta["dica_adicional_usada"]:
                dica_adicional = pergunta["dica"]
                self.label_dica.config(text=dica_adicional)
            else:
                self.label_dica.config(text="")
        else:
            messagebox.showinfo("Fim do Quiz", f"Quiz concluído! Você acertou {self.respostas_corretas} de {len(self.perguntas)} perguntas.")
            self.destroy()

    def verificar_resposta(self, index):
        for botao in self.botoes_opcoes:
            botao.config(state=tk.DISABLED)

        pergunta = self.perguntas[self.pergunta_atual]
        resposta_selecionada = pergunta["opcoes"][index]
        resposta_correta = pergunta["resposta"]
        if resposta_selecionada == resposta_correta:
            self.respostas_corretas += 1
            self.botoes_opcoes[index].config(bg="#006400")
        else:
            self.botoes_opcoes[index].config(bg="#f44336")

        self.pergunta_atual += 1
        self.label_pontuacao.config(text=f"Pontuação: {self.respostas_corretas}")
        self.after(1000, self.atualizar_pergunta)

    def usar_dica_eliminar(self):
        self.botao_dica_eliminar.config(state=tk.DISABLED)
        pergunta = self.perguntas[self.pergunta_atual]
        opcoes = pergunta["opcoes"]
        resposta_correta = pergunta["resposta"]
        opcoes_restantes = [opcao for opcao in opcoes if opcao != resposta_correta][:2]
        for i, botao in enumerate(self.botoes_opcoes):
            if botao["text"] in opcoes_restantes:
                botao.config(state=tk.DISABLED, bg="#f44336")

        pergunta["dica_eliminar_opcoes_usada"] = True

    def usar_dica_adicional(self):
        self.botao_dica_adicional.config(state=tk.DISABLED)
        pergunta = self.perguntas[self.pergunta_atual]
        dica_adicional = pergunta["dica"]
        self.label_dica.config(text=dica_adicional)

        pergunta["dica_adicional_usada"] = True

app = QuizApp()
app.mainloop()