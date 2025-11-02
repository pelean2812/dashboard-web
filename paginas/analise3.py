import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
st.set_page_config(layout="wide")

matriculas_direito = pd.read_csv("dados/matriculas_direito.csv", sep=';')
matriculas_direito['semestre'] = matriculas_direito['semestre'].astype(str)
matriculas_direito_sem_trancamento = matriculas_direito[matriculas_direito['descricao'] != 'TRANCADO'].copy()

semestres_ordenados = [
    '2011.1',	'2011.2',	'2012.1',	'2012.2', '2013.1',	'2013.2',	'2014.1',	'2014.2',
    '2015.1',	'2015.2',	'2016.1',	'2016.2',	'2017.1',	'2017.2',	'2018.1',	'2018.2',
    '2019.1',	'2019.2',	'2020.5',	'2020.6',	'2020.2',	'2021.1',	'2021.2',	'2022.1',
    '2022.2',	'2023.1',	'2023.2',	'2024.1',	'2024.2']

disciplinas_p1 = [
  'METODOLOGIA DA PESQUISA I',
  'CIENCIA POLITICA I',
  'SOCIOLOGIA E ANTROPOLOGIA GERAL',
  'INTRODUCAO AO ESTUDO DO DIREITO',
  'FILOSOFIA I'
]

disciplinas_p2 = [
  'DIREITO CIVIL I',
  'HISTORIA DO DIREITO',
  'DIREITO CONSTITUCIONAL I',
  'DIREITO PENAL I',
  'ECONOMIA POLITICA',
  'PSICOLOGIA APLICADA AO DIREITO'
]

disciplinas_p3 = [
  'DIREITO CIVIL II',
  'FILOSOFIA DO DIREITO',
  'TEORIA GERAL DO PROCESSO',
  'HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO',
  'DIREITO CONSTITUCIONAL II',
  'DIREITO PENAL II'
]

disciplinas_p4 = [
  'DIREITO CIVIL III',
  'DIREITO EMPRESARIAL I',
  'DIREITO INTERNACIONAL PUBLICO',
  'SOCIOLOGIA JURIDICA',
  'DIREITO PENAL III',
  'DIREITO PROCESSUAL CIVIL I'
]

disciplinas_p5 = [
  'DIREITO CIVIL IV',
  'DIREITO EMPRESARIAL II',
  'DIREITO ADMINISTRATIVO I',
  'DIREITO PENAL IV',
  'DIREITO PROCESSUAL CIVIL II',
  'DIREITOS HUMANOS FUNDAMENTAIS'
]

disciplinas_p6 = [
  'DIREITO CIVIL V',
  'DIREITO EMPRESARIAL III',
  'DIREITO ADMINISTRATIVO II',
  'DIREITO PROCESSUAL CIVIL III',
  'DIREITO PROCESSUAL PENAL I',
  'DIREITO DAS RELACOES DE CONSUMO'
]

disciplinas_p7 = [
  'DIREITO CIVIL VI',
  'DIREITO DO TRABALHO I',
  'AUTOCOMPOSICAO DE CONFLITOS: NEGOCIACAO, CONCILIACAO E MEDIACAO',
  'CARREIRAS JURIDICAS',
  'PECAS JURIDICAS II (EXTRAJUDICIAIS)',
  'PECAS JURIDICAS I (JUDICIAIS)',
  'DIREITO PROCESSUAL CIVIL IV',
  'DIREITO PROCESSUAL PENAL II',
  'ETICA GERAL E PROFISSIONAL'
]

disciplinas_p8 = [
  'METODOLOGIA DA PESQUISA II',
  'DIREITO CIVIL VII',
  'DIREITO DO TRABALHO II',
  'DIREITO TRIBUTARIO',
  'DIREITO PROCESSUAL COLETIVO'
]

disciplinas_p9 = [
  'DIREITO CIVIL VIII',
  'DIREITO DO TRABALHO III',
  'PRATICA JURIDICA III - ATENDIMENTOS',
  'DIREITO PROCESSUAL DO TRABALHO'
]

disciplinas_p10 = [
  'ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'
]

notas_faltas_p1 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p1)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p2 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p2)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p3 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p3)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p4 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p4)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p5 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p5)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p6 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p6)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p7 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p7)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p8 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p8)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p9 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p9)][['nome_componente','media_final', 'numero_total_faltas']]
notas_faltas_p10 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p10)][['nome_componente','media_final', 'numero_total_faltas']]

total_alunos_p1_0 = len(notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[0]])

intervalo_faltas_1 = np.arange(0, 35, 2)
intervalo_media_1 = np.arange(0, 11, 1)

dados_heatmap_1, yedges, xedges = np.histogram2d(
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[0]]['media_final'],
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[0]]['numero_total_faltas'],
  bins=[intervalo_media_1, intervalo_faltas_1]
)

heatmap_1 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_1,
    y = intervalo_media_1,
    z = dados_heatmap_1,
    colorscale='Plasma',
    text=dados_heatmap_1,
    texttemplate="%{text}"
))

heatmap_1.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p1[0]} ({total_alunos_p1_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_1,range=[0, 34]),
    yaxis=dict(tickvals=intervalo_media_1,range=[0, 10])
)

total_alunos_p1_1 = len(notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[1]])

intervalo_faltas_2 = np.arange(0, 77, 2)
intervalo_media_2 = np.arange(0, 11, 1)

dados_heatmap_2, yedges, xedges = np.histogram2d(
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[1]]['media_final'],
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[1]]['numero_total_faltas'],
  bins=[intervalo_media_2, intervalo_faltas_2]
)

heatmap_2 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_2,
    y = intervalo_media_2,
    z = dados_heatmap_2,
    colorscale='Plasma',
    text=dados_heatmap_2,
    texttemplate="%{text}"
))

heatmap_2.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p1[1]} ({total_alunos_p1_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_2,range=[0, 76]),
    yaxis=dict(tickvals=intervalo_media_2,range=[0, 10])
)

total_alunos_p1_2 = len(notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[2]])

intervalo_faltas_3 = np.arange(0, 67, 2)
intervalo_media_3 = np.arange(0, 11, 1)

dados_heatmap_3, yedges, xedges = np.histogram2d(
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[2]]['media_final'],
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[2]]['numero_total_faltas'],
  bins=[intervalo_media_3, intervalo_faltas_3]
)

