import streamlit as st

from forms.contact import contact_form


@st.dialog("Entre em contato")
def show_contact_form():
    contact_form()

curr_pdf = "views/assets/Italo_Magalhaes-Data-Analyst.pdf"

# HERO SECTION #

        
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
        st.image("views/assets/perfil.png")
        
with col2:
    st.title("Ítalo Magalhães", anchor= False)
    st.write(
        " Analista de Dados."
    )
    if st.button("✉️ Entrar em contato"):
        show_contact_form()
    
    with open(curr_pdf, "rb") as pdf_file:
         btn = st.download_button(
              label= "📝Curriculo",
              data=pdf_file,
              file_name="Italo_Magalhaes_Data-Analyst.pdf",
              mime="application/pdf"
         )
         

## Experiencias e qualificações ##
st.write("\n")
st.subheader("Experiência e Certificações", anchor=False)
st.write(
    """
    - Analista de Dados - Hostweb Data Center.
    - Engenheiro Agrônomo - Universidade Federal do Ceará.
    - Analista de Sistemas - Faculdade UNIASSELVI.
    - Data Science and Artificial Intelligence - Datatech Florida USA
"""
)

## Experiências ##
st.write("\n")
st.subheader("Habilidades", anchor=False)
st.write("""
    - Analises estatísticas, Testes A/B, Analise Ad Hoc;
    - Modelagem e Análise exploratória de dados (PowerBi e DAX);
    - Bibliotecas para tratamento e análise de dados em Python (Pandas, Numpy, Matplotlib e Seaborn);
    - Normalização, limpeza e processamento de dados (PowerBI, DAX e Python);
    - Criação de dashboards com Power BI, Python, Streamlit;
    - Gerenciamento e requisições de API'S com Python;
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
        - ⚙️ n8n
        - ⚙️ Power Automate
        - 💻 Git/GitHub
        - 📈 SQL Server
        """
    )