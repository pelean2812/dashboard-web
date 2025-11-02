import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("Gráfico de coordendas paralelas")

matriculas_direito = pd.read_csv("dados/matriculas_direito.csv", sep=';')
matriculas_direito['semestre'] = matriculas_direito['semestre'].astype(str)
matriculas_direito_sem_trancamento = matriculas_direito[matriculas_direito['descricao'] != 'TRANCADO'].copy()
turma_concluintes_2024_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['semestre'] == '2024.2') & (matriculas_direito_sem_trancamento['nome_componente'] == 'ATENDIMENTOS - ANDAMENTOS PROCESSUAIS')]['discente']

string_disciplinas = 'DIREITO PENAL I|DIREITO PENAL II|DIREITO PENAL III|DIREITO PENAL IV'
medias_direito_penal = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_penal = medias_direito_penal.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_penal = medias_direito_penal.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_penal = medias_direito_penal.dropna()

fig_1 = go.Figure(data=
    go.Parcoords(       
        dimensions = [
            dict(label='DIREITO PENAL I', values=medias_direito_penal['DIREITO PENAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PENAL II', values=medias_direito_penal['DIREITO PENAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PENAL III', values=medias_direito_penal['DIREITO PENAL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PENAL IV', values=medias_direito_penal['DIREITO PENAL IV'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_1.update_layout(
    title=f'Gráfico de coordenadas paralelas para as disciplinas de DIREITO PENAL IV e seus pré-requisitos',
    height=600, 
    margin=dict(l=50, r=50)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV'
medias_direito_civil = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil = medias_direito_civil.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil = medias_direito_civil.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil = medias_direito_civil.dropna()

fig_2 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_civil['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_civil['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL III', values=medias_direito_civil['DIREITO CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL IV', values=medias_direito_civil['DIREITO CIVIL IV'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_2.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL IV e seus pré-requisitos',
    height=600, 
    margin=dict(l=90, r=50)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO INTERNACIONAL PUBLICO'
medias_direito_internacional = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_internacional = medias_direito_internacional.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_internacional = medias_direito_internacional.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_internacional = medias_direito_internacional.dropna()

fig_3 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_internacional['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_internacional['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_internacional['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO INTERNACIONAL PUBLICO', values=medias_direito_internacional['DIREITO INTERNACIONAL PUBLICO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_3.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO INTERNACIONAL PÚBLICO e seus pré-requisitos (possibilidade 1)',
    height=600, 
    margin=dict(l=90, r=90)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO INTERNACIONAL PUBLICO'
medias_direito_internacional_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL III|DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_internacional_2 = medias_direito_internacional_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_internacional_2 = medias_direito_internacional_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_internacional_2 = medias_direito_internacional_2.dropna()

fig_4 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_internacional_2['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_internacional_2['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_internacional_2['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO INTERNACIONAL PUBLICO', values=medias_direito_internacional_2['DIREITO INTERNACIONAL PUBLICO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_4.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO INTERNACIONAL PÚBLICO e seus pré-requisitos (possibilidade 2)',
    height=600, 
    margin=dict(l=90, r=90)
)

string_disciplinas = 'HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO|DIREITO CIVIL I|INTRODUCAO AO ESTUDO DO DIREITO'
medias_hermeneutica = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_hermeneutica = medias_hermeneutica.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_hermeneutica = medias_hermeneutica.pivot(index='discente', columns='nome_componente', values='media_final')
medias_hermeneutica = medias_hermeneutica.dropna()

fig_5 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_hermeneutica['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_hermeneutica['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO', values=medias_hermeneutica['HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_5.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO e seus pré-requisitos',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO EMPRESARIAL I|DIREITO EMPRESARIAL II|DIREITO EMPRESARIAL III'
medias_direito_empresarial = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL III|DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_empresarial = medias_direito_empresarial.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_empresarial = medias_direito_empresarial.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_empresarial = medias_direito_empresarial.dropna()

fig_6 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_empresarial['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_empresarial['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_empresarial['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL I', values=medias_direito_empresarial['DIREITO EMPRESARIAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL II', values=medias_direito_empresarial['DIREITO EMPRESARIAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL III', values=medias_direito_empresarial['DIREITO EMPRESARIAL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_6.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO EMPRESARIAL III e seus pré-requisitos (possibilidade 1)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO EMPRESARIAL I|DIREITO EMPRESARIAL II|DIREITO EMPRESARIAL III'
medias_direito_empresarial_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_empresarial_2 = medias_direito_empresarial_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_empresarial_2 = medias_direito_empresarial_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_empresarial_2 = medias_direito_empresarial_2.dropna()

fig_7 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_empresarial_2['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_empresarial_2['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_empresarial_2['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL I', values=medias_direito_empresarial_2['DIREITO EMPRESARIAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL II', values=medias_direito_empresarial_2['DIREITO EMPRESARIAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL III', values=medias_direito_empresarial_2['DIREITO EMPRESARIAL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_7.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO EMPRESARIAL III e seus pré-requisitos (possibilidade 2)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO ADMINISTRATIVO I|DIREITO ADMINISTRATIVO II'
medias_direito_administrativo = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III|DIREITO ADMINISTRATIVO III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_administrativo = medias_direito_administrativo.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_administrativo = medias_direito_administrativo.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_administrativo = medias_direito_administrativo.dropna()

fig_8 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_administrativo['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_administrativo['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_administrativo['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO ADMINISTRATIVO I', values=medias_direito_administrativo['DIREITO ADMINISTRATIVO I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO ADMINISTRATIVO II', values=medias_direito_administrativo['DIREITO ADMINISTRATIVO II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_8.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO ADMINISTRATIVO II e seus pré-requisitos',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITOS HUMANOS FUNDAMENTAIS'
medias_direitos_humanos = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direitos_humanos = medias_direitos_humanos.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direitos_humanos = medias_direitos_humanos.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direitos_humanos = medias_direitos_humanos.dropna()

fig_9 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direitos_humanos['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direitos_humanos['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direitos_humanos['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITOS HUMANOS FUNDAMENTAIS', values=medias_direitos_humanos['DIREITOS HUMANOS FUNDAMENTAIS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_9.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITOS HUMANOS FUNDAMENTAIS e seus pré-requisitos',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO PROCESSUAL PENAL I|DIREITO PROCESSUAL PENAL II'
medias_direito_processual_penal = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL III|DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_processual_penal = medias_direito_processual_penal.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_processual_penal = medias_direito_processual_penal.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_processual_penal = medias_direito_processual_penal.dropna()

fig_10 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_processual_penal['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_processual_penal['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_processual_penal['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL I', values=medias_direito_processual_penal['DIREITO PROCESSUAL PENAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL II', values=medias_direito_processual_penal['DIREITO PROCESSUAL PENAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_10.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO PROCESSUAL PENAL II e seus pré-requisitos (possibilidade 1)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO PROCESSUAL PENAL I|DIREITO PROCESSUAL PENAL II'
medias_direito_processual_penal_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_processual_penal_2 = medias_direito_processual_penal_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_processual_penal_2 = medias_direito_processual_penal_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_processual_penal_2 = medias_direito_processual_penal_2.dropna()

fig_11 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_processual_penal_2['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_processual_penal_2['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_processual_penal_2['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL I', values=medias_direito_processual_penal_2['DIREITO PROCESSUAL PENAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL II', values=medias_direito_processual_penal_2['DIREITO PROCESSUAL PENAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_11.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO PROCESSUAL PENAL II e seus pré-requisitos (possibilidade 2)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'DIREITO PENAL I|DIREITO PENAL II|DIREITO PROCESSUAL PENAL I|DIREITO PROCESSUAL PENAL II'
medias_direito_processual_penal_3 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO PENAL III|DIREITO PENAL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_processual_penal_3 = medias_direito_processual_penal_3.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_processual_penal_3 = medias_direito_processual_penal_3.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_processual_penal_3 = medias_direito_processual_penal_3.dropna()

fig_12 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='DIREITO PENAL I', values=medias_direito_processual_penal_3['DIREITO PENAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PENAL II', values=medias_direito_processual_penal_3['DIREITO PENAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL I', values=medias_direito_processual_penal_3['DIREITO PROCESSUAL PENAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL II', values=medias_direito_processual_penal_3['DIREITO PROCESSUAL PENAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_12.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO PROCESSUAL PENAL II e seus pré-requisitos (possibilidade 3)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO DAS RELACOES DE CONSUMO'
medias_direito_rc = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('CIVIL II|CIVIL III|CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_rc = medias_direito_rc.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_rc = medias_direito_rc.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_rc = medias_direito_rc.dropna()

fig_13 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_rc['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_rc['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_direito_rc['TEORIA GERAL DO PROCESSO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DAS RELACOES DE CONSUMO', values=medias_direito_rc['DIREITO DAS RELACOES DE CONSUMO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_13.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO DAS RELACOES DE CONSUMO e seus pré-requisitos (possibilidade 1)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO CIVIL III|DIREITO DAS RELACOES DE CONSUMO'
medias_direito_rc_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_rc_2 = medias_direito_rc_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_rc_2 = medias_direito_rc_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_rc_2 = medias_direito_rc_2.dropna()

fig_14 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_rc_2['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_rc_2['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_rc_2['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL III', values=medias_direito_rc_2['DIREITO CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DAS RELACOES DE CONSUMO', values=medias_direito_rc_2['DIREITO DAS RELACOES DE CONSUMO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_14.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO DAS RELAÇÕES DE CONSUMO e seus pré-requisitos (possibilidade 2)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO EMPRESARIAL I|DIREITO DAS RELACOES DE CONSUMO'
medias_direito_rc_3 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III|DIREITO CONSTITUCIONAL IV|DIREITO EMPRESARIAL II|DIREITO EMPRESARIAL III|DIREITO EMPRESARIAL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_rc_3 = medias_direito_rc_3.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_rc_3 = medias_direito_rc_3.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_rc_3 = medias_direito_rc_3.dropna()

fig_15 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_rc_3['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_rc_3['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_rc_3['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL I', values=medias_direito_rc_3['DIREITO EMPRESARIAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DAS RELACOES DE CONSUMO', values=medias_direito_rc_3['DIREITO DAS RELACOES DE CONSUMO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_15.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DDIREITO DAS RELAÇÕES DE CONSUMO e seus pré-requisitos (possibilidade 3)',
    height=600, 
    margin=dict(l=90, r=80)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO PROCESSUAL CIVIL I|DIREITO PROCESSUAL CIVIL II|DIREITO PROCESSUAL CIVIL III|CARREIRAS JURIDICAS|PRATICA JURIDICA III - ATENDIMENTOS|ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'
medias_atendimentos_1 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO PROCESSUAL CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_atendimentos_1 = medias_atendimentos_1.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_atendimentos_1 = medias_atendimentos_1.pivot(index='discente', columns='nome_componente', values='media_final')
medias_atendimentos_1 = medias_atendimentos_1.dropna()

fig_16 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_atendimentos_1['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_atendimentos_1['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_atendimentos_1['TEORIA GERAL DO PROCESSO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL I', values=medias_atendimentos_1['DIREITO PROCESSUAL CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_atendimentos_1['DIREITO PROCESSUAL CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL III', values=medias_atendimentos_1['DIREITO PROCESSUAL CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='CARREIRAS JURIDICAS', values=medias_atendimentos_1['CARREIRAS JURIDICAS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='PRATICA JURIDICA III', values=medias_atendimentos_1['PRATICA JURIDICA III - ATENDIMENTOS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='ATENDIMENTOS - ANDAMENTOS PROCESSUAIS', values=medias_atendimentos_1['ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_16.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de ATENDIMENTOS - ANDAMENTOS PROCESSUAIS e seus pré-requisitos (possibilidade 1: CARREIRAS JURIDICAS)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO PROCESSUAL CIVIL I|DIREITO PROCESSUAL CIVIL II|DIREITO PROCESSUAL CIVIL III|PECAS JURIDICAS I|PRATICA JURIDICA III - ATENDIMENTOS|ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'
medias_atendimentos_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV|PECAS JURIDICAS II|DIREITO PROCESSUAL CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_atendimentos_2 = medias_atendimentos_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_atendimentos_2 = medias_atendimentos_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_atendimentos_2 = medias_atendimentos_2.dropna()

fig_17 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_atendimentos_2['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_atendimentos_2['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_atendimentos_2['TEORIA GERAL DO PROCESSO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL I', values=medias_atendimentos_2['DIREITO PROCESSUAL CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_atendimentos_2['DIREITO PROCESSUAL CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL III', values=medias_atendimentos_2['DIREITO PROCESSUAL CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='PEÇAS JURÍDICAS I', values=medias_atendimentos_2['PECAS JURIDICAS I (JUDICIAIS)'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='PRATICA JURIDICA III', values=medias_atendimentos_2['PRATICA JURIDICA III - ATENDIMENTOS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='ATENDIMENTOS - ANDAMENTOS PROCESSUAIS', values=medias_atendimentos_2['ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_17.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de ATENDIMENTOS - ANDAMENTOS PROCESSUAIS e seus pré-requisitos (possibilidade 2: PEÇAS JURIDICAS I)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO PROCESSUAL CIVIL I|DIREITO PROCESSUAL CIVIL II|DIREITO PROCESSUAL CIVIL III|PECAS JURIDICAS II|PRATICA JURIDICA III - ATENDIMENTOS|ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'
medias_atendimentos_3 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV|PECAS JURIDICAS I (JUDICIAIS)|DIREITO PROCESSUAL CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_atendimentos_3 = medias_atendimentos_3.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_atendimentos_3 = medias_atendimentos_3.pivot(index='discente', columns='nome_componente', values='media_final')
medias_atendimentos_3 = medias_atendimentos_3.dropna()

fig_18 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_atendimentos_3['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_atendimentos_3['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_atendimentos_3['TEORIA GERAL DO PROCESSO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL I', values=medias_atendimentos_3['DIREITO PROCESSUAL CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_atendimentos_3['DIREITO PROCESSUAL CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL III', values=medias_atendimentos_3['DIREITO PROCESSUAL CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='PEÇAS JURIDICAS II', values=medias_atendimentos_3['PECAS JURIDICAS II (EXTRAJUDICIAIS)'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='PRATICA JURIDICA III', values=medias_atendimentos_3['PRATICA JURIDICA III - ATENDIMENTOS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='ATENDIMENTOS - ANDAMENTOS PROCESSUAIS', values=medias_atendimentos_3['ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_18.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de ATENDIMENTOS - ANDAMENTOS PROCESSUAIS e seus pré-requisitos (possibilidade 3: PEÇAS JURIDICAS II)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO PROCESSUAL CIVIL I|DIREITO PROCESSUAL CIVIL II|DIREITO PROCESSUAL CIVIL III|AUTOCOMPOSICAO|PRATICA JURIDICA III - ATENDIMENTOS|ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'
medias_atendimentos_4 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV|DIREITO PROCESSUAL CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_atendimentos_4 = medias_atendimentos_4.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_atendimentos_4 = medias_atendimentos_4.pivot(index='discente', columns='nome_componente', values='media_final')
medias_atendimentos_4 = medias_atendimentos_4.dropna()

fig_19 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_atendimentos_4['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_atendimentos_4['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_atendimentos_4['TEORIA GERAL DO PROCESSO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL I', values=medias_atendimentos_4['DIREITO PROCESSUAL CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_atendimentos_4['DIREITO PROCESSUAL CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL III', values=medias_atendimentos_4['DIREITO PROCESSUAL CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='AUTOCOMPOSIÇÃO DE CONFLITOS', values=medias_atendimentos_4['AUTOCOMPOSICAO DE CONFLITOS: NEGOCIACAO, CONCILIACAO E MEDIACAO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='PRATICA JURIDICA III', values=medias_atendimentos_4['PRATICA JURIDICA III - ATENDIMENTOS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='ATENDIMENTOS - ANDAMENTOS PROCESSUAIS', values=medias_atendimentos_4['ATENDIMENTOS - ANDAMENTOS PROCESSUAIS'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
        ]
    )
)

fig_19.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de ATENDIMENTOS - ANDAMENTOS PROCESSUAIS e seus pré-requisitos (possibilidade 4: AUTOCOMPOSICAO DE CONFLITOS)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO CIVIL III|DIREITO DO TRABALHO I|DIREITO DO TRABALHO II|DIREITO DO TRABALHO III'
medias_direito_do_trabalho = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_do_trabalho = medias_direito_do_trabalho.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_do_trabalho = medias_direito_do_trabalho.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_do_trabalho = medias_direito_do_trabalho.dropna()

fig_20 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_do_trabalho['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_do_trabalho['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_do_trabalho['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL III', values=medias_direito_do_trabalho['DIREITO CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DO TRABALHO I', values=medias_direito_do_trabalho['DIREITO DO TRABALHO I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DO TRABALHO II', values=medias_direito_do_trabalho['DIREITO DO TRABALHO II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DO TRABALHO III', values=medias_direito_do_trabalho['DIREITO DO TRABALHO III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_20.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO DO TRABALHO III e seus pré-requisitos (possibilidade 1)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO DO TRABALHO I|DIREITO DO TRABALHO II|DIREITO DO TRABALHO III'
medias_direito_do_trabalho_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_do_trabalho_2 = medias_direito_do_trabalho_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_do_trabalho_2 = medias_direito_do_trabalho_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_do_trabalho_2 = medias_direito_do_trabalho_2.dropna()

fig_21 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_do_trabalho_2['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_do_trabalho_2['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_do_trabalho_2['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DO TRABALHO I', values=medias_direito_do_trabalho_2['DIREITO DO TRABALHO I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DO TRABALHO II', values=medias_direito_do_trabalho_2['DIREITO DO TRABALHO II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DO TRABALHO III', values=medias_direito_do_trabalho_2['DIREITO DO TRABALHO III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_21.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO DO TRABALHO III e seus pré-requisitos (possibilidade 2)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO TRIBUTARIO'
medias_direito_tributario = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III|DIREITO TRIBUTARIO APLICADO|ELEMENTOS DO DIREITO TRIBUTARIO')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_tributario = medias_direito_tributario.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_tributario = medias_direito_tributario.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_tributario = medias_direito_tributario.dropna()

fig_22 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_tributario['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_tributario['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_tributario['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO TRIBUTARIO', values=medias_direito_tributario['DIREITO TRIBUTARIO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_22.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO TRIBUTÁRIO e seus pré-requisitos',
    height=600, 
    margin=dict(l=90, r=90)
)

string_disciplinas = 'SOCIOLOGIA E ANTROPOLOGIA GERAL|DIREITO PROCESSUAL CIVIL I|DIREITO PROCESSUAL CIVIL II|DIREITO PROCESSUAL CIVIL III|DIREITO PROCESSUAL COLETIVO'
medias_direito_pc = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO PROCESSUAL CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_pc = medias_direito_pc.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_pc = medias_direito_pc.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_pc = medias_direito_pc.dropna()

fig_23 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='SOCIOLOGIA E ANTROPOLOGIA GERAL', values=medias_direito_pc['SOCIOLOGIA E ANTROPOLOGIA GERAL'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL I', values=medias_direito_pc['DIREITO PROCESSUAL CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_direito_pc['DIREITO PROCESSUAL CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL III', values=medias_direito_pc['DIREITO PROCESSUAL CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL COLETIVO', values=medias_direito_pc['DIREITO PROCESSUAL COLETIVO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_23.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO PROCESSUAL COLETIVO e seus pré-requisitos',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO CIVIL VI|DIREITO CIVIL VII'
medias_direito_civil_7 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL III|DIREITO CIVIL IV|DIREITO CIVIL VIII')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil_7 = medias_direito_civil_7.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil_7 = medias_direito_civil_7.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil_7 = medias_direito_civil_7.dropna()

fig_24 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil_7['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_civil_7['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_civil_7['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL III', values=medias_direito_civil_7['DIREITO CIVIL VI'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL IV', values=medias_direito_civil_7['DIREITO CIVIL VII'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_24.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL VII e seus pré-requisitos',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO CIVIL V|DIREITO CIVIL VIII'
medias_direito_civil_8 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL III|DIREITO CIVIL IV'))) & (~(matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL VI')) & (~(matriculas_direito_sem_trancamento['nome_componente'] == 'DIREITO CIVIL VII'))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil_8 = medias_direito_civil_8.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil_8 = medias_direito_civil_8.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil_8 = medias_direito_civil_8.dropna()

fig_25 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil_8['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_civil_8['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_civil_8['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL V', values=medias_direito_civil_8['DIREITO CIVIL V'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL VIII', values=medias_direito_civil_8['DIREITO CIVIL VIII'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_25.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL VIII e seus pré-requisitos (possibilidade 1)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO EMPRESARIAL I|DIREITO EMPRESARIAL II|DIREITO CIVIL VIII'
medias_direito_civil_8_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO EMPRESARIAL III|DIREITO CONSTITUCIONAL III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil_8_2 = medias_direito_civil_8_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil_8_2 = medias_direito_civil_8_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil_8_2 = medias_direito_civil_8_2.dropna()

fig_26 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil_8_2['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_civil_8_2['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_civil_8_2['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL I', values=medias_direito_civil_8_2['DIREITO EMPRESARIAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO EMPRESARIAL II', values=medias_direito_civil_8_2['DIREITO EMPRESARIAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL VIII', values=medias_direito_civil_8_2['DIREITO CIVIL VIII'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_26.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL VIII e seus pré-requisitos (possibilidade 2)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO PROCESSUAL PENAL I|DIREITO PROCESSUAL PENAL II|DIREITO CIVIL VIII'
medias_direito_civil_8_3 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil_8_3 = medias_direito_civil_8_3.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil_8_3 = medias_direito_civil_8_3.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil_8_3 = medias_direito_civil_8_3.dropna()

fig_27 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil_8_3['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_civil_8_3['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_civil_8_3['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL I', values=medias_direito_civil_8_3['DIREITO PROCESSUAL PENAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL PENAL II', values=medias_direito_civil_8_3['DIREITO PROCESSUAL PENAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL VIII', values=medias_direito_civil_8_3['DIREITO CIVIL VIII'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_27.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL VIII e seus pré-requisitos (possibilidade 3)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO CIVIL III|DIREITO DAS RELACOES DE CONSUMO|DIREITO CIVIL VIII'
medias_direito_civil_8_4 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil_8_4 = medias_direito_civil_8_4.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil_8_4 = medias_direito_civil_8_4.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil_8_4 = medias_direito_civil_8_4.dropna()

fig_28 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil_8_4['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_civil_8_4['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL II', values=medias_direito_civil_8_4['DIREITO CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL III', values=medias_direito_civil_8_4['DIREITO CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO DAS RELACOES DE CONSUMO', values=medias_direito_civil_8_4['DIREITO DAS RELACOES DE CONSUMO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL VIII', values=medias_direito_civil_8_4['DIREITO CIVIL VIII'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_28.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL VIII e seus pré-requisitos (possibilidade 4)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO PROCESSUAL CIVIL I|DIREITO PROCESSUAL CIVIL II|DIREITO PROCESSUAL CIVIL III|DIREITO CIVIL VIII'
medias_direito_civil_8_5 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV|DIREITO PROCESSUAL CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil_8_5 = medias_direito_civil_8_5.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil_8_5 = medias_direito_civil_8_5.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil_8_5 = medias_direito_civil_8_5.dropna()

fig_29 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil_8_5['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL I', values=medias_direito_civil_8_5['DIREITO CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_direito_civil_8_5['TEORIA GERAL DO PROCESSO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL I', values=medias_direito_civil_8_5['DIREITO PROCESSUAL CIVIL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_direito_civil_8_5['DIREITO PROCESSUAL CIVIL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO PROCESSUAL CIVIL III', values=medias_direito_civil_8_5['DIREITO PROCESSUAL CIVIL III'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL VIII', values=medias_direito_civil_8_5['DIREITO CIVIL VIII'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_29.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL VIII e seus pré-requisitos (possibilidade 5)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CONSTITUCIONAL I|DIREITO CONSTITUCIONAL II|DIREITO ADMINISTRATIVO I|DIREITO ADMINISTRATIVO II|DIREITO CIVIL VIII'
medias_direito_civil_8_6 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CONSTITUCIONAL III|DIREITO ADMINISTRATIVO III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_civil_8_6 = medias_direito_civil_8_6.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_civil_8_6 = medias_direito_civil_8_6.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_civil_8_6 = medias_direito_civil_8_6.dropna()

fig_30 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_civil_8_6['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL I', values=medias_direito_civil_8_6['DIREITO CONSTITUCIONAL I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CONSTITUCIONAL II', values=medias_direito_civil_8_6['DIREITO CONSTITUCIONAL II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO ADMINISTRATIVO I', values=medias_direito_civil_8_6['DIREITO ADMINISTRATIVO I'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO ADMINISTRATIVO II', values=medias_direito_civil_8_6['DIREITO ADMINISTRATIVO II'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2)),
            dict(label='DIREITO CIVIL VIII', values=medias_direito_civil_8_6['DIREITO CIVIL VIII'].values, range=[5, 10], tickvals=np.arange(5, 10.1, 0.2))
        ]
    )
)

fig_30.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO CIVIL VIII e seus pré-requisitos (possibilidade 6)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO PROCESSUAL DO TRABALHO'
medias_direito_pt = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_pt = medias_direito_pt.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_pt = medias_direito_pt.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_pt = medias_direito_pt.dropna()

fig_31 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='INTRODUCAO AO ESTUDO DO DIREITO', values=medias_direito_pt['INTRODUCAO AO ESTUDO DO DIREITO'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO CIVIL I', values=medias_direito_pt['DIREITO CIVIL I'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_direito_pt['TEORIA GERAL DO PROCESSO'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL DO TRABALHO', values=medias_direito_pt['DIREITO PROCESSUAL DO TRABALHO'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5))
        ]
    )
)

fig_31.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO PROCESSUAL DO TRABALHO (possibilidade 1)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|TEORIA GERAL DO PROCESSO|DIREITO PROCESSUAL CIVIL I|DIREITO PROCESSUAL CIVIL II|DDIREITO PROCESSUAL CIVIL III|DIREITO PROCESSUAL CIVIL IV|IREITO PROCESSUAL DO TRABALHO'
medias_direito_pt_2 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL II|DIREITO CIVIL III|DIREITO CIVIL IV')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_pt_2 = medias_direito_pt_2.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_pt_2 = medias_direito_pt_2.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_pt_2 = medias_direito_pt_2.dropna()

fig_32 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='DIREITO CIVIL I', values=medias_direito_pt_2['DIREITO CIVIL I'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='TEORIA GERAL DO PROCESSO', values=medias_direito_pt_2['TEORIA GERAL DO PROCESSO'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL CIVIL I', values=medias_direito_pt_2['DIREITO PROCESSUAL CIVIL I'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_direito_pt_2['DIREITO PROCESSUAL CIVIL II'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL CIVIL III', values=medias_direito_pt_2['DIREITO PROCESSUAL CIVIL III'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL CIVIL IV', values=medias_direito_pt_2['DIREITO PROCESSUAL CIVIL IV'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL DO TRABALHO', values=medias_direito_pt_2['DIREITO PROCESSUAL DO TRABALHO'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5))
        ]
    )
)

fig_32.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO PROCESSUAL DO TRABALHO (possibilidade 2)',
    height=600, 
    margin=dict(l=90, r=120)
)

string_disciplinas = 'INTRODUCAO AO ESTUDO DO DIREITO|DIREITO CIVIL I|DIREITO CIVIL II|DIREITO CIVIL III|DIREITO DO TRABALHO I|DIREITO DO TRABALHO II|IREITO PROCESSUAL DO TRABALHO'
medias_direito_pt_3 = matriculas_direito_sem_trancamento[(matriculas_direito_sem_trancamento['discente'].isin(turma_concluintes_2024_2)) & (matriculas_direito_sem_trancamento['nome_componente'].str.contains(string_disciplinas)) & (~(matriculas_direito_sem_trancamento['nome_componente'].str.contains('DIREITO CIVIL IV|DIREITO DO TRABALHO III')))][['discente','nome_componente', 'media_final', 'semestre']]
medias_direito_pt_3 = medias_direito_pt_3.sort_values(by=['discente', 'semestre']).drop_duplicates(subset=['discente', 'nome_componente'], keep='last')
medias_direito_pt_3 = medias_direito_pt_3.pivot(index='discente', columns='nome_componente', values='media_final')
medias_direito_pt_3 = medias_direito_pt_3.dropna()

fig_33 = go.Figure(data=
    go.Parcoords(
        dimensions = [
            dict(label='DIREITO CIVIL I', values=medias_direito_pt_3['DIREITO CIVIL I'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO CIVIL II', values=medias_direito_pt_3['DIREITO CIVIL II'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL CIVIL II', values=medias_direito_pt_3['DIREITO CIVIL III'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO DO TRABALHO I', values=medias_direito_pt_3['DIREITO DO TRABALHO I'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO DO TRABALHO II', values=medias_direito_pt_3['DIREITO DO TRABALHO II'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5)),
            dict(label='DIREITO PROCESSUAL DO TRABALHO', values=medias_direito_pt_3['DIREITO PROCESSUAL DO TRABALHO'].values, range=[0, 10], tickvals=np.arange(0, 10.1, 0.5))
        ]
    )
)

fig_33.update_layout(
    title='Gráfico de coordenadas paralelas para as disciplinas de DIREITO PROCESSUAL DO TRABALHO (possibilidade 3)',
    height=600, 
    margin=dict(l=90, r=120)
)

direito_penal = [fig_1]
direito_civil = [fig_2]
direito_internacional_publico = [fig_3, fig_4]
hermeneutica = [fig_5]
direito_empresarial = [fig_6,  fig_7]
direito_administrativo = [fig_8]
direitos_humanos = [fig_9]
direito_processual_penal = [fig_10, fig_11, fig_12]
direito_rc = [fig_13, fig_14, fig_15]
atendimentos_andamentos = [fig_16, fig_17, fig_18, fig_19]
direito_trabalho = [fig_20, fig_21]
direito_tributario = [fig_22]
direito_pc = [fig_23]
direito_civil_7 = [fig_24]
direito_civil_8 = [fig_25, fig_26, fig_27, fig_28, fig_29, fig_30]
direito_pt = [fig_31, fig_32, fig_33]

graficos_por_disciplina = {
    "DIREITO PENAL IV": (direito_penal, "DIREITO PENAL IV"),
    "DIREITO CIVIL IV": (direito_civil, "DIREITO CIVIL IV"),
    "DIREITO INTERNACIONAL PUBLICO": (direito_internacional_publico, "DIREITO INTERNACIONAL PUBLICO"),
    "HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO": (hermeneutica, "HERMENEUTICA JURIDICA E TEORIA DA ARGUMENTACAO"),
    "DIREITO EMPRESARIAL III": (direito_empresarial, "DIREITO EMPRESARIAL III"),
    "DIREITO ADMINISTRATIVO II": (direito_administrativo, "DIREITO ADMINISTRATIVO II"),
    "DIREITOS HUMANOS FUNDAMENTAIS": (direitos_humanos, "DIREITOS HUMANOS FUNDAMENTAIS"),
    "DIREITOS PROCESSUAL PENAL II": (direito_processual_penal, "DIREITOS PROCESSUAL PENAL II"),
    "DIREITOS DAS RELACOES DE CONSUMO": (direito_rc, "DIREITOS DAS RELACOES DE CONSUMO"),
    "ATENDIMENTOS - ANDAMENTOS PROCESSUAIS": (atendimentos_andamentos, "ATENDIMENTOS - ANDAMENTOS PROCESSUAIS"),
    "DIREITO DO TRABALHO III": (direito_trabalho, "DIREITO DO TRABALHO III"),
    "DIREITO DO TRIBUTARIO": (direito_tributario, "DIREITO DO TRIBUTARIO"),
    "DIREITO PROCESSUAL COLETIVO": (direito_pc, "DIREITO PROCESSUAL COLETIVO"),
    "DIREITO CIVIL VII": (direito_civil_7, "DIREITO CIVIL VII"),
    "DIREITO CIVIL VIII": (direito_civil_8, "DIREITO CIVIL VIII"),
    "DIREITO PROCESSUAL DO TRABALHO": (direito_pt, "DIREITO PROCESSUAL DO TRABALHO")
}

opcoes_disciplinas = list(graficos_por_disciplina.keys())

col1, col2 = st.columns([4, 2], vertical_alignment="center")

with col1:
    st.text("Os gráficos de coordenadas paralelas abaixos exibem as médias obtidas pelos formandos de 2024.2 em uma disciplina e em todas as suas disciplinas pré-requisitos. No menu de seleção ao lado, você pode selecionar outras disciplinas e visualizar o desempenho nela e nas suas pré-requisitos.")

with col2:
    disciplina_selecionada = st.selectbox(
        "Selecione ua disciplina",
        opcoes_disciplinas,
        label_visibility="hidden"
    )

st.text("Observação: Algumas disciplinas possuem mais de um gráfico pois ela pode ter mais de 1 pré-requisito, então, são exibidos os gráficos de coordenadas paralelas para cada pré-requisito.")

lista_de_graficos_para_exibir, sub_titulo = graficos_por_disciplina[disciplina_selecionada]

for grafico in lista_de_graficos_para_exibir:
    st.plotly_chart(grafico, use_container_width=True)