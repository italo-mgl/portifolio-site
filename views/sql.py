import streamlit as st

st.title("Projetos com SQL")

bi_link_car = "https://app.powerbi.com/view?r=eyJrIjoiMDIyMWYxYjktODI5ZS00NWMxLWIxNTItNTg0MGEzMDBkZTcwIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9"

st.markdown(
    f"""
    <div style="text-align: center; margin: 20px;">
        <a href="{bi_link_car}" target="_blank" style="text-decoration: none;">
            <img src="https://i.ibb.co/jk7G24zn/dash-cars.png" alt="Dashboard" style="width: 100%; max-width: 800px; transition: transform 0.3s;">
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