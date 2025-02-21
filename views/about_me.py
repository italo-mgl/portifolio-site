import streamlit as st

from forms.contact import contact_form


@st.dialog("Entre em contato")
def show_contact_form():
    contact_form()



# HERO SECTION #

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
     st.markdown(
        """
        <a href="https://www.linkedin.com/in/magalhaes-italo/" target="_blank">
            <img src=https://media.licdn.com/dms/image/v2/D4D03AQENIb_3XPW3qw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1721253821571?e=1745452800&v=beta&t=xCoh-BJ-_GkzjfDNZHBiUOuy1LqRZZTisqWIcCOxV1E" ""
            alt="Ícone" style="width:100%;">
        </a>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.title("Itin", anchor= False)
    st.write(
        " Analista de Sistemas, com experiencia em DEVOPS"
    )
    if st.button("✉️Contact Me"):
        show_contact_form()

## Experiencias e qualificações ##
st.write("\n")
st.subheader("Experiência e Certificações", anchor=False)
st.write(
    """
    - Testador de funilaria profissional - Funilaria de Seu Carlos
    - Habilidoso com conversações de merda e enganação de público
    - Fazedor de tinturaria
"""
)

## skiils ##
st.write("\n")
st.subheader("Skills Técnicas")
st.write(
    """
    - 🐍 Python
    - 📊 Power BI
    - 📊 Tableu
    - 🐘 PostgreSQL
"""
)