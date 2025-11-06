import streamlit as st
st.set_page_config(layout="wide")

st.title("Dashboard - Análise de Rendimento acadêmico")
st.text("Este dashboard contém todos os gráficos construídos para analisar o rendimento acadêmico dos discentes do curso de direito do turno matutino da UFRN no campus de Natal, entre os períodos de 2011.1 e 2024.2. Esta análise faz parte do Trabalho de Conclusão de Curso de Engenharia de Computação desenvolvido por Pedro Leandro Batista Marques. Abaixo é explicado brevemente o processo de coleta e pré-processamento dos dados, e no menu de seleção ao lado esquerdo, pode-se selecionar o tipo da análise realizada sobre os dados.") 
st.header("Coleta e Pré-processamento de dados")
st.markdown("Para realizar esta análise de dados, primeiro foi realizada uma coleta nos dados disponíveis no [portal de dados abertos da UFRN](https://dados.ufrn.br/). Então, foi feito o download de 1,94GB de dados, os quais distribuem-se em:")
st.markdown("1. 30 arquivos no formato .csv correspondentes a relação das matrículas em componentes dos cursos da UFRN, sendo cada arquivo corresponde à um determinado ano e período, disponíveis em [https://dados.ufrn.br/dataset/matriculas-componentes](https://dados.ufrn.br/dataset/matriculas-componentes).")
st.markdown("2. 30 arquivos no formato .csv correspondentes a relação de turmas dos cursos de todos os níveis de ensino da UFRN, sendo cada arquivo corresponde à um determinado ano e período,  disponíveis em [https://dados.ufrn.br/dataset/turmas](https://dados.ufrn.br/dataset/turmas).")
st.markdown("3. 1 arquivo no formato .csv correspondente a relação de componentes curriculares oferecidas pela UFRN em todas suas modalidades (presencial ou não), disponível em [https://dados.ufrn.br/dataset/componentes-curriculares](https://dados.ufrn.br/dataset/componentes-curriculares).")
st.markdown("4. 1 arquivo no formato .csv correspondente a relação de estruturas curriculares de todos os cursos da UFRN nos níveis de graduação e pós-graduação, disponível em [https://dados.ufrn.br/dataset/estruturas-curriculares](https://dados.ufrn.br/dataset/estruturas-curriculares).")
st.markdown("Em seguida, utilizando as bibliotecas pandas e numpy, os dados foram carregados e transformados em dataframes correspondente a cada categoria de arquivo .csv. Então, criou-se um dicionário dataframe para as matrículas, um dicionário de dataframes para as componentes curriculares, um dataframe com as estruturas curriculares e um dataframe com as componentes curriculares. A tabela abaixo ilustra o total de registros por dataframes.")

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("""
    | Total de registros de matrículas | Total de registros de turmas | Total de registros de componentes curriculares | Total de registros de estruturas curriculares |
    | :--- | :--- | :--- | :--- |
    | 18.968.575 | 387.935 | 44.525 | 450 |
    """)
st.markdown("Após isso, as diversas informações destes dataframes foram cruzadas a fim de se obter um único datframe contendo apenas os registros dos discentes do curso de direito no turno matutino da UFRN no campus de Natal. As duas imagens abaixo ilustram o processo de junção.")
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.image("imagens/estrategia1.png")
colA, colB, colC = st.columns([1, 6, 1])
with colB:
    st.image("imagens/estrategia2.png")

st.markdown("Este dataframe possui a estrutura desejada, porém, ele ainda contém os registros de todos os discentes da UFRN, então, este dataframe é filtrado buscando apenas os discentes cujo identificador do curso é 2000018, que é o identificador do curso de direito, no turno matutino, da UFRN do campus de natal. Após isso, é gerado um dataframe com estes registros e um arquivo .csv contendo estes registros, que agora ocupa apenas 16.8MB de espaço e possui 175550 registros.")
st.header("Estrutura curricular do curso de direito da UFRN")
st.text("A imagem abaixo ilustra a estrutura curricular 04A do curso de direito da UFRN, que corresponde a estrutura curricular do turno matutino e do campus de Natal vigente entre os períodos de 2011.1 e 2024.2 na UFRN.")
st.image("imagens/grafo_disciplinas.jpg")