heatmap_3 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_3,
    y = intervalo_media_3,
    z = dados_heatmap_3,
    colorscale='Plasma',
    text=dados_heatmap_3,
    texttemplate="%{text}"
))

heatmap_3.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p1[2]} ({total_alunos_p1_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_3,range=[0, 66]),
    yaxis=dict(tickvals=intervalo_media_3,range=[0, 10])
)

total_alunos_p1_3 = len(notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[3]])

intervalo_faltas_4 = np.arange(0, 113, 2)
intervalo_media_4 = np.arange(0, 11, 1)

dados_heatmap_4, yedges, xedges = np.histogram2d(
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[3]]['media_final'],
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[3]]['numero_total_faltas'],
  bins=[intervalo_media_4, intervalo_faltas_4]
)

heatmap_4 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_4,
    y = intervalo_media_4,
    z = dados_heatmap_4,
    colorscale='Plasma',
    text=dados_heatmap_4,
    texttemplate="%{text}"
))

heatmap_4.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p1[3]} ({total_alunos_p1_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_4,range=[0, 112]),
    yaxis=dict(tickvals=intervalo_media_4,range=[0, 10])
)

total_alunos_p1_4 = len(notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[4]])

intervalo_faltas_5 = np.arange(0, 85, 2)
intervalo_media_5 = np.arange(0, 11, 1)

dados_heatmap_5, yedges, xedges = np.histogram2d(
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[4]]['media_final'],
  notas_faltas_p1[notas_faltas_p1['nome_componente'] == disciplinas_p1[4]]['numero_total_faltas'],
  bins=[intervalo_media_5, intervalo_faltas_5]
)

heatmap_5 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_5,
    y = intervalo_media_5,
    z = dados_heatmap_5,
    colorscale='Plasma',
    text=dados_heatmap_5,
    texttemplate="%{text}"
))

heatmap_5.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p1[4]} ({total_alunos_p1_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_5,range=[0, 84]),
    yaxis=dict(tickvals=intervalo_media_5,range=[0, 10])
)

total_alunos_p2_0 = len(notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[0]])

intervalo_faltas_6 = np.arange(0, 83, 2)
intervalo_media_6 = np.arange(0, 11, 1)

dados_heatmap_6, yedges, xedges = np.histogram2d(
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[0]]['media_final'],
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[0]]['numero_total_faltas'],
  bins=[intervalo_media_6, intervalo_faltas_6]
)

heatmap_6 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_6,
    y = intervalo_media_6,
    z = dados_heatmap_6,
    colorscale='Plasma',
    text=dados_heatmap_6,
    texttemplate="%{text}"
))

heatmap_6.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p2[0]} ({total_alunos_p2_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_6,range=[0, 82]),
    yaxis=dict(tickvals=intervalo_media_6,range=[0, 10])
)

total_alunos_p2_1 = len(notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[1]])

intervalo_faltas_7 = np.arange(0, 37, 2)
intervalo_media_7 = np.arange(0, 11, 1)

dados_heatmap_7, yedges, xedges = np.histogram2d(
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[1]]['media_final'],
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[1]]['numero_total_faltas'],
  bins=[intervalo_media_7, intervalo_faltas_7]
)

heatmap_7 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_7,
    y = intervalo_media_7,
    z = dados_heatmap_7,
    colorscale='Plasma',
    text=dados_heatmap_7,
    texttemplate="%{text}"
))

heatmap_7.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p2[1]} ({total_alunos_p2_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_7,range=[0, 36]),
    yaxis=dict(tickvals=intervalo_media_7,range=[0, 10])
)

total_alunos_p2_2 = len(notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[2]])

intervalo_faltas_8 = np.arange(0, 75, 2)
intervalo_media_8 = np.arange(0, 11, 1)

dados_heatmap_8, yedges, xedges = np.histogram2d(
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[2]]['media_final'],
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[2]]['numero_total_faltas'],
  bins=[intervalo_media_8, intervalo_faltas_8]
)

heatmap_8 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_8,
    y = intervalo_media_8,
    z = dados_heatmap_8,
    colorscale='Plasma',
    text=dados_heatmap_8,
    texttemplate="%{text}"
))

heatmap_8.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p2[2]} ({total_alunos_p2_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_8,range=[0, 74]),
    yaxis=dict(tickvals=intervalo_media_8,range=[0, 10])
)

total_alunos_p2_3 = len(notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[3]])

intervalo_faltas_9 = np.arange(0, 51, 2)
intervalo_media_9 = np.arange(0, 11, 1)

dados_heatmap_9, yedges, xedges = np.histogram2d(
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[3]]['media_final'],
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[3]]['numero_total_faltas'],
  bins=[intervalo_media_9, intervalo_faltas_9]
)

heatmap_9 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_9,
    y = intervalo_media_9,
    z = dados_heatmap_9,
    colorscale='Plasma',
    text=dados_heatmap_9,
    texttemplate="%{text}"
))

heatmap_9.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p2[3]} ({total_alunos_p2_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_9,range=[0, 50]),
    yaxis=dict(tickvals=intervalo_media_9,range=[0, 10])
)

total_alunos_p2_4 = len(notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[4]])

intervalo_faltas_10 = np.arange(0, 77, 2)
intervalo_media_10 = np.arange(0, 11, 1)

dados_heatmap_10, yedges, xedges = np.histogram2d(
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[4]]['media_final'],
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[4]]['numero_total_faltas'],
  bins=[intervalo_media_10, intervalo_faltas_10]
)

heatmap_10 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_10,
    y = intervalo_media_10,
    z = dados_heatmap_10,
    colorscale='Plasma',
    text=dados_heatmap_10,
    texttemplate="%{text}"
))

heatmap_10.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p2[4]} ({total_alunos_p2_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_10,range=[0, 76]),
    yaxis=dict(tickvals=intervalo_media_10,range=[0, 10])
)

total_alunos_p2_5 = len(notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[5]])

intervalo_faltas_11 = np.arange(0, 69, 2)
intervalo_media_11 = np.arange(0, 11, 1)

