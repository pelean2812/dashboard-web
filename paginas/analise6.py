import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")

matriculas_direito = pd.read_csv("dados/matriculas_direito.csv", sep=';')
matriculas_direito['semestre'] = matriculas_direito['semestre'].astype(str)
matriculas_direito_sem_trancamento = matriculas_direito[matriculas_direito['descricao'] != 'TRANCADO'].copy()

df_1 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'METODOLOGIA DA PESQUISA I'].copy()

fig_1 = px.box(
    df_1,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina METODOLOGIA DA PESQUISA I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_2 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'CIENCIA POLITICA I'].copy()

fig_2 = px.box(
    df_2,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina CIENCIA POLITICA I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_3 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'SOCIOLOGIA E ANTROPOLOGIA GERAL'].copy()

fig_3 = px.box(
    df_3,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina SOCIOLOGIA E ANTROPOLOGIA GERAL (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)


df_4 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'INTRODUCAO AO ESTUDO DO DIREITO'].copy()

fig_4 = px.box(
    df_4,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina INTRODUCAO AO ESTUDO DO DIREITO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_5 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'FILOSOFIA I'].copy()

fig_5 = px.box(
    df_5,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina FILOSOFIA I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_6 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL I'].copy()

fig_6 = px.box(
    df_6,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_7 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'HISTORIA DO DIREITO'].copy()

fig_7 = px.box(
    df_7,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina HISTORIA DO DIREITO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_8 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CONSTITUCIONAL I'].copy()

fig_8 = px.box(
    df_8,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CONSTITUCIONAL I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_9 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PENAL I'].copy()

fig_9 = px.box(
    df_9,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PENAL I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_10 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'ECONOMIA POLITICA'].copy()

fig_10 = px.box(
    df_10,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina ECONOMIA POLITICA (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_11 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'PSICOLOGIA APLICADA AO DIREITO'].copy()

fig_11 = px.box(
    df_11,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina PSICOLOGIA APLICADA AO DIREITO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_12 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL II'].copy()

fig_12 = px.box(
    df_12,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_13 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'FILOSOFIA DO DIREITO'].copy()

fig_13 = px.box(
    df_13,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina FILOSOFIA DO DIREITO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_14 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'TEORIA GERAL DO PROCESSO'].copy()

fig_14 = px.box(
    df_14,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina TEORIA GERAL DO PROCESSO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_15 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO'].copy()

fig_15 = px.box(
    df_15,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_16 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CONSTITUCIONAL II'].copy()

fig_16 = px.box(
    df_16,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CONSTITUCIONAL II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_17 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PENAL II'].copy()

fig_17 = px.box(
    df_17,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PENAL II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_18 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL III'].copy()

fig_18 = px.box(
    df_18,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL III (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_19 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO EMPRESARIAL I'].copy()

fig_19 = px.box(
    df_19,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO EMPRESARIAL I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_20 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO INTERNACIONAL PUBLICO'].copy()

fig_20 = px.box(
    df_20,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO INTERNACIONAL PUBLICO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_21 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'SOCIOLOGIA JURIDICA'].copy()

fig_21 = px.box(
    df_21,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina SOCIOLOGIA JURIDICA (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_22 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PENAL III'].copy()

fig_22 = px.box(
    df_22,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PENAL III (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_23 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL CIVIL I'].copy()

fig_23 = px.box(
    df_23,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL CIVIL I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_24 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL IV'].copy()

fig_24 = px.box(
    df_24,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL IV (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_25 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO EMPRESARIAL II'].copy()

fig_25 = px.box(
    df_25,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO EMPRESARIAL II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_26 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO ADMINISTRATIVO I'].copy()

fig_26 = px.box(
    df_26,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO ADMINISTRATIVO I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_27 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PENAL IV'].copy()

fig_27 = px.box(
    df_27,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PENAL IV (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_28 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL CIVIL II'].copy()

fig_28 = px.box(
    df_28,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL CIVIL II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_29 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITOS HUMANOS FUNDAMENTAIS'].copy()

fig_29 = px.box(
    df_29,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITOS HUMANOS FUNDAMENTAIS (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_30 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL V'].copy()

fig_30 = px.box(
    df_30,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL V (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_31 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO EMPRESARIAL III'].copy()

fig_31 = px.box(
    df_31,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO EMPRESARIAL III (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_32 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO ADMINISTRATIVO II'].copy()

fig_32 = px.box(
    df_32,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO ADMINISTRATIVO II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_33 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL CIVIL III'].copy()

fig_33 = px.box(
    df_33,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL CIVIL III (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_34 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL PENAL I'].copy()

fig_34 = px.box(
    df_34,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL PENAL I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_35 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO DAS RELACOES DE CONSUMO'].copy()

fig_35 = px.box(
    df_35,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO DAS RELACOES DE CONSUMO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_36 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL VI'].copy()

fig_36 = px.box(
    df_36,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL VI (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_37 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO DO TRABALHO I'].copy()

fig_37 = px.box(
    df_37,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO DO TRABALHO I (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_38 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'AUTOCOMPOSICAO DE CONFLITOS: NEGOCIACAO, CONCILIACAO E MEDIACAO'].copy()

fig_38 = px.box(
    df_38,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina AUTOCOMPOSICAO DE CONFLITOS: NEGOCIACAO, CONCILIACAO E MEDIACAO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_39 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'CARREIRAS JURIDICAS'].copy()

fig_39 = px.box(
    df_39,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina CARREIRAS JURIDICAS (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_40 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'PECAS JURIDICAS II (EXTRAJUDICIAIS)'].copy()

fig_40 = px.box(
    df_40,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina PECAS JURIDICAS II (EXTRAJUDICIAIS) (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_41 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'PECAS JURIDICAS I (JUDICIAIS)'].copy()

fig_41 = px.box(
    df_41,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina PECAS JURIDICAS I (JUDICIAIS) (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_42 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL CIVIL IV'].copy()

fig_42 = px.box(
    df_42,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL CIVIL IV (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_43 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL PENAL II'].copy()

fig_43 = px.box(
    df_43,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL PENAL II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_44 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'ETICA GERAL E PROFISSIONAL'].copy()

fig_44 = px.box(
    df_44,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina ETICA GERAL E PROFISSIONAL (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_45 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'METODOLOGIA DA PESQUISA II'].copy()

fig_45 = px.box(
    df_45,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina METODOLOGIA DA PESQUISA II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_46 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL VII'].copy()

fig_46 = px.box(
    df_46,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL VII (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_47 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO DO TRABALHO II'].copy()

fig_47 = px.box(
    df_47,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO DO TRABALHO II (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_48 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO TRIBUTARIO'].copy()

fig_48 = px.box(
    df_48,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO TRIBUTARIO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_49 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL COLETIVO'].copy()

fig_49 = px.box(
    df_49,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL COLETIVO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_50 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL VIII'].copy()

fig_50 = px.box(
    df_50,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO CIVIL VIII (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_51 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO DO TRABALHO III'].copy()

fig_51 = px.box(
    df_51,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO DO TRABALHO III (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_52 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'PRATICA JURIDICA III - ATENDIMENTOS'].copy()

fig_52 = px.box(
    df_52,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina PRATICA JURIDICA III - ATENDIMENTOS (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_53 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO PROCESSUAL DO TRABALHO'].copy()

fig_53 = px.box(
    df_53,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina DIREITO PROCESSUAL DO TRABALHO (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
)

df_54 = matriculas_direito_sem_trancamento[matriculas_direito_sem_trancamento['nome_componente'] == 'ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'].copy()

fig_54 = px.box(
    df_54,
    y='media_final',
    x='semestre',
    title=f'Distribuição das médias finais por semestre da disciplina ATENDIMENTOS - ANDAMENTOS PROCESSUAIS (Box Plot)',
    labels={'media_final': 'Média Final', 'semestre': 'Semestre'}
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

st.title("Evolução temporal da dispersão da média em disciplinas")

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
    st.text("Os gráficos abaixo exibem a evolução temporal da dispersão das médias dos discentes em disciplinas obrigatórias do curso de direito de um período. No menu de seleção ao lado, você pode selecionar as disciplinas de outro período (de acordo com a recomendação do SIGAA).")

with col2:
    periodo_selecionado = st.selectbox(
        "Selecione um período",
        opcoes_periodos,
        label_visibility="hidden"
    )

lista_de_graficos_para_exibir, sub_titulo = graficos_por_periodo[periodo_selecionado]

for grafico in lista_de_graficos_para_exibir:
    st.plotly_chart(grafico, use_container_width=True)