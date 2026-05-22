import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURACIÓN DE DATOS (Puntos medios de la tabla de estimación real) ---
years = np.array([2022, 2023, 2024, 2025, 2026])

# IA Generativa / LLMs (Crecimiento exponencial post-ChatGPT)
# Rangos: [10, 30, 62, 97, 125]
gen_ai_llms = np.array([10, 30, 62, 97, 125])

# MARL / Agentes Autónomos (Crecimiento sostenido por simuladores)
# Rangos: [17, 25, 40, 52, 65]
marl_agents = np.array([17, 25, 40, 52, 65])

# Arquitecturas Autónomas OSAM (Base consolidada y emergente)
# Rangos: [30, 35, 45, 57, 70]
osam_archs = np.array([30, 35, 45, 57, 70])

# --- CONFIGURACIÓN ESTÉTICA IEEE ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.linewidth": 1.2,
    "xtick.direction": "in",
    "ytick.direction": "in"
})

colors = {
    'gen_ai': '#0047AB',  # Azul Cobalto (Tendencia dominante)
    'marl': '#4A4A4A',    # Gris Técnico
    'osam': '#000000'     # Negro
}

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# --- GENERACIÓN DE SERIES ---
# Graficamos con marcadores y líneas de grosor diferenciado
ax.plot(years, gen_ai_llms, color=colors['gen_ai'], marker='o', markersize=7,
        linewidth=2.5, label='Generative AI / LLMs', markerfacecolor='white', zorder=5)

ax.plot(years, marl_agents, color=colors['marl'], marker='s', markersize=6,
        linewidth=2.0, label='MARL / Autonomous Agents', markerfacecolor='white', zorder=4)

ax.plot(years, osam_archs, color=colors['osam'], marker='^', markersize=7,
        linewidth=2.0, label='OSAM Architectures', markerfacecolor='white', zorder=3)

# --- ESTILIZACIÓN DE EJES ---
ax.set_xlabel('Year', fontweight='bold', labelpad=12)
ax.set_ylabel('Number of Indexed Publications (Est.)', fontweight='bold', labelpad=12)

# Ajuste de ticks y límites
ax.set_xticks(years)
ax.set_ylim(0, 150) # Margen superior para la curva azul
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Eliminar bordes innecesarios
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# --- LEYENDA TÉCNICA ---
ax.legend(loc='upper left', frameon=True, fancybox=False, edgecolor='black', fontsize=10)

# Anotación del hito 2022 (Explosión Generativa)
ax.annotate('Post-ChatGPT Surge', xy=(2023, 30), xytext=(2022.5, 60),
            arrowprops=dict(arrowstyle='->', color=colors['gen_ai']),
            color=colors['gen_ai'], fontsize=9, fontweight='bold')

plt.tight_layout()

# Exportación para el reporte científico
plt.savefig('fig2_estado_del_arte_realista.png', bbox_inches='tight')
plt.savefig('fig2_estado_del_arte_realista.pdf', bbox_inches='tight')

plt.show()