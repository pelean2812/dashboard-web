import streamlit as st
import pandas as pd
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

matriculas_p1_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p1)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p2_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p2)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p3_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p3)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p4_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p4)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p5_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p5)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p6_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p6)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p7_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p7)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p8_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p8)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p9_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p9)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')
matriculas_p10_media_final_media = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'].isin(disciplinas_p10)].groupby(['nome_componente', 'semestre'])['media_final'].mean().reset_index(name='media_final_media')

matriculas_p1_media_final_media_pivotada = matriculas_p1_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p2_media_final_media_pivotada = matriculas_p2_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p3_media_final_media_pivotada = matriculas_p3_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p4_media_final_media_pivotada = matriculas_p4_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p5_media_final_media_pivotada = matriculas_p5_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p6_media_final_media_pivotada = matriculas_p6_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p7_media_final_media_pivotada = matriculas_p7_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p8_media_final_media_pivotada = matriculas_p8_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p9_media_final_media_pivotada = matriculas_p9_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)
matriculas_p10_media_final_media_pivotada = matriculas_p10_media_final_media.pivot(index='nome_componente', columns='semestre', values='media_final_media').reindex(columns=semestres_ordenados)

evolucao_medias_p1 = go.Figure()

for disciplina in matriculas_p1_media_final_media_pivotada.index:
    evolucao_medias_p1.add_trace(go.Scatter(x=matriculas_p1_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p1_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True, 
                             ))

evolucao_medias_p1.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Primeiro Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category'
    )
)

evolucao_medias_p2 = go.Figure()

for disciplina in matriculas_p2_media_final_media_pivotada.index:
    evolucao_medias_p2.add_trace(go.Scatter(x=matriculas_p2_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p2_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p2.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Segundo Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p3 = go.Figure()

for disciplina in matriculas_p3_media_final_media_pivotada.index:
    evolucao_medias_p3.add_trace(go.Scatter(x=matriculas_p3_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p3_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p3.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Terceiro Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p4 = go.Figure()

for disciplina in matriculas_p4_media_final_media_pivotada.index:
    evolucao_medias_p4.add_trace(go.Scatter(x=matriculas_p4_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p4_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p4.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Quarto Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p5 = go.Figure()

for disciplina in matriculas_p5_media_final_media_pivotada.index:
    evolucao_medias_p5.add_trace(go.Scatter(x=matriculas_p5_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p5_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p5.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Quinto Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p6 = go.Figure()

for disciplina in matriculas_p6_media_final_media_pivotada.index:
    evolucao_medias_p6.add_trace(go.Scatter(x=matriculas_p6_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p6_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p6.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Sexto Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p7 = go.Figure()

for disciplina in matriculas_p7_media_final_media_pivotada.index:
    evolucao_medias_p7.add_trace(go.Scatter(x=matriculas_p7_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p7_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p7.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Sétimo Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p8 = go.Figure()

for disciplina in matriculas_p8_media_final_media_pivotada.index:
    evolucao_medias_p8.add_trace(go.Scatter(x=matriculas_p8_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p8_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p8.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Oitavo Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p9 = go.Figure()

for disciplina in matriculas_p9_media_final_media_pivotada.index:
    evolucao_medias_p9.add_trace(go.Scatter(x=matriculas_p9_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p9_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p9.update_layout(
    title='Evolução Temporal da Média Final Média por Disciplina (Nono Período)',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

evolucao_medias_p10 = go.Figure()

for disciplina in matriculas_p10_media_final_media_pivotada.index:
    evolucao_medias_p10.add_trace(go.Scatter(x=matriculas_p10_media_final_media_pivotada.columns.astype(str),
                             y=matriculas_p10_media_final_media_pivotada.loc[disciplina],
                             mode='lines+markers',
                             name=disciplina,
                             connectgaps=True
                             ))

evolucao_medias_p10.update_layout(
    title='Evolução Temporal da Média Final Média na disciplina ATENDIMENTOS - ANDAMENTOS PROCESSUAIS',
    xaxis_title='Semestre',
    yaxis_title='Média Final Média',
    legend_title='Disciplinas',
    hovermode='x unified',
    xaxis=dict(
        type='category' 
    )
)

st.title("Evolução temporal das médias finais médias")

graficos_por_periodo = {
    "Disciplinas do primero período": (evolucao_medias_p1, "Disciplinas do primero período"),
    "Disciplinas do segundo período": (evolucao_medias_p2, "Disciplinas do segundo período"),
    "Disciplinas do terceiro período": (evolucao_medias_p3, "Disciplinas do terceiro período"),
    "Disciplinas do quarto período": (evolucao_medias_p4, "Disciplinas do quarto período"),
    "Disciplinas do quinto período": (evolucao_medias_p5, "Disciplinas do quinto período"),
    "Disciplinas do sexto período": (evolucao_medias_p6, "Disciplinas do sexto período"),
    "Disciplinas do sétimo período": (evolucao_medias_p7, "Disciplinas do sétimo período"),
    "Disciplinas do oitavo período": (evolucao_medias_p8, "Disciplinas do oitavo período"),
    "Disciplinas do nono período": (evolucao_medias_p9, "Disciplinas do nono período"),
    "Disciplinas do décimo período": (evolucao_medias_p10, "Disciplinas do décimo período"),
}

opcoes_periodos = list(graficos_por_periodo.keys())

col1, col2 = st.columns([4, 2], vertical_alignment="center")

with col1:
    st.text("O gráfico abaixo exibe a evolução temporal da média final média obtida pelos discentes em disciplinas obrigatórias do curso de direito de um período. No menu de seleção ao lado, você pode selecionar as disciplinas de outro período (de acordo com a recomendação do SIGAA).")

with col2:
    periodo_selecionado = st.selectbox(
        "Selecione um período",
        opcoes_periodos,
        label_visibility="hidden"
    )
grafico_para_exibir, sub_titulo = graficos_por_periodo[periodo_selecionado]

st.plotly_chart(grafico_para_exibir, use_container_width=True)