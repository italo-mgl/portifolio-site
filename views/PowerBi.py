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
        <p style="font-size: 32px; font-weight: bold;">Dashboard de Vendas de Carros:</p>
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

# bi_link_car = "https://app.powerbi.com/view?r=eyJrIjoiMDIyMWYxYjktODI5ZS00NWMxLWIxNTItNTg0MGEzMDBkZTcwIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9"

# st.markdown(
#     f"""
#     <div style="text-align: center; margin: 20px;">
#         <a href="{bi_link_car}" target="_blank" style="text-decoration: none;">
#             <img src="https://i.ibb.co/jk7G24zn/dash-cars.png" alt="Dashboard" style="width: 100%; max-width: 800px; transition: transform 0.3s;">
#             <h3 style="transition: color 0.3s;">Dashboard de Vendas de Carros</h3>
#         </a>
#     </div>

#     <style>
#         a:hover img {{
#             transform: scale(1.05);
#         }}
#         a:hover h3 {{
#             color: #007BFF; /* Cor do texto ao passar o mouse */
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

## Segundo projeto Dashboard

# Legenda acima do dashboard
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 32px; font-weight: bold;">Dashboard Análise de Vendas:</p>
        <p style="font-size: 16px;"> 
        Utilizando DAX para calculos de métricas: YTD, MOM, YOY, MTD
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <iframe title="Elertro Vendas" width="1000" height="450" src="https://app.powerbi.com/view?r=eyJrIjoiN2FkZWM3ZTUtOWNiOS00NTlhLWJlZjgtYTQ1YWU3NDc4ZWViIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9&pageName=ReportSection12a8a72e6fa50197971d" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# bi_link_vend = "https://app.powerbi.com/view?r=eyJrIjoiN2FkZWM3ZTUtOWNiOS00NTlhLWJlZjgtYTQ1YWU3NDc4ZWViIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9&pageName=ReportSection12a8a72e6fa50197971d"

# st.markdown(
#     f"""
#     <div style="text-align: center; margin: 20px;">
#         <a href="{bi_link_vend}" target="_blank" style="text-decoration: none;">
#             <img src="https://i.ibb.co/5h0Z4Nb3/dash-vendas.png" alt="Dashboard" style="width: 100%; max-width: 800px; transition: transform 0.3s;">
#             <h3 style="transition: color 0.3s;">Dashboard Análise de Vendas</h3>
#         </a>
#     </div>

#     <style>
#         a:hover img {{
#             transform: scale(1.05);
#         }}
#         a:hover h3 {{
#             color: #007BFF;
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

## Terceiro projeto Dashboard

# Legenda acima do dashboard
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 32px; font-weight: bold;">Dashboard RH:</p>
        <p style="font-size: 16px;"> 
        Utilizando DAX para calculos de métricas: YTD, MOM, YOY, MTD
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <iframe title="Dashboard-RH" width="1000" height="450" src="https://app.powerbi.com/view?r=eyJrIjoiZDc4ZTE3ZmQtNTZkMi00NTI2LTgzYzEtNGEzZjVmNTNmOTFlIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# bi_link_vend = "https://app.powerbi.com/view?r=eyJrIjoiN2FkZWM3ZTUtOWNiOS00NTlhLWJlZjgtYTQ1YWU3NDc4ZWViIiwidCI6Ijk4YTQ3YjdhLTBjMzYtNGUyNy04MGE3LTZjMDU2YzdjMWI0NCJ9&pageName=ReportSection12a8a72e6fa50197971d"

# st.markdown(
#     f"""
#     <div style="text-align: center; margin: 20px;">
#         <a href="{bi_link_vend}" target="_blank" style="text-decoration: none;">
#             <img src="https://i.ibb.co/5h0Z4Nb3/dash-vendas.png" alt="Dashboard" style="width: 100%; max-width: 800px; transition: transform 0.3s;">
#             <h3 style="transition: color 0.3s;">Dashboard Análise de Vendas</h3>
#         </a>
#     </div>

#     <style>
#         a:hover img {{
#             transform: scale(1.05);
#         }}
#         a:hover h3 {{
#             color: #007BFF;
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )
