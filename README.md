---
title: 🚀 Cold Email Generator
emoji: ✉️
colorFrom: blue
colorTo: yellow
sdk: streamlit
sdk_version: "1.35.0"   # Use your current installed Streamlit version
app_file: app.py
pinned: false
---

# 🚀 Cold Email Generator

This **Cold Email Generator** application helps you craft a targeted cold email for a company job as an **Operations Lead**, informing them that you can supply the operational team as a service.

[![Hugging Face Spaces](https://img.shields.io/badge/HuggingFace-ColdEmailGenerator-yellow?logo=huggingface)](https://huggingface.co/spaces/praveensunkara/Cold-Email-Generator)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/praveensunkara19/Cold-Email-Generator)

---

## ✨ **Features**

✅ Generate personalized cold emails for operations roles  
✅ Uses **LangChain** and **Groq API** for fast LLM-based generation  
✅ Reads PDFs for contextual understanding if extended for resume-based generation  
✅ Simple, clean Streamlit interface for quick deployment and testing

---

## 🛠 **Tech Stack**

- [LangChain](https://python.langchain.com/)
- [PyPDF](https://pypi.org/project/pypdf/)
- Prompt Templates
- [Groq API](https://groq.com/)

---

## 🌐 **Live Demo**

▶️ Check out the app on [Hugging Face Spaces](https://huggingface.co/spaces/praveensunkara/Cold-Email-Generator).

---

## 💻 **Installation**

```bash
1. Clone the repository

git clone https://github.com/praveensunkara19/Cold-Email-Generator.git
cd Cold-Email-Generator

2. Create virtual environment & activate

python -m venv myenv
myenv\Scripts\activate    # For Windows
# source myenv/bin/activate   # For Linux/Mac

3. Install requirements

pip install -r requirements.txt

4. Add your environment variables
Create a .env file with:

GROQ_API_KEY=your_groq_api_key
Or directly paste your Groq API key in place of GROQ_API_KEY in the code if testing locally.

5. Run the app

streamlit run app.py
```