dados_heatmap_11, yedges, xedges = np.histogram2d(
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[5]]['media_final'],
  notas_faltas_p2[notas_faltas_p2['nome_componente'] == disciplinas_p2[5]]['numero_total_faltas'],
  bins=[intervalo_media_11, intervalo_faltas_11]
)

heatmap_11 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_11,
    y = intervalo_media_11,
    z = dados_heatmap_11,
    colorscale='Plasma',
    text=dados_heatmap_11,
    texttemplate="%{text}"
))

heatmap_11.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p2[5]} ({total_alunos_p2_5} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_11,range=[0, 68]),
    yaxis=dict(tickvals=intervalo_media_11,range=[0, 10])
)

total_alunos_p3_0 = len(notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[0]])

intervalo_faltas_12 = np.arange(0, 69, 2)
intervalo_media_12 = np.arange(0, 11, 1)

dados_heatmap_12, yedges, xedges = np.histogram2d(
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[0]]['media_final'],
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[0]]['numero_total_faltas'],
  bins=[intervalo_media_12, intervalo_faltas_12]
)

heatmap_12 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_12,
    y = intervalo_media_12,
    z = dados_heatmap_12,
    colorscale='Plasma',
    text=dados_heatmap_12,
    texttemplate="%{text}"
))

heatmap_12.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p3[0]} ({total_alunos_p3_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_12,range=[0, 68]),
    yaxis=dict(tickvals=intervalo_media_12,range=[0, 10])
)

total_alunos_p3_1 = len(notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[1]])

intervalo_faltas_13 = np.arange(0, 61, 2)
intervalo_media_13 = np.arange(0, 11, 1)

dados_heatmap_13, yedges, xedges = np.histogram2d(
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[1]]['media_final'],
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[1]]['numero_total_faltas'],
  bins=[intervalo_media_13, intervalo_faltas_13]
)

heatmap_13 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_13,
    y = intervalo_media_13,
    z = dados_heatmap_13,
    colorscale='Plasma',
    text=dados_heatmap_13,
    texttemplate="%{text}"
))

heatmap_13.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p3[1]} ({total_alunos_p3_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_13,range=[0, 60]),
    yaxis=dict(tickvals=intervalo_media_13,range=[0, 10])
)

total_alunos_p3_2 = len(notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[2]])

intervalo_faltas_14 = np.arange(0, 55, 2)
intervalo_media_14 = np.arange(0, 11, 1)

dados_heatmap_14, yedges, xedges = np.histogram2d(
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[2]]['media_final'],
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[2]]['numero_total_faltas'],
  bins=[intervalo_media_14, intervalo_faltas_14]
)

heatmap_14 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_14,
    y = intervalo_media_14,
    z = dados_heatmap_14,
    colorscale='Plasma',
    text=dados_heatmap_14,
    texttemplate="%{text}"
))

heatmap_14.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p3[2]} ({total_alunos_p3_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_14,range=[0, 54]),
    yaxis=dict(tickvals=intervalo_media_14,range=[0, 10])
)

total_alunos_p3_3 = len(notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[3]])

intervalo_faltas_15 = np.arange(0, 73, 2)
intervalo_media_15 = np.arange(0, 11, 1)

dados_heatmap, yedges, xedges = np.histogram2d(
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[3]]['media_final'],
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[3]]['numero_total_faltas'],
  bins=[intervalo_media_15, intervalo_faltas_15]
)

heatmap_15 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_15,
    y = intervalo_media_15,
    z = dados_heatmap,
    colorscale='Plasma',
    text=dados_heatmap,
    texttemplate="%{text}"
))

heatmap_15.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p3[3]} ({total_alunos_p3_3} discentes)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_15,range=[0, 72]),
    yaxis=dict(tickvals=intervalo_media_15,range=[0, 10])
)

total_alunos_p3_4 = len(notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[4]])

intervalo_faltas_16 = np.arange(0, 73, 2)
intervalo_media_16 = np.arange(0, 11, 1)

dados_heatmap_16, yedges, xedges = np.histogram2d(
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[4]]['media_final'],
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[4]]['numero_total_faltas'],
  bins=[intervalo_media_16, intervalo_faltas_16]
)

heatmap_16 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_16,
    y = intervalo_media_16,
    z = dados_heatmap_16,
    colorscale='Plasma',
    text=dados_heatmap_16,
    texttemplate="%{text}"
))

heatmap_16.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p3[4]} ({total_alunos_p3_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_16,range=[0, 72]),
    yaxis=dict(tickvals=intervalo_media_16,range=[0, 10])
)

total_alunos_p3_5 = len(notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[5]])

intervalo_faltas_17 = np.arange(0, 65, 2)
intervalo_media_17 = np.arange(0, 11, 1)

dados_heatmap_17, yedges, xedges = np.histogram2d(
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[5]]['media_final'],
  notas_faltas_p3[notas_faltas_p3['nome_componente'] == disciplinas_p3[5]]['numero_total_faltas'],
  bins=[intervalo_media_17, intervalo_faltas_17]
)

heatmap_17 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_17,
    y = intervalo_media_17,
    z = dados_heatmap_17,
    colorscale='Plasma',
    text=dados_heatmap_17,
    texttemplate="%{text}"
))

heatmap_17.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p3[5]} ({total_alunos_p3_5} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_17,range=[0, 64]),
    yaxis=dict(tickvals=intervalo_media_17,range=[0, 10])
)

total_alunos_p4_0 = len(notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[0]])

intervalo_faltas_18 = np.arange(0, 81, 2)
intervalo_media_18 = np.arange(0, 11, 1)

dados_heatmap_18, yedges, xedges = np.histogram2d(
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[0]]['media_final'],
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[0]]['numero_total_faltas'],
  bins=[intervalo_media_18, intervalo_faltas_18]
)

heatmap_18 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_18,
    y = intervalo_media_18,
    z = dados_heatmap_18,
    colorscale='Plasma',
    text=dados_heatmap_18,
    texttemplate="%{text}"
))

heatmap_18.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p4[0]} ({total_alunos_p4_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_18,range=[0, 80]),
    yaxis=dict(tickvals=intervalo_media_18,range=[0, 10])
)

total_alunos_p4_1 = len(notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[1]])

intervalo_faltas_19 = np.arange(0, 81, 2)
intervalo_media_19 = np.arange(0, 11, 1)

