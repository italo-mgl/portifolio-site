import streamlit as st

st.set_page_config( page_title="Ítalo Magalhães - Portifólio")
#st.title("Ítalo Magalhães")

## Page configuration 

about_page = st.Page(
    page="views/about_me.py",
    title="Sobre mim",
    icon="👌",
    default= True,
)

project_1_page = st.Page(
    page="views/dashboard.py",
    title="Sales Dashboard",
    icon="😁",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon="👍",
)

## Navigation setup - without sections 
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

## Navigation setup - with sections

pg = st.navigation(
    {"Sobre": [about_page],
    "Projects":[project_1_page, project_2_page]
    }
)

## Logo image

#st.logo("assets/painel (1).jpg", size="small")
st.sidebar.text("Entre em contato")
st.sidebar.markdown(
    """
    <a href="https://www.linkedin.com/in/magalhaes-italo/" target="_blank">
        <img src="assets/painel.png" alt="Ícone" style="width:50px;height:50px;">
    </a>
    """, 
    unsafe_allow_html=True
)
## RUN Navigation
pg.run()
