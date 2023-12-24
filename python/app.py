# imports
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import random

from datetime import datetime
from itertools import count


# Criação de uma figura com subgráficos
fig = make_subplots(rows=1, cols=1, subplot_titles=['Gráfico em Tempo Real'])
trace = go.Scatter(x=[], y=[], mode='lines+markers',
                   name='Dados em Tempo Real')
fig.add_trace(trace)

# Layout do gráfico
fig.update_layout(title_text='Gráfico em Tempo Real', showlegend=True)

# Função para gerar dados em tempo real


def gerar_dados_externos():
    return [random.uniform(-1, 1) for _ in range(10)]


# Atualização do gráfico em tempo real
x_data, y_data = [], []

# Função para atualizar os dados e o gráfico
def update_graph(frame):
    global x_data, y_data
    x_data.append(datetime.now())
    y_data.extend(gerar_dados_externos() for _ in range(10))

    # Atualização dos dados no gráfico
    fig.data[0].x = x_data
    fig.data[0].y = y_data


# Atualização do gráfico em intervalos regulares
intervalo_ms = 1000  # 1 segundo
contador = count()

# Adicionando frames de animação
frames = []
for _ in range(100):  # Número de frames desejado
    next(contador)
    update_graph(_)
    frame = go.Frame(data=[go.Scatter(x=x_data, y=y_data)])
    frames.append(frame)

# Adicionando os frames à animação
fig.frames = frames

# Execução da animação
fig.show(config={'scrollZoom': False})