dados_heatmap_19, yedges, xedges = np.histogram2d(
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[1]]['media_final'],
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[1]]['numero_total_faltas'],
  bins=[intervalo_media_19, intervalo_faltas_19]
)

heatmap_19 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_19,
    y = intervalo_media_19,
    z = dados_heatmap_19,
    colorscale='Plasma',
    text=dados_heatmap_19,
    texttemplate="%{text}"
))

heatmap_19.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p4[1]} ({total_alunos_p4_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_19,range=[0, 80]),
    yaxis=dict(tickvals=intervalo_media_19,range=[0, 10])
)

total_alunos_p4_2 = len(notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[2]])

intervalo_faltas_20 = np.arange(0, 53, 2)
intervalo_media_20 = np.arange(0, 11, 1)

dados_heatmap_20, yedges, xedges = np.histogram2d(
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[2]]['media_final'],
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[2]]['numero_total_faltas'],
  bins=[intervalo_media_20, intervalo_faltas_20]
)

heatmap_20 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_20,
    y = intervalo_media_20,
    z = dados_heatmap_20,
    colorscale='Plasma',
    text=dados_heatmap_20,
    texttemplate="%{text}"
))

heatmap_20.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p4[2]} ({total_alunos_p4_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_20,range=[0, 52]),
    yaxis=dict(tickvals=intervalo_media_20,range=[0, 10])
)

total_alunos_p4_3 = len(notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[3]])

intervalo_faltas_21 = np.arange(0, 23, 2)
intervalo_media_21 = np.arange(0, 11, 1)

dados_heatmap_21, yedges, xedges = np.histogram2d(
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[3]]['media_final'],
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[3]]['numero_total_faltas'],
  bins=[intervalo_media_21, intervalo_faltas_21]
)

heatmap_21 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_21,
    y = intervalo_media_21,
    z = dados_heatmap_21,
    colorscale='Plasma',
    text=dados_heatmap_21,
    texttemplate="%{text}"
))

heatmap_21.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p4[3]} ({total_alunos_p4_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_21,range=[0, 22]),
    yaxis=dict(tickvals=intervalo_media_21,range=[0, 10])
)

total_alunos_p4_4 = len(notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[4]])

intervalo_faltas_22 = np.arange(0, 41, 2)
intervalo_media_22 = np.arange(0, 11, 1)

dados_heatmap_22, yedges, xedges = np.histogram2d(
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[4]]['media_final'],
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[4]]['numero_total_faltas'],
  bins=[intervalo_media_22, intervalo_faltas_22]
)

heatmap_22 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_22,
    y = intervalo_media_22,
    z = dados_heatmap_22,
    colorscale='Plasma',
    text=dados_heatmap_22,
    texttemplate="%{text}"
))

heatmap_22.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p4[4]} ({total_alunos_p4_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_22,range=[0, 40]),
    yaxis=dict(tickvals=intervalo_media_22,range=[0, 10])
)

total_alunos_p4_5 = len(notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[5]])

intervalo_faltas_23 = np.arange(0, 37, 2)
intervalo_media_23 = np.arange(0, 11, 1)

dados_heatmap_23, yedges, xedges = np.histogram2d(
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[5]]['media_final'],
  notas_faltas_p4[notas_faltas_p4['nome_componente'] == disciplinas_p4[5]]['numero_total_faltas'],
  bins=[intervalo_media_23, intervalo_faltas_23]
)

heatmap_23 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_23,
    y = intervalo_media_23,
    z = dados_heatmap_23,
    colorscale='Plasma',
    text=dados_heatmap_23,
    texttemplate="%{text}"
))

heatmap_23.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p4[5]} ({total_alunos_p4_5} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_23,range=[0, 36]),
    yaxis=dict(tickvals=intervalo_media_23,range=[0, 10])
)

total_alunos_p5_0 = len(notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[0]])

intervalo_faltas_24 = np.arange(0, 61, 2)
intervalo_media_24 = np.arange(0, 11, 1)

dados_heatmap_24, yedges, xedges = np.histogram2d(
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[0]]['media_final'],
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[0]]['numero_total_faltas'],
  bins=[intervalo_media_24, intervalo_faltas_24]
)

heatmap_24 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_24,
    y = intervalo_media_24,
    z = dados_heatmap_24,
    colorscale='Plasma',
    text=dados_heatmap_24,
    texttemplate="%{text}"
))

heatmap_24.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p5[0]} ({total_alunos_p5_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_24,range=[0, 60]),
    yaxis=dict(tickvals=intervalo_media_24,range=[0, 10])
)

total_alunos_p5_1 = len(notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[1]])

intervalo_faltas_25 = np.arange(0, 73, 2)
intervalo_media_25 = np.arange(0, 11, 1)

dados_heatmap_25, yedges, xedges = np.histogram2d(
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[1]]['media_final'],
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[1]]['numero_total_faltas'],
  bins=[intervalo_media_25, intervalo_faltas_25]
)

heatmap_25 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_25,
    y = intervalo_media_25,
    z = dados_heatmap_25,
    colorscale='Plasma',
    text=dados_heatmap_25,
    texttemplate="%{text}"
))

heatmap_25.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p5[1]} ({total_alunos_p5_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_25,range=[0, 72]),
    yaxis=dict(tickvals=intervalo_media_25,range=[0, 10])
)

total_alunos_p5_2 = len(notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[2]])

intervalo_faltas_26 = np.arange(0, 49, 2)
intervalo_media_26 = np.arange(0, 11, 1)

dados_heatmap_26, yedges, xedges = np.histogram2d(
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[2]]['media_final'],
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[2]]['numero_total_faltas'],
  bins=[intervalo_media_26, intervalo_faltas_26]
)

heatmap_26 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_26,
    y = intervalo_media_26,
    z = dados_heatmap_26,
    colorscale='Plasma',
    text=dados_heatmap_26,
    texttemplate="%{text}"
))

heatmap_26.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p5[2]} ({total_alunos_p5_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_26,range=[0, 48]),
    yaxis=dict(tickvals=intervalo_media_26,range=[0, 10])
)

total_alunos_p5_3 = len(notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[3]])

intervalo_faltas_27 = np.arange(0, 49, 2)
intervalo_media_27 = np.arange(0, 11, 1)

