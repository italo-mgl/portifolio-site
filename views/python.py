import streamlit as st


st.markdown(
    """
    <h1 style="text-align: center;">Projetos com Python</h1>
    """,
    unsafe_allow_html=True
)

### Estudo com Pandas

st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 32px; font-weight: bold;">Repositório de estudo com Pandas:</p>
        <p style="font-size: 16px;"> 
        Repositório destinado a estudo da biblioteca pandas para analise de dados.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


repo_pandas = "https://github.com/italo-mgl/Pandas_Pratica"

st.markdown(
    f"""
    <div style="text-align: center; margin: 20px;">
        <a href="{repo_pandas}" target="_blank" style="text-decoration: none;">
            <img src="https://i.ibb.co/mCm1XFHz/repositorio-pandas.png" alt="Dashboard" style="width: 50%; max-width: 300px; transition: transform 0.3s;">
            <h3 style="transition: color 0.3s;">Repositório de Estudos Pandas</h3>
        </a>
    </div>

    <style>
        a:hover img {{
            transform: scale(1.05);
        }}
        a:hover h3 {{
            color: #007BFF; /* Cor do texto ao passar o mouse */
        }}
    </style>
    """,
    unsafe_allow_html=True
)

### Repositório projetos ciencias de dados
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 32px; font-weight: bold;">Repositório dedicado a projetos de Ciências de Dados</p>
        <p style="font-size: 16px;"> 
        Projetos: Análise Taxa de Suicídio, E.D.A, Sistema de recomendação de filmes, Web Scraping...
    </div>
    """,
    unsafe_allow_html=True
)


repo_natalino = "https://github.com/italo-mgl/Ciencias_de_Dados_Projetos"

st.markdown(
    f"""
    <div style="text-align: center; margin: 20px;">
        <a href="{repo_natalino}" target="_blank" style="text-decoration: none;">
            <img src="https://i.ibb.co/hzv7bsL/ciencias-dados.png" alt="Dashboard" style="width: 50%; max-width: 300px; transition: transform 0.3s;">
            <h3 style="transition: color 0.3s;">Repositório de Projetos de Ciências de Dados</h3>
        </a>
    </div>

    <style>
        a:hover img {{
            transform: scale(1.05);
        }}
        a:hover h3 {{
            color: #007BFF; /* Cor do texto ao passar o mouse */
        }}
    </style>
    """,
    unsafe_allow_html=True
)




### Projeto Filmes Natalinos
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 32px; font-weight: bold;">Análise de Dados de Filmes Natalinos no IMDB:</p>
        <p style="font-size: 16px;"> 
        Analises feitas: Avaliação do ano de lançamento dos filmes, quantidade de votos IMDB, gênero principal.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


repo_natalino = "https://github.com/italo-mgl/Analise_Filmes_Natalinos/tree/main"

st.markdown(
    f"""
    <div style="text-align: center; margin: 20px;">
        <a href="{repo_natalino}" target="_blank" style="text-decoration: none;">
            <img src="https://i.ibb.co/93ttFyHF/Analise-filmes-Natalinos.png" alt="Dashboard" style="width: 50%; max-width: 300px; transition: transform 0.3s;">
            <h3 style="transition: color 0.3s;">Análise de Filmes Natalinos IMDB</h3>
        </a>
    </div>

    <style>
        a:hover img {{
            transform: scale(1.05);
        }}
        a:hover h3 {{
            color: #007BFF; /* Cor do texto ao passar o mouse */
        }}
    </style>
    """,
    unsafe_allow_html=True
)