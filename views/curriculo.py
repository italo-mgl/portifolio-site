import streamlit as st

# Início do conteúdo
st.markdown("<h1 style='text-align: center; color: #ffffff;'><b>Ítalo Magalhães</b></h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Analista de Dados</h3>", unsafe_allow_html=True)

# Informações de contato
st.markdown(
    """
    <p style='text-align: center;'>
    📞 <a href="https://api.whatsapp.com/send?phone=5585986160142" target="_blank">85-986160142</a> &nbsp;|&nbsp;
    ✉️ <a href="mailto:italomagalhaes77@gmail.com" target="_blank">italomagalhaes77@gmail.com</a> &nbsp;|&nbsp;
    🔗 <a href="https://www.linkedin.com/in/magalhaes-italo/" target="_blank">LinkedIn</a> &nbsp;|&nbsp;
    🐙 <a href="https://github.com/italo-mgl" target="_blank">GitHub</a> &nbsp;|&nbsp;
    🌐 <a href="https://italo-mgl.streamlit.app/" target="_blank">Portifólio</a>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---") 

# Seção de Formação
st.header("Formação")
st.markdown("""
- **UNIASSELVI** – Análise e Desenvolvimento de Sistemas
  *Fortaleza, CE | Jan. 2022 – Dez. 2024*
- **Universidade Federal do Ceará** – Engenharia Agronômica
  *Fortaleza, CE | Ago. 2018 – Dez. 2023*
""")

# Seção de Experiência
st.header("Experiência")

# Hostweb Data Center
st.subheader("Analista de Dados e Sistemas")
st.write("Hostweb Data Center - Fortaleza, CE 2024 – Atualmente")
st.markdown("""
- Atuei com a equipe de processos para definir os escopos dos setores e a criação de **métricas e KPIs** da empresa, com a criação de dashboards no **Power BI** para cada time, além de realizar apresentações à diretoria e stakeholders.
- Responsável por **estruturar, implementar e dar suporte** ao novo sistema ERP para o time de vendas varejo, além de criar **relatórios e definir métricas** analisando o desempenho do time de vendas, facilitando a gestão da diretoria e stakeholders.
- Responsável por estruturar todo o estoque da empresa no sistema, partindo desde a coleta das informações nos bancos de dados **SQL Server e PostgreSQL**, com o **tratamento e a modelagem** dos dados feita em **Excel** e realizando a atualização dos itens no sistema via **API com Python**, corrigindo e estruturando o estoque.
- Reponsável por estruturar o **CRM** da empresa em conjunto com o setor comercial, com a criação de **automações, fluxos de trabalho, e dashboards**, otimizando o funil de vendas e facilitando o gerenciamento.
- Atuei no **tratamento, estruturação e modelagem** dos dados dos clientes no processo de migração de sistema ERP, coletando dados via **SQL** e realizando a migração via **API** com scripts em **Python**.
- Atuei com o time de marketing na **criação e mensuração** de campanhas para prospecção de leads, através de eventos e estratégias de **inbound marketing**, com foco em otimização de resultados e melhoria contínua.
- Responsável por **manter e dar suporte** aos sistemas utilizados na empresa, como **CRM** comercial, **ERP** do time de varejo, **ferramenta ITSM** interna de chamados e tickets, além de criar automações via **Power Automate**, para disparo de questionários nas campanhas realizadas pelo RH.
""")

# Meireles e Freitas Advogados Associados
st.subheader("Estagiário de Análise de Dados")
st.write("Meireles e Freitas Advogados Associados - Fortaleza, CE  |  Jan. 2023 – Dez. 2023")
st.markdown("""
- Atuei no time de advogados associados, sendo responsável por **coletar, tratar e analisar** os dados oriundos dos processos com a utilização **Excel** e criação de relatórios e dashboards no **PowerBI** com uso de **DAX**.
- Contactava os diferentes times da empresa, atuando nas **diversas etapas dos processos**, além de participar de **reuniões com os stakeholders** para o direcionamento na criação de relatórios e dashboards.
- Responsável por criar relatórios semanais, quinzenais e mensais para diferentes setores, além de realizar **apresentações dos resultados** para a diretoria com a utilização de **Power Bi e PowerPoint**.
- Criação de automações de processos judiciais com Python utilizando **Selenium e PyAutoGUI**.
""")

# Seção de Certificações e Habilidades
st.header("Certificações e Habilidades")
st.markdown("""
- **Data Tech Florida**: Data Science and Artificial Intelligence in Action
- **Hashtag Treinamentos**: Análise de Dados Impressionadora
- **IMPARH**: Inglês B2
""")

st.markdown("### Tecnologias:")
st.write("PowerBI, DAX, Python, SQL Server, PostgreSQL, Excel, DataBricks")

st.markdown("### Ferramentas:")
st.write("Power Automate, Git, GitHub, Jupyter Notebook, Bitrix24")

st.markdown("### Bibliotecas Python:")
st.write("Pandas, Numpy, Matplotlib, Plotly, Scikit-Learn, Selenium, PyAutoGUI")