dados_heatmap_27, yedges, xedges = np.histogram2d(
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[3]]['media_final'],
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[3]]['numero_total_faltas'],
  bins=[intervalo_media_27, intervalo_faltas_27]
)

heatmap_27 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_27,
    y = intervalo_media_27,
    z = dados_heatmap_27,
    colorscale='Plasma',
    text=dados_heatmap_27,
    texttemplate="%{text}"
))

heatmap_27.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p5[3]} ({total_alunos_p5_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_27,range=[0, 48]),
    yaxis=dict(tickvals=intervalo_media_27,range=[0, 10])
)

total_alunos_p5_4 = len(notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[4]])

intervalo_faltas_28 = np.arange(0, 61, 2)
intervalo_media_28 = np.arange(0, 11, 1)

dados_heatmap_28, yedges, xedges = np.histogram2d(
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[4]]['media_final'],
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[4]]['numero_total_faltas'],
  bins=[intervalo_media_28, intervalo_faltas_28]
)

heatmap_28 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_28,
    y = intervalo_media_28,
    z = dados_heatmap_28,
    colorscale='Plasma',
    text=dados_heatmap_28,
    texttemplate="%{text}"
))

heatmap_28.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p5[4]} ({total_alunos_p5_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_28,range=[0, 60]),
    yaxis=dict(tickvals=intervalo_media_28,range=[0, 10])
)

total_alunos_p5_5 = len(notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[5]])

intervalo_faltas_29 = np.arange(0, 39, 2)
intervalo_media_29 = np.arange(0, 11, 1)

dados_heatmap_29, yedges, xedges = np.histogram2d(
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[5]]['media_final'],
  notas_faltas_p5[notas_faltas_p5['nome_componente'] == disciplinas_p5[5]]['numero_total_faltas'],
  bins=[intervalo_media_29, intervalo_faltas_29]
)

heatmap_29 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_29,
    y = intervalo_media_29,
    z = dados_heatmap_29,
    colorscale='Plasma',
    text=dados_heatmap_29,
    texttemplate="%{text}"
))

heatmap_29.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p5[5]} ({total_alunos_p5_5} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_29,range=[0, 38]),
    yaxis=dict(tickvals=intervalo_media_29,range=[0, 10])
)

total_alunos_p6_0 = len(notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[0]])

intervalo_faltas_30 = np.arange(0, 75, 2)
intervalo_media_30 = np.arange(0, 11, 1)

dados_heatmap_30, yedges, xedges = np.histogram2d(
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[0]]['media_final'],
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[0]]['numero_total_faltas'],
  bins=[intervalo_media_30, intervalo_faltas_30]
)

heatmap_30 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_30,
    y = intervalo_media_30,
    z = dados_heatmap_30,
    colorscale='Plasma',
    text=dados_heatmap_30,
    texttemplate="%{text}"
))

heatmap_30.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p6[0]} ({total_alunos_p6_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_30,range=[0, 74]),
    yaxis=dict(tickvals=intervalo_media_30,range=[0, 10])
)

total_alunos_p6_1 = len(notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[1]])

intervalo_faltas_31 = np.arange(0, 41, 2)
intervalo_media_31 = np.arange(0, 11, 1)

dados_heatmap_31, yedges, xedges = np.histogram2d(
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[1]]['media_final'],
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[1]]['numero_total_faltas'],
  bins=[intervalo_media_31, intervalo_faltas_31]
)

heatmap_31 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_31,
    y = intervalo_media_31,
    z = dados_heatmap_31,
    colorscale='Plasma',
    text=dados_heatmap_31,
    texttemplate="%{text}"
))

heatmap_31.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p6[1]} ({total_alunos_p6_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_31,range=[0, 40]),
    yaxis=dict(tickvals=intervalo_media_31,range=[0, 10])
)

total_alunos_p6_2 = len(notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[2]])

intervalo_faltas_32 = np.arange(0, 55, 2)
intervalo_media_32 = np.arange(0, 11, 1)

dados_heatmap_32, yedges, xedges = np.histogram2d(
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[2]]['media_final'],
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[2]]['numero_total_faltas'],
  bins=[intervalo_media_32, intervalo_faltas_32]
)

heatmap_32 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_32,
    y = intervalo_media_32,
    z = dados_heatmap_32,
    colorscale='Plasma',
    text=dados_heatmap_32,
    texttemplate="%{text}"
))

heatmap_32.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p6[2]} ({total_alunos_p6_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_32,range=[0, 54]),
    yaxis=dict(tickvals=intervalo_media_32,range=[0, 10])
)

total_alunos_p6_3 = len(notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[3]])

intervalo_faltas_33 = np.arange(0, 61, 2)
intervalo_media_33 = np.arange(0, 11, 1)

dados_heatmap_33, yedges, xedges = np.histogram2d(
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[3]]['media_final'],
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[3]]['numero_total_faltas'],
  bins=[intervalo_media_33, intervalo_faltas_33]
)

heatmap_33 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_33,
    y = intervalo_media_33,
    z = dados_heatmap_33,
    colorscale='Plasma',
    text=dados_heatmap_33,
    texttemplate="%{text}"
))

heatmap_33.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p6[3]} ({total_alunos_p6_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_33,range=[0, 60]),
    yaxis=dict(tickvals=intervalo_media_33,range=[0, 10])
)

total_alunos_p6_4 = len(notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[4]])

intervalo_faltas_34 = np.arange(0, 77, 2)
intervalo_media_34 = np.arange(0, 11, 1)

dados_heatmap_34, yedges, xedges = np.histogram2d(
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[4]]['media_final'],
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[4]]['numero_total_faltas'],
  bins=[intervalo_media_34, intervalo_faltas_34]
)

heatmap_34 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_34,
    y = intervalo_media_34,
    z = dados_heatmap_34,
    colorscale='Plasma',
    text=dados_heatmap_34,
    texttemplate="%{text}"
))

heatmap_34.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p6[4]} ({total_alunos_p6_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_34,range=[0, 76]),
    yaxis=dict(tickvals=intervalo_media_34,range=[0, 10])
)

total_alunos_p6_5 = len(notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[5]])

intervalo_faltas_35 = np.arange(0, 77, 2)
intervalo_media_35 = np.arange(0, 11, 1)

