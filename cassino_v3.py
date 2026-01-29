import tkinter as tk
import random

simbolos = ["🐯", "🍒", "⭐", "💎", "🍀"]
saldo = 100

janela = tk.Tk()
janela.title("🐯 Tigrinho do Rafa")
janela.geometry("400x300")
janela.resizable(False, False)

titulo = tk.Label(janela, text="🐯 TIGRINHO DO RAFA 🐯", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

saldo_label = tk.Label(janela, text=f"Saldo: {saldo}", font=("Arial", 12))
saldo_label.pack()

frame_slots = tk.Frame(janela)
frame_slots.pack(pady=20)

slot1 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot2 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot3 = tk.Label(frame_slots, text="❓", font=("Arial", 30))

slot1.pack(side="left", padx=10)
slot2.pack(side="left", padx=10)
slot3.pack(side="left", padx=10)

resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack()

def verificar_resultado():
    global saldo

    resultado = [slot1.cget("text"), slot2.cget("text"), slot3.cget("text")]

    if resultado[0] == resultado[1] == resultado[2]:
        saldo += 50
        resultado_label.config(text="🎉 JACKPOT! +50", fg="green")
    else:
        saldo -= 10
        resultado_label.config(text="❌ Perdeu -10", fg="red")

    saldo_label.config(text=f"Saldo: {saldo}")

    if saldo <= 0:
        botao_girar.config(state="disabled")
        resultado_label.config(text="💀 GAME OVER")

def animar_giro(giros=15):
    if giros > 0:
        slot1.config(text=random.choice(simbolos))
        slot2.config(text=random.choice(simbolos))
        slot3.config(text=random.choice(simbolos))
        janela.after(100, animar_giro, giros - 1)
    else:
        verificar_resultado()

def girar():
    resultado_label.config(text="")
    animar_giro()

botao_girar = tk.Button(janela, text="🎰 GIRAR", font=("Arial", 12, "bold"), command=girar)
botao_girar.pack(pady=10)

janela.mainloop()
