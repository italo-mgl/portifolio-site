import streamlit as st

curr_pdf = "views/assets/Ítalo_s_Resume.pdf"
with open(curr_pdf, "rb") as pdf_file:
         btn = st.download_button(
              label= "📝Curriculo",
              data=pdf_file,
              file_name="Italo_Magalhaes_CV.pdf",
              mime="application/pdf"
         )