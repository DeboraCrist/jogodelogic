import tkinter as tk

class JogoFutebol:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Vai que é tua Carolino")

        self.movimentos = []

        self.frame_controles = tk.Frame(self.janela, bg="#f0f0f0")
        self.frame_controles.pack(padx=10, pady=10)

        self.frame_log = tk.Frame(self.janela, bg="#f0f0f0")
        self.frame_log.pack(side=tk.RIGHT, padx=10, pady=10)

        self.texto_log = tk.Text(self.frame_log, width=30, height=10, bg="#e6e6e6", fg="#333", font=("Helvetica", 10))
        self.texto_log.pack()

        self.btn_compilar = tk.Button(self.frame_log, text="Compilar Movimentos", command=self.compilar_movimentos, bg="#4CAF50", fg="white")
        self.btn_compilar.pack(pady=(10,0))

        self.texto_log.config(state=tk.DISABLED)

        self.canvas = tk.Canvas(self.janela, width=300, height=300, bg="white", highlightthickness=0)
        self.canvas.pack()
        self.personagem = self.canvas.create_oval(140, 140, 160, 160, fill="blue")
        self.gol = self.canvas.create_rectangle(120, 20, 180, 0, fill="red")

        self.btn_frente = tk.Button(self.frame_controles, text="Mover para Frente", command=self.move_frente, bg="#4CAF50", fg="white")
        self.btn_frente.grid(row=5, column=5, padx=5, pady=5)

        self.btn_tras = tk.Button(self.frame_controles, text="Mover para Trás", command=self.move_tras, bg="#4CAF50", fg="white")
        self.btn_tras.grid(row=5, column=4, padx=5, pady=5)

        self.btn_esquerda = tk.Button(self.frame_controles, text="Mover para Esquerda", command=self.move_esquerda, bg="#4CAF50", fg="white")
        self.btn_esquerda.grid(row=6, column=4, padx=5, pady=5)

        self.btn_direita = tk.Button(self.frame_controles, text="Mover para Direita", command=self.move_direita, bg="#4CAF50", fg="white")
        self.btn_direita.grid(row=6, column=5, padx=5, pady=5)

    def move_frente(self):
        self.movimentos.append("frente")

    def move_tras(self):
        self.movimentos.append("tras")

    def move_esquerda(self):
        self.movimentos.append("esquerda")

    def move_direita(self):
        self.movimentos.append("direita")

    def verificar_gol(self):
        coordenadas_bola = self.canvas.coords(self.personagem)
        coordenadas_gol = self.canvas.coords(self.gol)
        if (coordenadas_bola[1] <= coordenadas_gol[3]):  # Check if any part of the ball crosses the goal line
            self.registrar_movimento("GOL!")
        else:
            self.registrar_movimento("Bola não chegou ao gol!")


    def compilar_movimentos(self):
        for movimento in self.movimentos:
            if movimento == "frente":
                self.canvas.move(self.personagem, 0, -25)
            elif movimento == "tras":
                self.canvas.move(self.personagem, 0, 25)
            elif movimento == "esquerda":
                self.canvas.move(self.personagem, -25, 0)
            elif movimento == "direita":
                self.canvas.move(self.personagem, 25, 0)
        self.movimentos.clear()
        self.verificar_gol()

    def registrar_movimento(self, mensagem):
        self.texto_log.config(state=tk.NORMAL)
        self.texto_log.insert(tk.END, mensagem + "\n")
        self.texto_log.see(tk.END)
        self.texto_log.config(state=tk.DISABLED)

    def main(self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = tk.Tk()
    jogo = JogoFutebol(janela)
    jogo.main()
