import tkinter as tk
from tkinter import messagebox

class BotaoMovimento(tk.Button):
    def __init__(self, *args, direcao=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.direcao = direcao

class JogoFutebol:
    def __init__(self, janela):
        self.primeira_fase_concluida = False
        self.janela = janela
        self.janela.title("Vai que é tua Carolino")
        self.janela.configure(bg="white")  

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

        self.btn_reset = tk.Button(self.frame_log, text="Resetar Jogo", command=self.resetar_jogo, bg="#FF5733", fg="white")
        self.btn_reset.pack(side=tk.BOTTOM, pady=(5,0))

        self.canvas = tk.Canvas(self.janela, width=300, height=350, bg="white", highlightthickness=0)
        self.canvas.pack()

        self.imagem_fundo = tk.PhotoImage(file="campo.png")

        x_center = (300 - self.imagem_fundo.width()) // 2

        self.canvas.create_image(x_center, 0, anchor=tk.NW, image=self.imagem_fundo)
        
        self.personagem = self.canvas.create_oval(140, 140, 160, 160, fill="blue")
        self.gol = self.canvas.create_rectangle(120, 20, 180, 0, fill="red")

        self.btn_frente = BotaoMovimento(self.frame_controles, text="Mover para frente", command=lambda: self.move("Mover para frente"), bg="#4CAF50", fg="white", direcao="frente")
        self.btn_frente.grid(row=5, column=5, padx=5, pady=5)

        self.btn_tras = BotaoMovimento(self.frame_controles, text="Mover para trás", command=lambda: self.move("Mover para trás"), bg="#4CAF50", fg="white", direcao="tras")
        self.btn_tras.grid(row=5, column=4, padx=5, pady=5)

        self.btn_esquerda = BotaoMovimento(self.frame_controles, text="Mover para esquerda", command=lambda: self.move("Mover para esquerda"), bg="#4CAF50", fg="white", direcao="esquerda")
        self.btn_esquerda.grid(row=6, column=4, padx=5, pady=5)

        self.btn_direita = BotaoMovimento(self.frame_controles, text="Mover para direita", command=lambda: self.move("Mover para direita"), bg="#4CAF50", fg="white", direcao="direita")
        self.btn_direita.grid(row=6, column=5, padx=5, pady=5)

    def move(self, direcao):
        self.movimentos.append(direcao)
        original_bg = self.btn_frente.cget('bg')
        btn_movimento = BotaoMovimento(self.frame_log, text=direcao.capitalize(), bg=original_bg, fg="white", direcao=direcao)
        btn_movimento.pack(side=tk.BOTTOM)
        btn_movimento.config(command=lambda: self.remover_movimento(btn_movimento, direcao))  
        self.btn_compilar.config(state=tk.NORMAL if self.movimentos else tk.DISABLED)

    def remover_movimento(self, btn_movimento, direcao):
        if direcao in self.movimentos:
            self.movimentos.remove(direcao)
            btn_movimento.destroy()

    def verificar_gol(self):
        coordenadas_bola = self.canvas.coords(self.personagem)
        coordenadas_gol = self.canvas.coords(self.gol)
        if coordenadas_bola[1] <= coordenadas_gol[3] and coordenadas_bola[0] >= coordenadas_gol[0] and coordenadas_bola[2] <= coordenadas_gol[2]:  
            if not self.primeira_fase_concluida:
                self.primeira_fase_concluida = True
                movimentos_str = '\n'.join(self.movimentos)
                messagebox.showinfo("GOLLL!", f"Você resolveu este nível com {len(self.movimentos)} linhas de Python:\n{movimentos_str}\n\nVocê está pronto para o nível 2?")
                self.iniciar_segunda_fase()
            else:
                self.registrar_movimento("Segunda fase já iniciada!")
        else:
            self.registrar_movimento("Bola não chegou ao gol!")

    def resetar_jogo(self):
        self.limpar_jogo()

    def iniciar_segunda_fase(self):
        self.limpar_jogo()
        self.label_fase.config(text="Segunda Fase")
        self.canvas.coords(self.gol, 100, 0, 200, 20) 
        self.canvas.itemconfig(self.gol, fill="red")
        self.bola = self.canvas.create_oval(140, 140, 160, 160, fill="yellow")

    def limpar_jogo(self):
        self.canvas.delete("all")
        self.movimentos.clear()
        self.label_status.config(text="")
        self.gol = self.canvas.create_rectangle(120, 20, 180, 0, fill="red")
        self.imagem_fundo = tk.PhotoImage(file="campo.png")
        x_center = (300 - self.imagem_fundo.width()) // 2
        self.canvas.create_image(x_center, 0, anchor=tk.NW, image=self.imagem_fundo)

    def compilar_movimentos(self):
        movimentos_temporarios = list(self.movimentos)  
        for movimento in movimentos_temporarios:
            if movimento == "Mover para frente":
                self.canvas.move(self.personagem, 0, -50)
            elif movimento == "Mover para trás":
                self.canvas.move(self.personagem, 0, 50)
            elif movimento == "Mover para esquerda":
                self.canvas.move(self.personagem, -50, 0)
            elif movimento == "Mover para direita":
                self.canvas.move(self.personagem, 50, 0)
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
