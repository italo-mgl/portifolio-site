import streamlit as st

from forms.contact import contact_form


@st.dialog("Entre em contato")
def show_contact_form():
    contact_form()

curr_pdf = "views/assets/Ítalo_s_Resume.pdf"

# HERO SECTION #


        
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
        st.image("views/assets/perfil.png")
        
with col2:
    st.title("Itin", anchor= False)
    st.write(
        " Analista de Sistemas, com experiencia em DEVOPS"
    )
    if st.button("✉️ Entrar em contato"):
        show_contact_form()
    
    with open(curr_pdf, "rb") as pdf_file:
         btn = st.download_button(
              label= "📝Curriculo",
              data=pdf_file,
              file_name="Italo_Magalhaes_CV.pdf",
              mime="application/pdf"
         )
         

## Experiencias e qualificações ##
st.write("\n")
st.subheader("Experiência e Certificações", anchor=False)
st.write(
    """
    - Analista de Processos - Hostweb Data Center.
    - Engenheiro Agrônomo - Universidade Federal do Ceará.
    - Analista de Sistemas - Faculdade UNIASSELVI.
"""
)

## Experiências ##
st.write("\n")
st.subheader("Experiências", anchor=False)
st.write("""
    - Bibliotecas para tratamento e análise de dados em Python (Pandas, Numpy, Matplotlib e Seaborn).
    - Modelagem e Análise exploratória de dados (PowerBi e DAX).
    - Normalização, limpeza e processamento de dados (PowerBI, DAX e Python).
    - Criação de dashboards com Power BI, Python.
    - Gerenciamento e requisições de API'S com Python.
    - Gerenciamento de banco de dados com SQL.
         """)

## skiils ##
st.write("\n")
st.subheader("Linguagens e Tecnologias")

# Ajustando as colunas lado a lado
col3, col4 = st.columns(2)

with col3:
    st.write(
        """
        - 🐍 Python
        - 📊 Power BI
        - 📊 Excel
        - 🐘 PostgreSQL
        """
    )

with col4:
    st.write(
        """
        - 🛢️ Databricks
        - ⚙️ Power Automate
        - 💻 Git/GitHub
        - 📈 SQL Server
        """
    )