dados_heatmap_35, yedges, xedges = np.histogram2d(
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[5]]['media_final'],
  notas_faltas_p6[notas_faltas_p6['nome_componente'] == disciplinas_p6[5]]['numero_total_faltas'],
  bins=[intervalo_media_35, intervalo_faltas_35]
)

heatmap_35 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_35,
    y = intervalo_media_35,
    z = dados_heatmap_35,
    colorscale='Plasma',
    text=dados_heatmap_35,
    texttemplate="%{text}"
))

heatmap_35.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p6[5]} ({total_alunos_p6_5} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_35,range=[0, 76]),
    yaxis=dict(tickvals=intervalo_media_35,range=[0, 10])
)

total_alunos_p7_0 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[0]])

intervalo_faltas_36 = np.arange(0, 71, 2)
intervalo_media_36 = np.arange(0, 11, 1)

dados_heatmap_36, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[0]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[0]]['numero_total_faltas'],
  bins=[intervalo_media_36, intervalo_faltas_36]
)

heatmap_36 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_36,
    y = intervalo_media_36,
    z = dados_heatmap_36,
    colorscale='Plasma',
    text=dados_heatmap_36,
    texttemplate="%{text}"
))

heatmap_36.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[0]} ({total_alunos_p7_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_36,range=[0, 70]),
    yaxis=dict(tickvals=intervalo_media_36,range=[0, 10])
)

total_alunos_p7_1 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[1]])

intervalo_faltas_37 = np.arange(0, 61, 2)
intervalo_media_37 = np.arange(0, 11, 1)

dados_heatmap_37, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[1]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[1]]['numero_total_faltas'],
  bins=[intervalo_media_37, intervalo_faltas_37]
)

heatmap_37 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_37,
    y = intervalo_media_37,
    z = dados_heatmap_37,
    colorscale='Plasma',
    text=dados_heatmap_37,
    texttemplate="%{text}"
))

heatmap_37.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[1]} ({total_alunos_p7_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_37,range=[0, 60]),
    yaxis=dict(tickvals=intervalo_media_37,range=[0, 10])
)

total_alunos_p7_2 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[2]])

intervalo_faltas_38 = np.arange(0, 25, 2)
intervalo_media_38 = np.arange(0, 11, 1)

dados_heatmap_38, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[2]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[2]]['numero_total_faltas'],
  bins=[intervalo_media_38, intervalo_faltas_38]
)

heatmap_38 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_38,
    y = intervalo_media_38,
    z = dados_heatmap_38,
    colorscale='Plasma',
    text=dados_heatmap_38,
    texttemplate="%{text}"
))

heatmap_38.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[2]} ({total_alunos_p7_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_38,range=[0, 24]),
    yaxis=dict(tickvals=intervalo_media_38,range=[0, 10])
)

total_alunos_p7_3 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[3]])

intervalo_faltas_39 = np.arange(0, 31, 2)
intervalo_media_39 = np.arange(0, 11, 1)

dados_heatmap_39, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[3]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[3]]['numero_total_faltas'],
  bins=[intervalo_media_39, intervalo_faltas_39]
)

heatmap_39 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_39,
    y = intervalo_media_39,
    z = dados_heatmap_39,
    colorscale='Plasma',
    text=dados_heatmap_39,
    texttemplate="%{text}"
))

heatmap_39.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[3]} ({total_alunos_p7_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_39,range=[0, 30]),
    yaxis=dict(tickvals=intervalo_media_39,range=[0, 10])
)

total_alunos_p7_4 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[4]])

intervalo_faltas_40 = np.arange(0, 35, 2)
intervalo_media_40 = np.arange(0, 11, 1)

dados_heatmap_40, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[4]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[4]]['numero_total_faltas'],
  bins=[intervalo_media_40, intervalo_faltas_40]
)

heatmap_40 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_40,
    y = intervalo_media_40,
    z = dados_heatmap_40,
    colorscale='Plasma',
    text=dados_heatmap_40,
    texttemplate="%{text}"
))

heatmap_40.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[4]} ({total_alunos_p7_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_40,range=[0, 34]),
    yaxis=dict(tickvals=intervalo_media_40,range=[0, 10])
)

total_alunos_p7_5 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[5]])

intervalo_faltas_41 = np.arange(0, 29, 2)
intervalo_media_41 = np.arange(0, 11, 1)

dados_heatmap_41, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[5]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[5]]['numero_total_faltas'],
  bins=[intervalo_media_41, intervalo_faltas_41]
)

heatmap_41 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_41,
    y = intervalo_media_41,
    z = dados_heatmap_41,
    colorscale='Plasma',
    text=dados_heatmap_41,
    texttemplate="%{text}"
))

heatmap_41.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[5]} ({total_alunos_p7_5} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_41,range=[0, 28]),
    yaxis=dict(tickvals=intervalo_media_41,range=[0, 10])
)

total_alunos_p7_6 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[6]])

intervalo_faltas_42 = np.arange(0, 67, 2)
intervalo_media_42 = np.arange(0, 11, 1)

dados_heatmap_42, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[6]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[6]]['numero_total_faltas'],
  bins=[intervalo_media_42, intervalo_faltas_42]
)

heatmap_42 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_42,
    y = intervalo_media_42,
    z = dados_heatmap_42,
    colorscale='Plasma',
    text=dados_heatmap_42,
    texttemplate="%{text}"
))

heatmap_42.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[6]} ({total_alunos_p7_6} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_42,range=[0, 66]),
    yaxis=dict(tickvals=intervalo_media_42,range=[0, 10])
)

total_alunos_p7_7 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[7]])

intervalo_faltas_43 = np.arange(0, 73, 2)
intervalo_media_43 = np.arange(0, 11, 1)

dados_heatmap_43, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[7]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[7]]['numero_total_faltas'],
  bins=[intervalo_media_43, intervalo_faltas_43]
)

heatmap_43 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_43,
    y = intervalo_media_43,
    z = dados_heatmap_43,
    colorscale='Plasma',
    text=dados_heatmap_43,
    texttemplate="%{text}"
))

heatmap_43.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[7]} ({total_alunos_p7_7} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_43,range=[0, 72]),
    yaxis=dict(tickvals=intervalo_media_43,range=[0, 10])
)

total_alunos_p7_8 = len(notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[8]])

intervalo_faltas_44 = np.arange(0, 69, 2)
intervalo_media_44 = np.arange(0, 11, 1)

dados_heatmap_44, yedges, xedges = np.histogram2d(
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[8]]['media_final'],
  notas_faltas_p7[notas_faltas_p7['nome_componente'] == disciplinas_p7[8]]['numero_total_faltas'],
  bins=[intervalo_media_44, intervalo_faltas_44]
)

heatmap_44 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_44,
    y = intervalo_media_44,
    z = dados_heatmap_44,
    colorscale='Plasma',
    text=dados_heatmap_44,
    texttemplate="%{text}"
))

heatmap_44.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p7[8]} ({total_alunos_p7_8} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_44,range=[0, 68]),
    yaxis=dict(tickvals=intervalo_media_44,range=[0, 10])
)

total_alunos_p8_0 = len(notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[0]])

intervalo_faltas_45 = np.arange(0, 39, 2)
intervalo_media_45 = np.arange(0, 11, 1)

dados_heatmap_45, yedges, xedges = np.histogram2d(
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[0]]['media_final'],
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[0]]['numero_total_faltas'],
  bins=[intervalo_media_45, intervalo_faltas_45]
)

heatmap_45 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_45,
    y = intervalo_media_45,
    z = dados_heatmap_45,
    colorscale='Plasma',
    text=dados_heatmap_45,
    texttemplate="%{text}"
))

heatmap_45.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p8[0]} ({total_alunos_p8_0} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_45,range=[0, 38]),
    yaxis=dict(tickvals=intervalo_media_45,range=[0, 10])
)

total_alunos_p8_2 = len(notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[1]])

intervalo_faltas_46 = np.arange(0, 41, 2)
intervalo_media_46 = np.arange(0, 11, 1)

dados_heatmap_46, yedges, xedges = np.histogram2d(
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[1]]['media_final'],
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[1]]['numero_total_faltas'],
  bins=[intervalo_media_46, intervalo_faltas_46]
)

heatmap_46 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_46,
    y = intervalo_media_46,
    z = dados_heatmap_46,
    colorscale='Plasma',
    text=dados_heatmap_46,
    texttemplate="%{text}"
))

heatmap_46.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p8[1]} ({total_alunos_p8_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_46,range=[0, 40]),
    yaxis=dict(tickvals=intervalo_media_46,range=[0, 10])
)

total_alunos_p8_3 = len(notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[2]])

intervalo_faltas_47 = np.arange(0, 83, 2)
intervalo_media_47 = np.arange(0, 11, 1)

dados_heatmap_47, yedges, xedges = np.histogram2d(
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[2]]['media_final'],
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[2]]['numero_total_faltas'],
  bins=[intervalo_media_47, intervalo_faltas_47]
)

heatmap_47 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_47,
    y = intervalo_media_47,
    z = dados_heatmap_47,
    colorscale='Plasma',
    text=dados_heatmap_47,
    texttemplate="%{text}"
))

heatmap_47.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p8[2]} ({total_alunos_p8_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_47,range=[0, 82]),
    yaxis=dict(tickvals=intervalo_media_47,range=[0, 10])
)

total_alunos_p8_4 = len(notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[3]])

intervalo_faltas_48 = np.arange(0, 69, 2)
intervalo_media_48 = np.arange(0, 11, 1)

dados_heatmap_48, yedges, xedges = np.histogram2d(
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[3]]['media_final'],
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[3]]['numero_total_faltas'],
  bins=[intervalo_media_48, intervalo_faltas_48]
)

heatmap_48 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_48,
    y = intervalo_media_48,
    z = dados_heatmap_48,
    colorscale='Plasma',
    text=dados_heatmap_48,
    texttemplate="%{text}"
))

heatmap_48.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p8[3]} ({total_alunos_p8_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_48,range=[0, 68]),
    yaxis=dict(tickvals=intervalo_media_48,range=[0, 10])
)

total_alunos_p8_5 = len(notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[4]])

intervalo_faltas_49 = np.arange(0, 75, 2)
intervalo_media_49 = np.arange(0, 11, 1)

dados_heatmap_49, yedges, xedges = np.histogram2d(
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[4]]['media_final'],
  notas_faltas_p8[notas_faltas_p8['nome_componente'] == disciplinas_p8[4]]['numero_total_faltas'],
  bins=[intervalo_media_49, intervalo_faltas_49]
)

heatmap_49 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_49,
    y = intervalo_media_49,
    z = dados_heatmap_49,
    colorscale='Plasma',
    text=dados_heatmap_49,
    texttemplate="%{text}"
))

heatmap_49.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p8[4]} ({total_alunos_p8_5} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_49,range=[0, 74]),
    yaxis=dict(tickvals=intervalo_media_49,range=[0, 10])
)

total_alunos_p9_1 = len(notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[0]])

intervalo_faltas_50 = np.arange(0, 57, 2)
intervalo_media_50 = np.arange(0, 11, 1)

dados_heatmap_50, yedges, xedges = np.histogram2d(
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[0]]['media_final'],
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[0]]['numero_total_faltas'],
  bins=[intervalo_media_50, intervalo_faltas_50]
)

heatmap_50 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_50,
    y = intervalo_media_50,
    z = dados_heatmap_50,
    colorscale='Plasma',
    text=dados_heatmap_50,
    texttemplate="%{text}"
))

heatmap_50.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p9[0]} ({total_alunos_p9_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_50,range=[0, 56]),
    yaxis=dict(tickvals=intervalo_media_50,range=[0, 10])
)

total_alunos_p9_2 = len(notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[1]])

intervalo_faltas_51 = np.arange(0, 41, 2)
intervalo_media_51 = np.arange(0, 11, 1)

dados_heatmap_51, yedges, xedges = np.histogram2d(
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[1]]['media_final'],
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[1]]['numero_total_faltas'],
  bins=[intervalo_media_51, intervalo_faltas_51]
)

heatmap_51 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_51,
    y = intervalo_media_51,
    z = dados_heatmap_51,
    colorscale='Plasma',
    text=dados_heatmap_51,
    texttemplate="%{text}"
))

heatmap_51.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p9[1]} ({total_alunos_p9_2} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_51,range=[0, 40]),
    yaxis=dict(tickvals=intervalo_media_51,range=[0, 10])
)

