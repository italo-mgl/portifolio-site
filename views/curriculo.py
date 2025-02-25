import streamlit as st

# Título da página
st.title("Ítalo Magalhães")

# Informações de contato
st.header("Contatos")
st.write(""" 
     📞 [85-986160142](https://api.whatsapp.com/send?phone=5585986160142)  
     ✉️ [italomagalhaes77@gmail.com](mailto:italomagalhaes77@gmail.com)  
     🔗 [LinkedIn](https://www.linkedin.com/in/magalhaes-italo/) | [GitHub](https://github.com/italo-mgl)
     """)

# Seção de Formação
st.header("Formação")
st.write("""
- **UNIASSELVI**, Fortaleza, CE  
  Análise e Desenvolvimento de Sistemas (Jan. 2022 -- Dez. 2024)

- **Universidade Federal do Ceará**, Fortaleza, CE  
  Engenharia Agronômica (Ago. 2018 -- Dez. 2023)
""")

# Seção de Experiência
st.header("Experiência")
st.write("""
- **Analista de Processos**  
  Hostweb Data Center, Fortaleza, CE (Fev. 2024 -- Atualmente)  
  - Mapeamento de processos com delineamento de escopo e criação de fluxogramas utilizando Bizagi, Sharepoint e Bitrix24.
  - Documentação de processos com notação BPMN, analisando e buscando melhoria contínua dos processos de negócios com metodologia PDCA.
  - Gerenciamento de CRM e funis de vendas, criando automações em cards de negócios na plataforma Bitrix24.

- **Estagiário de Análise de Dados**  
  Meireles e Freitas Advogados Associados, Fortaleza, CE (Jan. 2023 -- Dez. 2023)  
  - Coleta, análise e tratamento de dados utilizando Excel e PowerBI e DAX.
  - Criação de relatórios, dashboards e apresentações utilizando PowerBI e PowerPoint.
  - Criação de automações de processos judiciais com Python utilizando Selenium e PyAutoGUI.

- **Bootcamp Ciências de Dados**  
  Instituto Atlântico, Fortaleza, CE (Out. 2022 -- Dez. 2022)  
  - Bootcamp seguindo metodologias ágeis utilizadas no mercado com SCRUM e KANBAN.
  - Fundamentação de estatística voltada para análise de dados.
  - Utilização de bibliotecas Python para análise de dados como Pandas, Seaborn e Matplotlib.
  - Criação de projeto sobre análise de sentimento do Twitter, definindo um sentimento de acordo com o contexto da mensagem e criando nuvem das palavras mais usadas.
""")

# Seção de Projetos
st.header("Projetos")
st.write("""
- **Gitlytics** | *Python, Flask, React, PostgreSQL, Docker*  
  Desenvolveu uma aplicação web full-stack usando Flask servindo uma API REST com React no front-end.

- **Simple Paintball** | *Spigot API, Java, Maven, TravisCI, Git*  
  Desenvolveu um plugin para servidor Minecraft que divertiu crianças durante o tempo livre, com mais de 2K downloads e uma média de 4.5/5 estrelas.
""")

# Seção de Habilidades Técnicas
st.header("Habilidades Técnicas")
st.write("""
- **Tecnologias**: PowerBI, DAX, Python, SQL, Excel, R, FastAPI, BPMN  
- **Bibliotecas Python**: Pandas, Numpy, Matplotlib, Plotly, Scikit-Learn, Selenium, PyAutoGUI  
- **Ferramentas**: Git, GitHub, Docker, Jupyter Notebook, VS Code, Bizagi, Bitrix24  
""")

# Rodapé
st.write("© Ítalo Magalhães. Todos os direitos reservados.")