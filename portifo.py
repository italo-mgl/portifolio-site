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

## Navigation setup - with sections

pg = st.navigation(
    {"Sobre": [about_page],
    "Projetos":[project_1_page, project_2_page],
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

image_url = "https://cdn-icons-png.flaticon.com/512/145/145807.png"
link_url = "https://www.linkedin.com/in/magalhaes-italo/"

image_url2 = "https://cdn-icons-png.flaticon.com/512/25/25231.png"
link_url2 = "https://github.com/italo-mgl"

col5, col6 = st.sidebar.columns(2,border=False, gap="small")

with col5:
    #st.image("views/assets/linkedin.png", width=40)
    st.markdown(
    f'<a href="{link_url}" target="_blank">'
    f'<img src="{image_url}" width="45"></a>', 
    unsafe_allow_html=True
    )
with col6:
    #st.image("views/assets/github.png", width=40)

    st.markdown(
    f'<a href="{link_url2}" target="_blank">'
    f'<img src="{image_url2}" width="40"></a>', 
    unsafe_allow_html=True
    )

## RUN Navigation
pg.run()
