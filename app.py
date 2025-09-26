# app.py
import os
os.environ["USER_AGENT"] = "ColdEmailGenerator/1.0"
os.environ["LANGCHAIN_TRACING_V2"] = "false"   # disable tracing
os.environ["LANGCHAIN_API_KEY"] = ""           # avoid sending telemetry


import streamlit as st
from chains import Chain
from portfolio_db import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader


def create_streamlit_app(chain, portfolio):
    st.title("📧 Cold Email Generator")

    url_input = st.text_input(
        "Enter a URL (or paste your own job posting URL below):",
        value="https://in.bebee.com/job/40a3cd2ce0674a40b1095c9d2e57de1e?trk=bingjobs"
    )
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            page_content = loader.load()
            if page_content:
                data = clean_text(page_content[0].page_content)

                # Load portfolio data into vector store
                portfolio.load_portfolio()

                jobs = chain.extract_jobs(data)

            if jobs:   # make sure at least one job was found
                job = jobs[0]  # take only the first job
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = chain.write_mail(job, links)
                st.text_area("Generated Email", email, height=500)
            else:
                st.warning("No jobs could be extracted from the page.")


        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    st.set_page_config(page_title="Cold Email Generator", page_icon="📧", layout="wide")
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio)
