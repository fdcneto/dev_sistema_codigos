# ===========================================
# 🧮 CALCULADORA PYTHON COM INTERFACE MODERNA
# Feita com Tkinter
# Autor: Francisco (com ajuda do ChatGPT 😄)
# ===========================================

import tkinter as tk
from tkinter import ttk

# ------------------------------
# 🎨 1. Configuração da janela
# ------------------------------
janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("340x520")
janela.resizable(False, False)
janela.configure(bg="#dbe4ee")  # fundo cinza-azulado suave

# ------------------------------
# 🖋️ 2. Campo de entrada (visor)
# ------------------------------
visor = tk.Entry(
    janela, width=16, font=("Segoe UI", 26), borderwidth=4,
    relief="flat", justify="right", bg="#f1f3f6", fg="#0a0a0a"
)
visor.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

# ------------------------------
# ⚙️ 3. Funções da calculadora
# ------------------------------
def clicar(botao):
    """Adiciona o número ou símbolo no visor"""
    visor.insert(tk.END, botao)

def limpar():
    """Limpa o visor"""
    visor.delete(0, tk.END)

def calcular():
    """Executa a expressão matemática"""
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# ------------------------------
# 🔢 4. Lista de botões
# ------------------------------
botoes = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

# ------------------------------
# 🎨 5. Estilos de botão
# ------------------------------
style_padrao = {
    "font": ("Segoe UI", 14, "bold"),
    "width": 5,
    "height": 2,
    "relief": "flat",
    "bg": "#e7eef6",
    "fg": "#0a0a0a",
    "activebackground": "#bdd1ec",
    "activeforeground": "#0a0a0a"
}

style_operador = {
    **style_padrao,
    "bg": "#a8c4f0",
    "fg": "#0a0a0a",
    "activebackground": "#7faee8"
}

# ------------------------------
# 🔘 6. Criar e posicionar botões
# ------------------------------
linha_inicial = 1
for linha, grupo in enumerate(botoes):
    for coluna, simbolo in enumerate(grupo):
        if simbolo == '=':
            botao = tk.Button(
                janela, text=simbolo, command=calcular,
                **style_operador
            )
        elif simbolo in ['/', '*', '-', '+']:
            botao = tk.Button(
                janela, text=simbolo,
                command=lambda s=simbolo: clicar(s),
                **style_operador
            )
        else:
            botao = tk.Button(
                janela, text=simbolo,
                command=lambda s=simbolo: clicar(s),
                **style_padrao
            )

        botao.grid(row=linha+linha_inicial, column=coluna, padx=5, pady=5)

# ------------------------------
# 🧹 7. Botão limpar (C)
# ------------------------------
tk.Button(
    janela, text="Clear", command=limpar,
    font=("Segoe UI", 14, "bold"),
    width=22, height=2, relief="flat",
    bg="#b0c4de", fg="#0a0a0a",
    activebackground="#8ca9c7"
).grid(row=linha_inicial+4, column=0, columnspan=4, pady=15)

# ------------------------------
# ▶️ 8. Rodar o programa
# ------------------------------
janela.mainloop()
