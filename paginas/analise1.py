import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.set_page_config(layout="wide")

matriculas_direito = pd.read_csv("dados/matriculas_direito.csv", sep=';')

cores_grafico_barras_detalhado = {
  'APROVADO': '#3b6dc5',
  'APROVADO POR NOTA': '#a6beea',
  'REPROVADO': '#fadf70',
  'REPROVADO POR FALTAS': '#ffc12c',
  'REPROVADO POR MÉDIA E POR FALTAS': '#fdaa07',
  'REPROVADO POR NOTA E FALTA': '#f2700d',
  'REPROVADO POR NOTA': '#f0800d',
  'TRANCADO': '#ce0026'
}

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

matriculas_p1 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p1)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p2 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p2)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p3 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p3)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p4 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p4)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p5 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p5)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p6 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p6)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p7 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p7)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p8 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p8)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p9 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p9)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')
matriculas_p10 = matriculas_direito[matriculas_direito['nome_componente'].isin(disciplinas_p10)].copy().groupby(['nome_componente', 'descricao']).size().reset_index(name='contagem')

matriculas_p1_pivotada = matriculas_p1.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p2_pivotada = matriculas_p2.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p3_pivotada = matriculas_p3.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p4_pivotada = matriculas_p4.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p5_pivotada = matriculas_p5.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p6_pivotada = matriculas_p6.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p7_pivotada = matriculas_p7.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p8_pivotada = matriculas_p8.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p9_pivotada = matriculas_p9.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)
matriculas_p10_pivotada = matriculas_p10.pivot(index='nome_componente', columns='descricao', values='contagem').fillna(0)

grafico_barras_p1 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p1_pivotada.index,
    y=matriculas_p1_pivotada[col],
    text=matriculas_p1_pivotada[col],
    textposition='outside',
    marker_color=cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p1_pivotada.columns
])

grafico_barras_p1.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do primeiro semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height= 600
)

grafico_barras_p2 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p2_pivotada.index,
    y=matriculas_p2_pivotada[col],
    text=matriculas_p2_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026'),
  ) for col in matriculas_p1_pivotada.columns
])

grafico_barras_p2.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do segundo semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600
)

grafico_barras_p3 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p3_pivotada.index,
    y=matriculas_p3_pivotada[col],
    text=matriculas_p3_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p3_pivotada.columns
])

grafico_barras_p3.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do terceiro semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)

grafico_barras_p4 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p4_pivotada.index,
    y=matriculas_p4_pivotada[col],
    text=matriculas_p4_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p4_pivotada.columns
])

grafico_barras_p4.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do quarto semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)

grafico_barras_p5 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p5_pivotada.index,
    y=matriculas_p5_pivotada[col],
    text=matriculas_p5_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p5_pivotada.columns
])

grafico_barras_p5.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do quinto semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)

grafico_barras_p6 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p6_pivotada.index,
    y=matriculas_p6_pivotada[col],
    text=matriculas_p6_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p6_pivotada.columns
])

grafico_barras_p6.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do sexto semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)

grafico_barras_p7 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p7_pivotada.index,
    y=matriculas_p7_pivotada[col],
    text=matriculas_p7_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p7_pivotada.columns
])

grafico_barras_p7.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do sétimo semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)

grafico_barras_p8 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p8_pivotada.index,
    y=matriculas_p8_pivotada[col],
    text=matriculas_p8_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p8_pivotada.columns
])

grafico_barras_p8.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do oitavo semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)

grafico_barras_p9 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p9_pivotada.index,
    y=matriculas_p9_pivotada[col],
    text=matriculas_p9_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p9_pivotada.columns
])

grafico_barras_p9.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos em disciplinas obrigatórias do nono semestre do curso de Direito, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)

grafico_barras_p10 = go.Figure(data=[
  go.Bar(
    name=col,
    x=matriculas_p10_pivotada.index,
    y=matriculas_p10_pivotada[col],
    text=matriculas_p10_pivotada[col],
    textposition='outside',
    marker_color = cores_grafico_barras_detalhado.get(col, '#ce0026')
  ) for col in matriculas_p10_pivotada.columns
])

grafico_barras_p10.update_layout(
  title='Contagem de aprovações, reprovações e trancamentos na disciplina ATENDIMENTOS - ANDAMENTOS PROCESSUAIS, entre 2011.1 e 2024.2',
  xaxis_title='Disciplina',
  yaxis_title='Número de discentes',
  barmode='group',
  height=600,
)


st.title("Situação geral dos discentes em disciplinas")

graficos_por_periodo = {
    "Disciplinas do primero período": (grafico_barras_p1, "Disciplinas do primero período"),
    "Disciplinas do segundo período": (grafico_barras_p2, "Disciplinas do segundo período"),
    "Disciplinas do terceiro período": (grafico_barras_p3, "Disciplinas do terceiro período"),
    "Disciplinas do quarto período": (grafico_barras_p4, "Disciplinas do quarto período"),
    "Disciplinas do quinto período": (grafico_barras_p5, "Disciplinas do quinto período"),
    "Disciplinas do sexto período": (grafico_barras_p6, "Disciplinas do sexto período"),
    "Disciplinas do sétimo período": (grafico_barras_p7, "Disciplinas do sétimo período"),
    "Disciplinas do oitavo período": (grafico_barras_p8, "Disciplinas do oitavo período"),
    "Disciplinas do nono período": (grafico_barras_p9, "Disciplinas do nono período"),
    "Disciplinas do décimo período": (grafico_barras_p10, "Disciplinas do décimo período"),
}

opcoes_periodos = list(graficos_por_periodo.keys())

col1, col2 = st.columns([4, 2], vertical_alignment="center")

with col1:
    st.text("O gráfico de barras abaixo exibe o total de aprovações, reprovações e trancamentos em disciplinas obrigatórias do curso de direito de um período. No menu de seleção ao lado, você pode selecionar as disciplinas de outro período (de acordo com a recomendação do SIGAA).")

with col2:
    periodo_selecionado = st.selectbox(
        "Selecione um período",
        opcoes_periodos,
        label_visibility="hidden"
    )
grafico_para_exibir, sub_titulo = graficos_por_periodo[periodo_selecionado]

st.plotly_chart(grafico_para_exibir, use_container_width=True)