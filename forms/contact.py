import streamlit as st
import requests
import re

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nome:")
        email = st.text_input("E-mail:")
        message = st.text_area("Mensagem:", height=150)
        submit_button = st.form_submit_button("Enviar")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Serviço de e-mail não está funcionando no momento. Tente mais tarde", icon="📧")
            st.stop()

        if not name:
            st.error("Por favor, coloque seu nome.", icon="🧑")
            st.stop()

        if not email:
            st.error("Por favor, coloque seu e-mail.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Por favor, coloque um e-mail válido.", icon="📧")
            st.stop()

        if not message:
            st.error("Por favor, coloque uma mensagem.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {
            "email": email,
            "nome": name,
            "mensagem": message
        }
        
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 202:
            st.success("Sua mensagem foi enviada com sucesso!🎉", icon="🚀")
        else:
            st.error("Ocorreu um erro ao enviar sua mensagem. Código de status: {}".format(response.status_code), icon="😨")
