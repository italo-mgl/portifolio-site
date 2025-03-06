import streamlit as st

# Título centralizado
st.markdown(
    """
    <h1 style="text-align: center;">Projetos com Power BI</h1>
    """,
    unsafe_allow_html=True
)

# Legenda acima do dashboard
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 16px; font-weight: bold;">Dashboard de Vendas de Carros:</p>
        <p style="font-size: 16px;"> 
        Utilizando DAX para calculos de métricas: YTD, MOM, YOY, MTD
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Iframe centralizado
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <iframe title="Car_Sales" width="1000" height="450" src="https://app.powerbi.com/view?r=eyJrIjoiMDIyMWYxYjktODI5ZS00NWMxLWIxNTItNTg0MGEzMDBkZTcwIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

bi_link = "https://app.powerbi.com/view?r=eyJrIjoiMDIyMWYxYjktODI5ZS00NWMxLWIxNTItNTg0MGEzMDBkZTcwIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9"

st.markdown(
    f"""
    <div style="text-align: center; margin: 20px;">
        <a href="{bi_link}" target="_blank" style="text-decoration: none;">
            <img src="https://scontent-for2-1.xx.fbcdn.net/v/t39.30808-6/482279230_122108857934786829_8037870845834313548_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=127cfc&_nc_ohc=EOSQKDdOXHQQ7kNvgHquNuq&_nc_oc=AdgTLprGUCANdN-7bXyypMKXOs62Kvtw8hGLlgCgYERYmwKjg-IvJ8bsCzP7u2n3tq0&_nc_zt=23&_nc_ht=scontent-for2-1.xx&_nc_gid=A8F2WQFBiQmNGy86uB5lMz5&oh=00_AYD4lJtGaDflcuqKUZg2cd7JIQBkXC1l3VYni_teVvvMVQ&oe=67CFC908" alt="Dashboard" style="width: 100%; max-width: 800px; transition: transform 0.3s;">
            <h3 style="transition: color 0.3s;">Dashboard de Vendas de Carros</h3>
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
