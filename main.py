import tkinter as tk

movimentos = []
botoes = []

def iniciar_arrastar(event, botao):
    canvas.bind("<B1-Motion>", lambda event, botao=botao: arrastar(event, botao))

def arrastar(event, botao):
    x, y = event.x, event.y
    canvas.coords(botao, x - 10, y - 10, x + 10, y + 10)

def move_frente():
    movimentos.append("frente")
    criar_botao_log("Frente")

def move_tras():
    movimentos.append("tras")
    criar_botao_log("Trás")

def move_esquerda():
    movimentos.append("esquerda")
    criar_botao_log("Esquerda")

def move_direita():
    movimentos.append("direita")
    criar_botao_log("Direita")

def verificar_gol():
    coordenadas_bola = canvas.coords(personagem)
    coordenadas_gol = canvas.coords(gol)
    if coordenadas_bola[0] >= coordenadas_gol[0] and coordenadas_bola[1] >= coordenadas_gol[1] and coordenadas_bola[2] <= coordenadas_gol[2] and coordenadas_bola[3] <= coordenadas_gol[3]:
        registrar_movimento("Bola chegou ao gol!")
    else:
        registrar_movimento("Bola não chegou ao gol!")

def compilar_movimentos():
    for movimento in movimentos:
        if movimento == "frente":
            canvas.move(personagem, 0, -20)
        elif movimento == "tras":
            canvas.move(personagem, 0, 20)
        elif movimento == "esquerda":
            canvas.move(personagem, -20, 0)
        elif movimento == "direita":
            canvas.move(personagem, 20, 0)
    movimentos.clear()
    verificar_gol()

def criar_botao_log(texto):
    botao = tk.Button(frame_log, text=texto)
    botao.pack()
    botao.bind("<Button-1>", lambda event, botao=botao: iniciar_arrastar(event, botao))
    botoes.append(botao)

def registrar_movimento(mensagem):
    texto_log.config(state=tk.NORMAL)
    texto_log.insert(tk.END, mensagem + "\n")
    texto_log.see(tk.END)
    texto_log.config(state=tk.DISABLED)

def mover_bola_perto_do_gol():
    canvas.coords(personagem, 150, 140, 170, 160)  # Move a bola mais perto do gol
    verificar_gol()

def main():
    janela = tk.Tk()
    janela.title("Vai que é tua Carolino")

    frame_controles = tk.Frame(janela)
    frame_controles.pack(side=tk.LEFT, padx=10, pady=10)

    global frame_log
    frame_log = tk.Frame(janela)
    frame_log.pack(side=tk.RIGHT, padx=10, pady=10)

    btn_frente = tk.Button(frame_controles, text="Mover para Frente", command=move_frente)
    btn_frente.grid(row=0, column=0)

    btn_tras = tk.Button(frame_controles, text="Mover para Trás", command=move_tras)
    btn_tras.grid(row=1, column=0)

    btn_esquerda = tk.Button(frame_controles, text="Mover para Esquerda", command=move_esquerda)
    btn_esquerda.grid(row=2, column=0)

    btn_direita = tk.Button(frame_controles, text="Mover para Direita", command=move_direita)
    btn_direita.grid(row=3, column=0)

    global texto_log
    texto_log = tk.Text(frame_log, width=30, height=10)
    texto_log.pack()

    btn_compilar = tk.Button(frame_log, text="Compilar Movimentos", command=compilar_movimentos)
    btn_compilar.pack()

    texto_log.config(state=tk.DISABLED)

    global canvas, personagem, gol
    canvas = tk.Canvas(janela, width=300, height=300)
    canvas.pack()
    personagem = canvas.create_oval(140, 140, 160, 160, fill="blue")
    gol = canvas.create_rectangle(120, 20, 180, 0, fill="red")

    janela.mainloop()

if __name__ == "__main__":
    main()