total_alunos_p9_3 = len(notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[2]])

intervalo_faltas_52 = np.arange(0, 21, 2)
intervalo_media_52 = np.arange(0, 11, 1)

dados_heatmap_52, yedges, xedges = np.histogram2d(
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[2]]['media_final'],
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[2]]['numero_total_faltas'],
  bins=[intervalo_media_52, intervalo_faltas_52]
)

heatmap_52 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_52,
    y = intervalo_media_52,
    z = dados_heatmap_52,
    colorscale='Plasma',
    text=dados_heatmap_52,
    texttemplate="%{text}"
))

heatmap_52.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p9[2]} ({total_alunos_p9_3} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_52,range=[0, 20]),
    yaxis=dict(tickvals=intervalo_media_52,range=[0, 10])
)

total_alunos_p9_4 = len(notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[3]])

intervalo_faltas_53 = np.arange(0, 71, 2)
intervalo_media_53 = np.arange(0, 11, 1)

dados_heatmap_53, yedges, xedges = np.histogram2d(
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[3]]['media_final'],
  notas_faltas_p9[notas_faltas_p9['nome_componente'] == disciplinas_p9[3]]['numero_total_faltas'],
  bins=[intervalo_media_53, intervalo_faltas_53]
)

heatmap_53 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_53,
    y = intervalo_media_53,
    z = dados_heatmap_53,
    colorscale='Plasma',
    text=dados_heatmap_53,
    texttemplate="%{text}"
))

heatmap_53.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p9[3]} ({total_alunos_p9_4} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_53,range=[0, 70]),
    yaxis=dict(tickvals=intervalo_media_53,range=[0, 10])
)

total_alunos_p10_1 = len(notas_faltas_p10[notas_faltas_p10['nome_componente'] == disciplinas_p10[0]])

intervalo_faltas_54 = np.arange(0, 29, 2)
intervalo_media_54 = np.arange(0, 11, 1)

dados_heatmap_54, yedges, xedges = np.histogram2d(
  notas_faltas_p10[notas_faltas_p10['nome_componente'] == disciplinas_p10[0]]['media_final'],
  notas_faltas_p10[notas_faltas_p10['nome_componente'] == disciplinas_p10[0]]['numero_total_faltas'],
  bins=[intervalo_media_54, intervalo_faltas_54]
)

heatmap_54 = go.Figure(data=go.Heatmap(
    x = intervalo_faltas_54,
    y = intervalo_media_54,
    z = dados_heatmap_54,
    colorscale='Plasma',
    text=dados_heatmap_54,
    texttemplate="%{text}"
))

heatmap_54.update_layout(
    title=f'Heatmap de Média Final vs. Número Total de Faltas para a disciplina {disciplinas_p10[0]} ({total_alunos_p10_1} discentes analisados)',
    xaxis_title='Número Total de Faltas',
    yaxis_title='Média Final',
    xaxis=dict(tickvals=intervalo_faltas_54,range=[0, 28]),
    yaxis=dict(tickvals=intervalo_media_54,range=[0, 10])
)

st.title("Heatmaps de médias x faltas em disciplinas")

heatmaps_p1 = [heatmap_1, heatmap_2, heatmap_3, heatmap_4, heatmap_5]
heatmaps_p2 = [heatmap_6, heatmap_7, heatmap_8, heatmap_9, heatmap_10, heatmap_11]
heatmaps_p3 = [heatmap_12, heatmap_13, heatmap_14, heatmap_15, heatmap_16, heatmap_17]
heatmaps_p4 = [heatmap_18, heatmap_19, heatmap_20, heatmap_21, heatmap_22, heatmap_23]
heatmaps_p5 = [heatmap_24, heatmap_25, heatmap_26, heatmap_27, heatmap_28, heatmap_29]
heatmaps_p6 = [heatmap_30, heatmap_31, heatmap_32, heatmap_33, heatmap_34, heatmap_35]
heatmaps_p7 = [heatmap_36, heatmap_37, heatmap_38, heatmap_39, heatmap_40, heatmap_41, heatmap_42, heatmap_43, heatmap_44]
heatmaps_p8 = [heatmap_45, heatmap_46, heatmap_47, heatmap_48, heatmap_49]
heatmaps_p9 = [heatmap_50, heatmap_51, heatmap_52, heatmap_53]
heatmaps_p10 = [heatmap_54]

graficos_por_periodo = {
    "Disciplinas do primero período": (heatmaps_p1, "Disciplinas do primero período"),
    "Disciplinas do segundo período": (heatmaps_p2, "Disciplinas do segundo período"),
    "Disciplinas do terceiro período": (heatmaps_p3, "Disciplinas do terceiro período"),
    "Disciplinas do quarto período": (heatmaps_p4, "Disciplinas do quarto período"),
    "Disciplinas do quinto período": (heatmaps_p5, "Disciplinas do quinto período"),
    "Disciplinas do sexto período": (heatmaps_p6, "Disciplinas do sexto período"),
    "Disciplinas do sétimo período": (heatmaps_p7, "Disciplinas do sétimo período"),
    "Disciplinas do oitavo período": (heatmaps_p8, "Disciplinas do oitavo período"),
    "Disciplinas do nono período": (heatmaps_p9, "Disciplinas do nono período"),
    "Disciplinas do décimo período": (heatmaps_p10, "Disciplinas do décimo período")
}

opcoes_periodos = list(graficos_por_periodo.keys())

col1, col2 = st.columns([4, 2], vertical_alignment="center")

with col1:
    st.text("Os gráficos abaixo exibem os heatmaps de médias x faltas dos discentes em disciplinas obrigatórias do curso de direito de um período. No menu de seleção ao lado, você pode selecionar as disciplinas de outro período (de acordo com a recomendação do SIGAA).")

with col2:
    periodo_selecionado = st.selectbox(
        "Selecione um período",
        opcoes_periodos,
        label_visibility="hidden"
    )

st.text("Observação: cada célula do heatmap contém uma quantidade de discentes que obtiveram uma faixa de médias finais estando em uma faixa de faltas na disciplina.")

lista_de_graficos_para_exibir, sub_titulo = graficos_por_periodo[periodo_selecionado]

for grafico in lista_de_graficos_para_exibir:
    st.plotly_chart(grafico, use_container_width=True)