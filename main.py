import tkinter as tk

class BotaoMovimento(tk.Button):
    def __init__(self, *args, direcao=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.direcao = direcao

class JogoFutebol:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Vai que é tua Carolino")

        self.movimentos = []

        self.label_fase = tk.Label(self.janela, text="Primeira Fase", bg="#f0f0f0", fg="#333", font=("Helvetica", 14, "bold"))
        self.label_fase.pack(pady=(5, 5))

        self.frame_controles = tk.Frame(self.janela, bg="#f0f0f0")
        self.frame_controles.pack(padx=10, pady=10)

        self.frame_log = tk.Frame(self.janela, bg="#f0f0f0")
        self.frame_log.pack(side=tk.RIGHT, padx=10, pady=10)

        self.label_status = tk.Label(self.frame_log, text="", bg="#f0f0f0", fg="#333", font=("Helvetica", 10))
        self.label_status.pack()

        self.btn_compilar = tk.Button(self.frame_log, text="Compilar Movimentos", command=self.compilar_movimentos, bg="#4CAF50", fg="white")
        self.btn_compilar.pack(side=tk.BOTTOM, pady=(10,0))

        self.canvas = tk.Canvas(self.janela, width=300, height=300, bg="white", highlightthickness=0)
        self.canvas.pack()
        self.personagem = self.canvas.create_oval(140, 140, 160, 160, fill="blue")
        self.gol = self.canvas.create_rectangle(120, 20, 180, 0, fill="red")

        self.btn_frente = BotaoMovimento(self.frame_controles, text="Mover para Frente", command=lambda: self.move("frente"), bg="#4CAF50", fg="white", direcao="frente")
        self.btn_frente.grid(row=5, column=5, padx=5, pady=5)

        self.btn_tras = BotaoMovimento(self.frame_controles, text="Mover para Trás", command=lambda: self.move("tras"), bg="#4CAF50", fg="white", direcao="tras")
        self.btn_tras.grid(row=5, column=4, padx=5, pady=5)

        self.btn_esquerda = BotaoMovimento(self.frame_controles, text="Mover para Esquerda", command=lambda: self.move("esquerda"), bg="#4CAF50", fg="white", direcao="esquerda")
        self.btn_esquerda.grid(row=6, column=4, padx=5, pady=5)

        self.btn_direita = BotaoMovimento(self.frame_controles, text="Mover para Direita", command=lambda: self.move("direita"), bg="#4CAF50", fg="white", direcao="direita")
        self.btn_direita.grid(row=6, column=5, padx=5, pady=5)

    def move(self, direcao):
        self.movimentos.append(direcao)
        original_bg = self.btn_frente.cget('bg')
        btn_movimento = BotaoMovimento(self.frame_log, text=direcao.capitalize(), bg=original_bg, fg="white", direcao=direcao)
        btn_movimento.pack(side=tk.BOTTOM)
        btn_movimento.config(command=lambda: self.remover_movimento(btn_movimento))
        self.btn_compilar.config(state=tk.NORMAL if self.movimentos else tk.DISABLED)

    def remover_movimento(self, btn_movimento):
        direcao = btn_movimento.direcao
        if direcao in self.movimentos:
            self.movimentos.remove(direcao)
            btn_movimento.destroy()


    def verificar_gol(self):
        coordenadas_bola = self.canvas.coords(self.personagem)
        coordenadas_gol = self.canvas.coords(self.gol)
        if coordenadas_bola[1] <= coordenadas_gol[3]:  
            self.registrar_movimento("GOL!")
            self.iniciar_segunda_fase()
        else:
            self.registrar_movimento("Bola não chegou ao gol!")

    def iniciar_segunda_fase(self):
        self.canvas.itemconfig(self.gol, fill="green")

    def compilar_movimentos(self):
        movimentos_temporarios = list(self.movimentos)  
        for movimento in movimentos_temporarios:
            if movimento == "frente":
                self.canvas.move(self.personagem, 0, -25)
            elif movimento == "tras":
                self.canvas.move(self.personagem, 0, 25)
            elif movimento == "esquerda":
                self.canvas.move(self.personagem, -25, 0)
            elif movimento == "direita":
                self.canvas.move(self.personagem, 25, 0)
        self.verificar_gol()
        self.movimentos.clear()
        self.btn_compilar.config(state=tk.NORMAL)


    def repetir_movimento(self, direcao):
        self.move(direcao)

    def registrar_movimento(self, mensagem):
        self.label_status.config(text=mensagem)  
        self.janela.after(2000, lambda: self.label_status.config(text="")) 

    def main(self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = tk.Tk()
    jogo = JogoFutebol(janela)
    jogo.main()
