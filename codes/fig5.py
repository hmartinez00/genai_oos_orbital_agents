import numpy as np
import matplotlib.pyplot as plt

# 1. GENERACIÓN DE DATOS (Simulación científica)
episodes_full = np.linspace(0, 2000, 100)
episodes_tikz = np.linspace(0, 2000, 15) # Menos puntos para un TikZ más limpio

def get_y(x, speed, final_val):
    return final_val * (1 - np.exp(-x / speed))

# Datos para las curvas
curves = {
    'Hybrid': {'speed': 180, 'val': 0.95, 'color': 'blue', 'mark': 'o', 'label': 'Propuesto (Hibrido)'},
    'ART':    {'speed': 450, 'val': 0.85, 'color': 'black', 'mark': 'square*', 'label': 'ART Baseline'},
    'MARL':   {'speed': 800, 'val': 0.70, 'color': 'gray', 'mark': 'triangle*', 'label': 'MARL Puro'},
    'LLM':    {'speed': 1200, 'val': 0.62, 'color': 'lightgray', 'mark': 'diamond*', 'label': 'LLM-only'}
}

# 2. RENDERIZADO EN MATPLOTLIB (Para validación rápida)
plt.figure(figsize=(8, 5))
for name, conf in curves.items():
    y = get_y(episodes_full, conf['speed'], conf['val'])
    plt.plot(episodes_full, y, label=conf['label'], linewidth=2)

plt.title("Vista previa (Matplotlib)")
plt.legend()
plt.show()

# 3. GENERADOR DE CÓDIGO TIKZ (PGFPLOTS)
print("\n" + "="*30)
print("CÓDIGO TIKZ PARA OVERLEAF")
print("="*30 + "\n")

tikz_code = r"""\begin{tikzpicture}
\begin{axis}[
    width=0.95\textwidth, height=7cm,
    grid=both, grid style={line width=.1pt, draw=gray!10},
    major grid style={line width=.2pt, draw=gray!30},
    xlabel={Training Episodes},
    ylabel={Mean Reward},
    xmin=0, xmax=2000, ymin=0, ymax=1,
    legend pos=south east,
    legend style={font=\tiny, cells={anchor=west}},
    no markers
]"""

for name, conf in curves.items():
    coords = "".join([f"({x:.0f},{get_y(x, conf['speed'], conf['val']):.3f})" for x in episodes_tikz])
    tikz_code += f"\n\\addplot[thick, {conf['color']}, mark={conf['mark']}, mark size=1.5pt] coordinates {{{coords}}};"
    tikz_code += f"\n\\addlegendentry{{{conf['label']}}}"

tikz_code += "\n\\end{axis}\n\\end{tikzpicture}"

print(tikz_code)