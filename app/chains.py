import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

os.getenv("GROQ_API_KEY")

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")
        
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format  containing 
            following keys: 'role', 'experience', 'skills' and 'description'.
            Only return the valid JSON
            ### VALID JSON (NO PREAMBLE):
            
            
            """
            
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse jobs")
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Siva Naga Santosh Adabala, a Data Scientist at Parlay Finance and a former Data Analyst at Accenture with over 3 years of experience. At Parlay Finance, a decentralized finance (DeFi) platform, you contributed to building sophisticated financial instruments, optimizing portfolio management strategies using blockchain, and developing data-driven investment solutions for both retail and institutional investors. You have hands-on experience in leveraging machine learning techniques like K-Means clustering and Random Forest to improve lending recommendation systems, as well as automating investment strategies.

            At Accenture, you delivered predictive models and insights that enhanced financial processes, improved loan eligibility evaluations, and optimized system integration, resulting in significant performance improvements. You effectively communicated actionable insights to stakeholders using tools like Tableau, and you are proficient in SQL, Python, and cloud platforms.

            Write a cold email highlighting your experience and how your skill set aligns with the job description provided above. Reference relevant accomplishments from Accenture and Parlay Finance to showcase your technical expertise and problem-solving ability. Ensure the email is concise, professional, and emphasizes how your background makes you an ideal fit for fulfilling the company's needs.

            ### EMAIL (NO PREMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))