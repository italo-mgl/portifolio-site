import streamlit as st

st.title("Projetos com SQL")

st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 32px; font-weight: bold;">E.D.A Utilizando SQL no SQL Server:</p>
        <p style="font-size: 16px;"> 
        Analises feitas: Exploração DB, Exploração de Dimensões, Datas, Medidas, Magnitudes e Ranking.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


repo_sql = "https://github.com/italo-mgl/sql_estudos/tree/main/E.D.A%20SQL"

st.markdown(
    f"""
    <div style="text-align: center; margin: 20px;">
        <a href="{repo_sql}" target="_blank" style="text-decoration: none;">
            <img src="https://i.ibb.co/vx16xvY3/EDA-sql2.png" alt="Dashboard" style="width: 80%; max-width: 500px; transition: transform 0.3s;">
            <h3 style="transition: color 0.3s;">E.D.A com SQL</h3>
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