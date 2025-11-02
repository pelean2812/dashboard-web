import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")

matriculas_direito = pd.read_csv("dados/matriculas_direito.csv", sep=';')
matriculas_direito['semestre'] = matriculas_direito['semestre'].astype(str)

df_1 = matriculas_direito[matriculas_direito['nome_componente'] == 'METODOLOGIA DA PESQUISA I'].copy()
contagem_semestre_descricao_1 = df_1.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_1['semestre'] = pd.Categorical(contagem_semestre_descricao_1['semestre'])
contagem_semestre_descricao_1 = contagem_semestre_descricao_1.sort_values('semestre')

fig_1 = px.line(
    contagem_semestre_descricao_1,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina METODOLOGIA DA PESQUISA I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_2 = matriculas_direito[matriculas_direito['nome_componente'] == 'CIENCIA POLITICA I'].copy()
contagem_semestre_descricao_2 = df_2.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_2['semestre'] = pd.Categorical(contagem_semestre_descricao_2['semestre'])
contagem_semestre_descricao_2 = contagem_semestre_descricao_2.sort_values('semestre')

fig_2 = px.line(
    contagem_semestre_descricao_2,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina CIENCIA POLITICA I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_3 = matriculas_direito[matriculas_direito['nome_componente'] == 'SOCIOLOGIA E ANTROPOLOGIA GERAL'].copy()
contagem_semestre_descricao_3 = df_3.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_3['semestre'] = pd.Categorical(contagem_semestre_descricao_3['semestre'])
contagem_semestre_descricao_3 = contagem_semestre_descricao_3.sort_values('semestre')

fig_3 = px.line(
    contagem_semestre_descricao_3,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina SOCIOLOGIA E ANTROPOLOGIA GERAL (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_4 = matriculas_direito[matriculas_direito['nome_componente'] == 'INTRODUCAO AO ESTUDO DO DIREITO'].copy()
contagem_semestre_descricao_4 = df_4.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_4['semestre'] = pd.Categorical(contagem_semestre_descricao_4['semestre'])
contagem_semestre_descricao_4 = contagem_semestre_descricao_4.sort_values('semestre')

fig_4 = px.line(
    contagem_semestre_descricao_4,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina INTRODUCAO AO ESTUDO DO DIREITO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_5 = matriculas_direito[matriculas_direito['nome_componente'] == 'FILOSOFIA I'].copy()
contagem_semestre_descricao_5 = df_5.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_5['semestre'] = pd.Categorical(contagem_semestre_descricao_5['semestre'])
contagem_semestre_descricao_5 = contagem_semestre_descricao_5.sort_values('semestre')

fig_5 = px.line(
    contagem_semestre_descricao_5,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina FILOSOFIA I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_6 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL I'].copy()
contagem_semestre_descricao_6 = df_6.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_6['semestre'] = pd.Categorical(contagem_semestre_descricao_6['semestre'])
contagem_semestre_descricao_6 = contagem_semestre_descricao_6.sort_values('semestre')

fig_6 = px.line(
    contagem_semestre_descricao_6,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_7 = matriculas_direito[matriculas_direito['nome_componente'] == 'HISTORIA DO DIREITO'].copy()
contagem_semestre_descricao_7 = df_7.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_7['semestre'] = pd.Categorical(contagem_semestre_descricao_7['semestre'])
contagem_semestre_descricao_7 = contagem_semestre_descricao_7.sort_values('semestre')

fig_7 = px.line(
    contagem_semestre_descricao_7,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina HISTORIA DO DIREITO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_8 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CONSTITUCIONAL I'].copy()
contagem_semestre_descricao_8 = df_8.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_8['semestre'] = pd.Categorical(contagem_semestre_descricao_8['semestre'])
contagem_semestre_descricao_8 = contagem_semestre_descricao_8.sort_values('semestre')

fig_8 = px.line(
    contagem_semestre_descricao_8,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CONSTITUCIONAL I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_9 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PENAL I'].copy()
contagem_semestre_descricao_9 = df_9.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_9['semestre'] = pd.Categorical(contagem_semestre_descricao_9['semestre'])
contagem_semestre_descricao_9 = contagem_semestre_descricao_9.sort_values('semestre')

fig_9 = px.line(
    contagem_semestre_descricao_9,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PENAL I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_10 = matriculas_direito[matriculas_direito['nome_componente'] == 'ECONOMIA POLITICA'].copy()
contagem_semestre_descricao_10 = df_10.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_10['semestre'] = pd.Categorical(contagem_semestre_descricao_10['semestre'])
contagem_semestre_descricao_10 = contagem_semestre_descricao_10.sort_values('semestre')

fig_10 = px.line(
    contagem_semestre_descricao_10,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina ECONOMIA POLITICA (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_11 = matriculas_direito[matriculas_direito['nome_componente'] == 'PSICOLOGIA APLICADA AO DIREITO'].copy()
contagem_semestre_descricao_11 = df_11.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_11['semestre'] = pd.Categorical(contagem_semestre_descricao_11['semestre'])
contagem_semestre_descricao_11 = contagem_semestre_descricao_11.sort_values('semestre')

fig_11 = px.line(
    contagem_semestre_descricao_11,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina PSICOLOGIA APLICADA AO DIREITO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_12 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL II'].copy()
contagem_semestre_descricao_12 = df_12.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_12['semestre'] = pd.Categorical(contagem_semestre_descricao_12['semestre'])
contagem_semestre_descricao_12 = contagem_semestre_descricao_12.sort_values('semestre')

fig_12 = px.line(
    contagem_semestre_descricao_12,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_13 = matriculas_direito[matriculas_direito['nome_componente'] == 'FILOSOFIA DO DIREITO'].copy()
contagem_semestre_descricao_13 = df_13.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_13['semestre'] = pd.Categorical(contagem_semestre_descricao_13['semestre'])
contagem_semestre_descricao_13 = contagem_semestre_descricao_13.sort_values('semestre')

fig_13 = px.line(
    contagem_semestre_descricao_13,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina FILOSOFIA DO DIREITO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_14 = matriculas_direito[matriculas_direito['nome_componente'] == 'TEORIA GERAL DO PROCESSO'].copy()
contagem_semestre_descricao_14 = df_14.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_14['semestre'] = pd.Categorical(contagem_semestre_descricao_14['semestre'])
contagem_semestre_descricao_14 = contagem_semestre_descricao_14.sort_values('semestre')

fig_14 = px.line(
    contagem_semestre_descricao_14,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina TEORIA GERAL DO PROCESSO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_15 = matriculas_direito[matriculas_direito['nome_componente'] == 'HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO'].copy()
contagem_semestre_descricao_15 = df_15.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_15['semestre'] = pd.Categorical(contagem_semestre_descricao_15['semestre'])
contagem_semestre_descricao_15 = contagem_semestre_descricao_15.sort_values('semestre')

fig_15 = px.line(
    contagem_semestre_descricao_15,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_16 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CONSTITUCIONAL II'].copy()
contagem_semestre_descricao_16 = df_16.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_16['semestre'] = pd.Categorical(contagem_semestre_descricao_16['semestre'])
contagem_semestre_descricao_16 = contagem_semestre_descricao_16.sort_values('semestre')

fig_16 = px.line(
    contagem_semestre_descricao_16,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CONSTITUCIONAL II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_17 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PENAL II'].copy()
contagem_semestre_descricao_17 = df_17.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_17['semestre'] = pd.Categorical(contagem_semestre_descricao_17['semestre'])
contagem_semestre_descricao_17 = contagem_semestre_descricao_17.sort_values('semestre')

fig_17 = px.line(
    contagem_semestre_descricao_17,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PENAL II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_18 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL III'].copy()
contagem_semestre_descricao_18 = df_18.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_18['semestre'] = pd.Categorical(contagem_semestre_descricao_18['semestre'])
contagem_semestre_descricao_18 = contagem_semestre_descricao_18.sort_values('semestre')

fig_18 = px.line(
    contagem_semestre_descricao_18,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL III (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_19 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO EMPRESARIAL I'].copy()
contagem_semestre_descricao_19 = df_19.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_19['semestre'] = pd.Categorical(contagem_semestre_descricao_19['semestre'])
contagem_semestre_descricao_19 = contagem_semestre_descricao_19.sort_values('semestre')

fig_19 = px.line(
    contagem_semestre_descricao_19,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO EMPRESARIAL I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_20 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO INTERNACIONAL PUBLICO'].copy()
contagem_semestre_descricao_20 = df_20.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_20['semestre'] = pd.Categorical(contagem_semestre_descricao_20['semestre'])
contagem_semestre_descricao_20 = contagem_semestre_descricao_20.sort_values('semestre')

fig_20 = px.line(
    contagem_semestre_descricao_20,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO INTERNACIONAL PUBLICO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_21 = matriculas_direito[matriculas_direito['nome_componente'] == 'SOCIOLOGIA JURIDICA'].copy()
contagem_semestre_descricao_21 = df_21.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_21['semestre'] = pd.Categorical(contagem_semestre_descricao_21['semestre'])
contagem_semestre_descricao_21 = contagem_semestre_descricao_21.sort_values('semestre')

fig_21 = px.line(
    contagem_semestre_descricao_21,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina SOCIOLOGIA JURIDICA (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_22 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PENAL III'].copy()
contagem_semestre_descricao_22 = df_22.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_22['semestre'] = pd.Categorical(contagem_semestre_descricao_22['semestre'])
contagem_semestre_descricao_22 = contagem_semestre_descricao_22.sort_values('semestre')

fig_22 = px.line(
    contagem_semestre_descricao_22,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PENAL III (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_23 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL CIVIL I'].copy()
contagem_semestre_descricao_23 = df_23.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_23['semestre'] = pd.Categorical(contagem_semestre_descricao_23['semestre'])
contagem_semestre_descricao_23 = contagem_semestre_descricao_23.sort_values('semestre')

fig_23 = px.line(
    contagem_semestre_descricao_23,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL CIVIL I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_24 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL IV'].copy()
contagem_semestre_descricao_24 = df_24.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_24['semestre'] = pd.Categorical(contagem_semestre_descricao_24['semestre'])
contagem_semestre_descricao_24 = contagem_semestre_descricao_24.sort_values('semestre')

fig_24 = px.line(
    contagem_semestre_descricao_24,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL IV (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_25 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO EMPRESARIAL II'].copy()
contagem_semestre_descricao_25 = df_25.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_25['semestre'] = pd.Categorical(contagem_semestre_descricao_25['semestre'])
contagem_semestre_descricao_25 = contagem_semestre_descricao_25.sort_values('semestre')

fig_25 = px.line(
    contagem_semestre_descricao_25,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO EMPRESARIAL II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_26 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO ADMINISTRATIVO I'].copy()
contagem_semestre_descricao_26 = df_26.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_26['semestre'] = pd.Categorical(contagem_semestre_descricao_26['semestre'])
contagem_semestre_descricao_26 = contagem_semestre_descricao_26.sort_values('semestre')

fig_26 = px.line(
    contagem_semestre_descricao_26,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO ADMINISTRATIVO I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_27 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PENAL IV'].copy()
contagem_semestre_descricao_27 = df_27.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_27['semestre'] = pd.Categorical(contagem_semestre_descricao_27['semestre'])
contagem_semestre_descricao_27 = contagem_semestre_descricao_27.sort_values('semestre')

fig_27 = px.line(
    contagem_semestre_descricao_27,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PENAL IV (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_28 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL CIVIL II'].copy()
contagem_semestre_descricao_28 = df_28.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_28['semestre'] = pd.Categorical(contagem_semestre_descricao_28['semestre'])
contagem_semestre_descricao_28 = contagem_semestre_descricao_28.sort_values('semestre')

fig_28 = px.line(
    contagem_semestre_descricao_28,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL CIVIL II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_29 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITOS HUMANOS FUNDAMENTAIS'].copy()
contagem_semestre_descricao_29 = df_29.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_29['semestre'] = pd.Categorical(contagem_semestre_descricao_29['semestre'])
contagem_semestre_descricao_29 = contagem_semestre_descricao_29.sort_values('semestre')

fig_29 = px.line(
    contagem_semestre_descricao_29,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITOS HUMANOS FUNDAMENTAIS (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_30 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL V'].copy()
contagem_semestre_descricao_30 = df_30.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_30['semestre'] = pd.Categorical(contagem_semestre_descricao_30['semestre'])
contagem_semestre_descricao_30 = contagem_semestre_descricao_30.sort_values('semestre')

fig_30 = px.line(
    contagem_semestre_descricao_30,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL V (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_31 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO EMPRESARIAL III'].copy()
contagem_semestre_descricao_31 = df_31.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_31['semestre'] = pd.Categorical(contagem_semestre_descricao_31['semestre'])
contagem_semestre_descricao_31 = contagem_semestre_descricao_31.sort_values('semestre')

fig_31 = px.line(
    contagem_semestre_descricao_31,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO EMPRESARIAL III (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_32 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO ADMINISTRATIVO II'].copy()
contagem_semestre_descricao_32 = df_32.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_32['semestre'] = pd.Categorical(contagem_semestre_descricao_32['semestre'])
contagem_semestre_descricao_32 = contagem_semestre_descricao_32.sort_values('semestre')

fig_32 = px.line(
    contagem_semestre_descricao_32,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO ADMINISTRATIVO II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_33 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL CIVIL III'].copy()
contagem_semestre_descricao_33 = df_33.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_33['semestre'] = pd.Categorical(contagem_semestre_descricao_33['semestre'])
contagem_semestre_descricao_33 = contagem_semestre_descricao_33.sort_values('semestre')

fig_33 = px.line(
    contagem_semestre_descricao_33,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL CIVIL III (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_34 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL PENAL I'].copy()
contagem_semestre_descricao_34 = df_34.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_34['semestre'] = pd.Categorical(contagem_semestre_descricao_34['semestre'])
contagem_semestre_descricao_34 = contagem_semestre_descricao_34.sort_values('semestre')

fig_34 = px.line(
    contagem_semestre_descricao_34,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL PENAL I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_35 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO DAS RELACOES DE CONSUMO'].copy()
contagem_semestre_descricao_35 = df_35.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_35['semestre'] = pd.Categorical(contagem_semestre_descricao_35['semestre'])
contagem_semestre_descricao_35 = contagem_semestre_descricao_35.sort_values('semestre')

fig_35 = px.line(
    contagem_semestre_descricao_35,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO DAS RELACOES DE CONSUMO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_36 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL VI'].copy()
contagem_semestre_descricao_36 = df_36.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_36['semestre'] = pd.Categorical(contagem_semestre_descricao_36['semestre'])
contagem_semestre_descricao_36 = contagem_semestre_descricao_36.sort_values('semestre')

fig_36 = px.line(
    contagem_semestre_descricao_36,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL VI (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_37 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO DO TRABALHO I'].copy()
contagem_semestre_descricao_37 = df_37.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_37['semestre'] = pd.Categorical(contagem_semestre_descricao_37['semestre'])
contagem_semestre_descricao_37 = contagem_semestre_descricao_37.sort_values('semestre')

fig_37 = px.line(
    contagem_semestre_descricao_37,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO DO TRABALHO I (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)
df_38 = matriculas_direito[matriculas_direito['nome_componente'] == 'AUTOCOMPOSICAO DE CONFLITOS: NEGOCIACAO, CONCILIACAO E MEDIACAO'].copy()
contagem_semestre_descricao_38 = df_38.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_38['semestre'] = pd.Categorical(contagem_semestre_descricao_38['semestre'])
contagem_semestre_descricao_38 = contagem_semestre_descricao_38.sort_values('semestre')

fig_38 = px.line(
    contagem_semestre_descricao_38,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina AUTOCOMPOSICAO DE CONFLITOS: NEGOCIACAO, CONCILIACAO E MEDIACAO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_39 = matriculas_direito[matriculas_direito['nome_componente'] == 'CARREIRAS JURIDICAS'].copy()
contagem_semestre_descricao_39 = df_39.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_39['semestre'] = pd.Categorical(contagem_semestre_descricao_39['semestre'])
contagem_semestre_descricao_39 = contagem_semestre_descricao_39.sort_values('semestre')

fig_39 = px.line(
    contagem_semestre_descricao_39,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina CARREIRAS JURIDICAS (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_40 = matriculas_direito[matriculas_direito['nome_componente'] == 'PECAS JURIDICAS II (EXTRAJUDICIAIS)'].copy()
contagem_semestre_descricao_40 = df_40.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_40['semestre'] = pd.Categorical(contagem_semestre_descricao_40['semestre'])
contagem_semestre_descricao_40 = contagem_semestre_descricao_40.sort_values('semestre')

fig_40 = px.line(
    contagem_semestre_descricao_40,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina PECAS JURIDICAS II (EXTRAJUDICIAIS) (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_41 = matriculas_direito[matriculas_direito['nome_componente'] == 'PECAS JURIDICAS I (JUDICIAIS)'].copy()
contagem_semestre_descricao_41 = df_41.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_41['semestre'] = pd.Categorical(contagem_semestre_descricao_41['semestre'])
contagem_semestre_descricao_41 = contagem_semestre_descricao_41.sort_values('semestre')

fig_41 = px.line(
    contagem_semestre_descricao_41,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina PECAS JURIDICAS I (JUDICIAIS) (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_42 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL CIVIL IV'].copy()
contagem_semestre_descricao_42 = df_42.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_42['semestre'] = pd.Categorical(contagem_semestre_descricao_42['semestre'])
contagem_semestre_descricao_42 = contagem_semestre_descricao_42.sort_values('semestre')

fig_42 = px.line(
    contagem_semestre_descricao_42,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL CIVIL IV (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_43 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL PENAL II'].copy()
contagem_semestre_descricao_43 = df_43.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_43['semestre'] = pd.Categorical(contagem_semestre_descricao_43['semestre'])
contagem_semestre_descricao_43 = contagem_semestre_descricao_43.sort_values('semestre')

fig_43 = px.line(
    contagem_semestre_descricao_43,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL PENAL II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_44 = matriculas_direito[matriculas_direito['nome_componente'] == 'ETICA GERAL E PROFISSIONAL'].copy()
contagem_semestre_descricao_44 = df_44.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_44['semestre'] = pd.Categorical(contagem_semestre_descricao_44['semestre'])
contagem_semestre_descricao_44 = contagem_semestre_descricao_44.sort_values('semestre')

fig_44 = px.line(
    contagem_semestre_descricao_44,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina ETICA GERAL E PROFISSIONAL (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_45 = matriculas_direito[matriculas_direito['nome_componente'] == 'METODOLOGIA DA PESQUISA II'].copy()
contagem_semestre_descricao_45 = df_45.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_45['semestre'] = pd.Categorical(contagem_semestre_descricao_45['semestre'])
contagem_semestre_descricao_45 = contagem_semestre_descricao_45.sort_values('semestre')

fig_45 = px.line(
    contagem_semestre_descricao_45,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina METODOLOGIA DA PESQUISA II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_46 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL VII'].copy()
contagem_semestre_descricao_46 = df_46.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_46['semestre'] = pd.Categorical(contagem_semestre_descricao_46['semestre'])
contagem_semestre_descricao_46 = contagem_semestre_descricao_46.sort_values('semestre')

fig_46 = px.line(
    contagem_semestre_descricao_46,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL VII (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_47 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO DO TRABALHO II'].copy()
contagem_semestre_descricao_47 = df_47.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_47['semestre'] = pd.Categorical(contagem_semestre_descricao_47['semestre'])
contagem_semestre_descricao_47 = contagem_semestre_descricao_47.sort_values('semestre')

fig_47 = px.line(
    contagem_semestre_descricao_47,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO DO TRABALHO II (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_48 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO TRIBUTARIO'].copy()
contagem_semestre_descricao_48 = df_48.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_48['semestre'] = pd.Categorical(contagem_semestre_descricao_48['semestre'])
contagem_semestre_descricao_48 = contagem_semestre_descricao_48.sort_values('semestre')

fig_48 = px.line(
    contagem_semestre_descricao_48,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO TRIBUTARIO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_49 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL COLETIVO'].copy()
contagem_semestre_descricao_49 = df_49.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_49['semestre'] = pd.Categorical(contagem_semestre_descricao_49['semestre'])
contagem_semestre_descricao_49 = contagem_semestre_descricao_49.sort_values('semestre')

fig_49 = px.line(
    contagem_semestre_descricao_49,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL COLETIVO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_50 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO CIVIL VIII'].copy()
contagem_semestre_descricao_50 = df_50.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_50['semestre'] = pd.Categorical(contagem_semestre_descricao_50['semestre'])
contagem_semestre_descricao_50 = contagem_semestre_descricao_50.sort_values('semestre')

fig_50 = px.line(
    contagem_semestre_descricao_50,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO CIVIL VIII (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_51 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO DO TRABALHO III'].copy()
contagem_semestre_descricao_51 = df_51.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_51['semestre'] = pd.Categorical(contagem_semestre_descricao_51['semestre'])
contagem_semestre_descricao_51 = contagem_semestre_descricao_51.sort_values('semestre')

fig_51 = px.line(
    contagem_semestre_descricao_51,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO DO TRABALHO III (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_52 = matriculas_direito[matriculas_direito['nome_componente'] == 'PRATICA JURIDICA III - ATENDIMENTOS'].copy()
contagem_semestre_descricao_52 = df_52.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_52['semestre'] = pd.Categorical(contagem_semestre_descricao_52['semestre'])
contagem_semestre_descricao_52 = contagem_semestre_descricao_52.sort_values('semestre')

fig_52 = px.line(
    contagem_semestre_descricao_52,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina PRATICA JURIDICA III - ATENDIMENTOS (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_53 = matriculas_direito[matriculas_direito['nome_componente'] == 'DIREITO PROCESSUAL DO TRABALHO'].copy()
contagem_semestre_descricao_53 = df_53.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_53['semestre'] = pd.Categorical(contagem_semestre_descricao_53['semestre'])
contagem_semestre_descricao_53 = contagem_semestre_descricao_53.sort_values('semestre')

fig_53 = px.line(
    contagem_semestre_descricao_53,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina DIREITO PROCESSUAL DO TRABALHO (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

df_54 = matriculas_direito[matriculas_direito['nome_componente'] == 'ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'].copy()
contagem_semestre_descricao_54 = df_54.groupby(['semestre', 'descricao']).size().reset_index(name='quantidade')
contagem_semestre_descricao_54['semestre'] = pd.Categorical(contagem_semestre_descricao_54['semestre'])
contagem_semestre_descricao_54 = contagem_semestre_descricao_54.sort_values('semestre')

fig_54 = px.line(
    contagem_semestre_descricao_54,
    x='semestre',
    y='quantidade',
    color='descricao',
    title='Evolução temporal de aprovações, reprovações e trancamentos da disciplina ATENDIMENTOS - ANDAMENTOS PROCESSUAIS (detalhada)',
    labels={'semestre': 'Semestre', 'quantidade': 'Quantidade', 'descricao': 'Situação'},
    markers=True
)

fig_1.update_layout(xaxis=dict(type='category'))
fig_2.update_layout(xaxis=dict(type='category'))
fig_3.update_layout(xaxis=dict(type='category'))
fig_4.update_layout(xaxis=dict(type='category'))
fig_5.update_layout(xaxis=dict(type='category'))
fig_6.update_layout(xaxis=dict(type='category'))
fig_7.update_layout(xaxis=dict(type='category'))
fig_8.update_layout(xaxis=dict(type='category'))
fig_9.update_layout(xaxis=dict(type='category'))
fig_10.update_layout(xaxis=dict(type='category'))
fig_11.update_layout(xaxis=dict(type='category'))
fig_12.update_layout(xaxis=dict(type='category'))
fig_13.update_layout(xaxis=dict(type='category'))
fig_14.update_layout(xaxis=dict(type='category'))
fig_15.update_layout(xaxis=dict(type='category'))
fig_16.update_layout(xaxis=dict(type='category'))
fig_17.update_layout(xaxis=dict(type='category'))
fig_18.update_layout(xaxis=dict(type='category'))
fig_19.update_layout(xaxis=dict(type='category'))
fig_20.update_layout(xaxis=dict(type='category'))
fig_21.update_layout(xaxis=dict(type='category'))
fig_22.update_layout(xaxis=dict(type='category'))
fig_23.update_layout(xaxis=dict(type='category'))
fig_24.update_layout(xaxis=dict(type='category'))
fig_25.update_layout(xaxis=dict(type='category'))
fig_26.update_layout(xaxis=dict(type='category'))
fig_27.update_layout(xaxis=dict(type='category'))
fig_28.update_layout(xaxis=dict(type='category'))
fig_29.update_layout(xaxis=dict(type='category'))
fig_30.update_layout(xaxis=dict(type='category'))
fig_31.update_layout(xaxis=dict(type='category'))
fig_32.update_layout(xaxis=dict(type='category'))
fig_33.update_layout(xaxis=dict(type='category'))
fig_34.update_layout(xaxis=dict(type='category'))
fig_35.update_layout(xaxis=dict(type='category'))
fig_36.update_layout(xaxis=dict(type='category'))
fig_37.update_layout(xaxis=dict(type='category'))
fig_38.update_layout(xaxis=dict(type='category'))
fig_39.update_layout(xaxis=dict(type='category'))
fig_40.update_layout(xaxis=dict(type='category'))
fig_41.update_layout(xaxis=dict(type='category'))
fig_42.update_layout(xaxis=dict(type='category'))
fig_43.update_layout(xaxis=dict(type='category'))
fig_44.update_layout(xaxis=dict(type='category'))
fig_45.update_layout(xaxis=dict(type='category'))
fig_46.update_layout(xaxis=dict(type='category'))
fig_47.update_layout(xaxis=dict(type='category'))
fig_48.update_layout(xaxis=dict(type='category'))
fig_49.update_layout(xaxis=dict(type='category'))
fig_50.update_layout(xaxis=dict(type='category'))
fig_51.update_layout(xaxis=dict(type='category'))
fig_52.update_layout(xaxis=dict(type='category'))
fig_53.update_layout(xaxis=dict(type='category'))
fig_54.update_layout(xaxis=dict(type='category'))

st.title("Evolução temporal das situações dos discentes em disciplinas")

disciplinas_p1 = [fig_1, fig_2, fig_3, fig_4, fig_5]
disciplinas_p2 = [fig_6, fig_7, fig_8, fig_9, fig_10, fig_11]
disciplinas_p3 = [fig_12, fig_13, fig_14, fig_15, fig_16, fig_17]
disciplinas_p4 = [fig_18, fig_19, fig_20, fig_21, fig_22, fig_23]
disciplinas_p5 = [fig_24, fig_25, fig_26, fig_27, fig_28, fig_29]
disciplinas_p6 = [fig_30, fig_31, fig_32, fig_33, fig_34, fig_35]
disciplinas_p7 = [fig_36, fig_37, fig_38, fig_39, fig_40, fig_41, fig_42, fig_43, fig_44]
disciplinas_p8 = [fig_45, fig_46, fig_47, fig_48, fig_49]
disciplinas_p9 = [fig_50, fig_51, fig_52, fig_53]
disciplinas_p10 = [fig_54]

graficos_por_periodo = {
    "Disciplinas do primero período": (disciplinas_p1, "Disciplinas do primero período"),
    "Disciplinas do segundo período": (disciplinas_p2, "Disciplinas do segundo período"),
    "Disciplinas do terceiro período": (disciplinas_p3, "Disciplinas do terceiro período"),
    "Disciplinas do quarto período": (disciplinas_p4, "Disciplinas do quarto período"),
    "Disciplinas do quinto período": (disciplinas_p5, "Disciplinas do quinto período"),
    "Disciplinas do sexto período": (disciplinas_p6, "Disciplinas do sexto período"),
    "Disciplinas do sétimo período": (disciplinas_p7, "Disciplinas do sétimo período"),
    "Disciplinas do oitavo período": (disciplinas_p8, "Disciplinas do oitavo período"),
    "Disciplinas do nono período": (disciplinas_p9, "Disciplinas do nono período"),
    "Disciplinas do décimo período": (disciplinas_p10, "Disciplinas do décimo período")
}

opcoes_periodos = list(graficos_por_periodo.keys())

col1, col2 = st.columns([4, 2], vertical_alignment="center")

with col1:
    st.text("Os gráficos abaixo exibem a evolução temporal das situações dos discentes em disciplinas obrigatórias do curso de direito de um período. No menu de seleção ao lado, você pode selecionar as disciplinas de outro período (de acordo com a recomendação do SIGAA).")

with col2:
    periodo_selecionado = st.selectbox(
        "Selecione um período",
        opcoes_periodos,
        label_visibility="hidden"
    )

lista_de_graficos_para_exibir, sub_titulo = graficos_por_periodo[periodo_selecionado]

for grafico in lista_de_graficos_para_exibir:
    st.plotly_chart(grafico, use_container_width=True)