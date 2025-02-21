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

## Navigation setup - without sections 
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

## Navigation setup - with sections

pg = st.navigation(
    {"Sobre": [about_page],
    "Projects":[project_1_page, project_2_page],
    "Currículo":[]
    }
)

## Logo image

st.sidebar.text("Entre em contato")

##st.sidebar.image("views/assets/linkedin.png", width=30)



col5, col6, col7, col8 = st.sidebar.columns(4,border=True)

with col5:
    st.image("views/assets/linkedin.png", width=25)

with col6:
    st.image("views/assets/linkedin.png", width=25)

with col7:
    st.image("views/assets/linkedin.png", width=25)

with col8:
    st.image("views/assets/linkedin.png", width=25)

## RUN Navigation
pg.run()
