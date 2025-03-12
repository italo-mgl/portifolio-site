import streamlit as st

st.set_page_config( page_title="Ítalo Magalhães - Portifólio")
#st.title("Ítalo Magalhães")

## Page configuration 

about_page = st.Page(
    page="views/about_me.py",
    title="Sobre mim",
    icon="🖥️",
    default= True,
)



project_1_page = st.Page(
    page="views/PowerBi.py",
    title="Power Bi",
    icon="📊"
)

project_2_page = st.Page(
    page="views/python.py",
    title="Python",
    icon="🐍",
)

project_3_page = st.Page(
    page="views/sql.py",
    title="SQL",
    icon="🛢️",
)

curriculo_page = st.Page(
    page="views/curriculo.py",
    title="Curriculo",
    icon ="📝"
)

## Navigation setup - with sections

pg = st.navigation(
    {"Sobre": [about_page],
    "Projetos":[project_1_page, project_2_page, project_3_page],
    "Currículo":[curriculo_page]
    }
)


st.sidebar.markdown(
    """
    <div style="text-align: center; margin-bottom: 30px;">
        <h4>Redes</h4>
    </div>
    """, 
    unsafe_allow_html=True
)

# URLs das imagens e links
image_url = "https://cdn-icons-png.flaticon.com/512/145/145807.png"
link_url = "https://www.linkedin.com/in/magalhaes-italo/"
image_url2 = "https://cdn-icons-png.flaticon.com/512/25/25231.png"
link_url2 = "https://github.com/italo-mgl"

# Criando uma div para alinhar os ícones
st.sidebar.markdown(
    """
    <div style="display: flex; justify-content: center; gap: 40px;">
    <a href="{}" target="_blank">
        <img src="{}" width="45">
    </a>
    <a href="{}" target="_blank">
        <img src="{}" width="45">
    </a>
    </div>
    """.format(link_url, image_url, link_url2, image_url2),
    unsafe_allow_html=True
)

## RUN Navigation
pg.run()
