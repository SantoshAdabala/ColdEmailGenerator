
#  Cold EMail Generator

A cold email generator for service companies built with Groq, LangChain, and Streamlit. Users provide the URL of a company's careers page, and the tool extracts job listings from it. It then crafts personalized cold emails, incorporating relevant portfolio links pulled from a vector database, tailored to the specific job descriptions.

# Architecture Diagram
<img width="949" alt="Screenshot 2024-10-16 at 2 46 48 PM" src="https://github.com/user-attachments/assets/e6b1cbe1-caa3-49d7-9f85-cc27915e981f">


<img width="1286" alt="Screenshot 2024-10-16 at 2 34 27 PM" src="https://github.com/user-attachments/assets/61eead6d-cb24-433b-b68e-0817fdf29816">


Set-up

To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside app/.env update the value of GROQ_API_KEY with the API_KEY you created.

To get started, first install the dependencies using:

pip install -r requirements.txt

Run the streamlit app:

streamlit run app/main.py
