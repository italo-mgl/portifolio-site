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