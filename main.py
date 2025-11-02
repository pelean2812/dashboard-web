import streamlit as st

pagina_principal = st.Page(
    page = "paginas/principal.py",
    title = "Página inicial",
    icon = "🏠",
    default = True
)

pagina_analise_1 = st.Page(
    page = "paginas/analise1.py",
    title = "Situação geral dos discentes em disciplinas",
    icon = "📊"
)

pagina_analise_2 = st.Page(
    page = "paginas/analise2.py",
    title = "Médias finais médias",
    icon = "📈"
)

pagina_analise_3 = st.Page(
    page = "paginas/analise3.py",
    title = "Faltas x Médias finais dos discentes",
    icon = "🔥"
)

pagina_analise_4 = st.Page(
    page = "paginas/analise4.py",
    title = "Coordenadas paralelas",
    icon = "🚶‍♀️‍➡️"
)

pagina_analise_5 = st.Page(
    page = "paginas/analise5.py",
    title = "Desempenho dos formandos de 2024.2",
    icon = "👨🏽‍🎓"
)

pagina_analise_6 = st.Page(
    page = "paginas/analise6.py",
    title = "Dispersões das médias em disciplinas",
    icon = "📈"
)

pagina_analise_7 = st.Page(
    page = "paginas/analise7.py",
    title = "Situações dos discentes em disciplinas",
    icon = "📈"
)

navegacao = st.navigation({
    "Página principal": [pagina_principal],
    "Gráficos de barras": [pagina_analise_1],
    "Gráficos de evoluções temporais": [pagina_analise_2, pagina_analise_6, pagina_analise_7],
    "Heatmaps": [pagina_analise_3],
    "Turma de 2024.2": [pagina_analise_4, pagina_analise_5]
})

st.logo("imagens/ufrn_logo.png")

navegacao.run()