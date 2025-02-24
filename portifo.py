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
    page="views/PowerBi.py",
    title="Power Bi",
    icon="📊"
)

project_2_page = st.Page(
    page="views/dashboard.py",
    title="Python",
    icon="🐍",
)

curriculo_page = st.Page(
    page="views/curriculo.py",
    title="Curriculo",
    icon ="📝"
)

## Navigation setup - without sections 
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

## Navigation setup - with sections

pg = st.navigation(
    {"Sobre": [about_page],
    "Projetos":[project_1_page, project_2_page],
    "Currículo":[curriculo_page]
    }
)

## Logo image

st.sidebar.text("Entre em contato")

##st.sidebar.image("views/assets/linkedin.png", width=30)



col5, col6 = st.sidebar.columns(2,border=False, gap="small")

with col5:
    st.image("views/assets/linkedin.png", width=40)

with col6:
    st.image("views/assets/e-mail.png", width=40)

#with col7:
    #st.image("views/assets/linkedin.png", width=50)

#with col8:
    #st.image("views/assets/linkedin.png", width=50)

## RUN Navigation
pg.run()
