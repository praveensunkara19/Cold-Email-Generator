# chains.py

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=os.getenv('GROQ_API_KEY'),
            model="llama-3.3-70b-versatile",
            temperature=0
        )

    def extract_jobs(self, clean_text):
        """
        Extract job postings from scraped page data.
        """
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE
            {page_data}
            ### INSTRUCTION
            The scraped text is from the careers page of a website.
            Your job is to extract the job postings and return them in JSON format containing the 
            following keys: 'company', 'role', 'experience', 'skills', and 'description'.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm

        try:
            response = chain_extract.invoke({'page_data': clean_text})
            json_parser = JsonOutputParser()
            jobs = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs (limit:10000 tokens).")

        return jobs if isinstance(jobs, list) else [jobs]

    def write_mail(self, job, links):
        """
        Write a cold email based on job details and portfolio links.
        """
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION
            {job_description}
            You are Praveen, Operations Manager and Business Development Executive at PraAI. PraAI is an AI and Software Consulting
            company with seamless integration of business processes through automated tools.
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability,
            process optimization, cost reduction, and heightened overall efficiency.
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of PraAI
            in fulfilling their needs.
            Also add the most relevant one from the following links to showcase PraAI's portfolios in single line : {link_list}.
            Remember you are Praveen, Operations Manager & Business Development Executive at PraAI. The content should be concise, to the point, and written in 2-3 short paragraphs.
            Do not provide any preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        response = chain_email.invoke({"job_description": str(job), "link_list": links})
        return response.content

if __name__ == "__main__":
    chain = Chain()
    print("Chain initialized successfully.")
