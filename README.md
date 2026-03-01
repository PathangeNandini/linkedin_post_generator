🚀 LinkedIn Post Generator (AI Powered)

An AI-powered LinkedIn post generator that creates professional, motivational, and engaging posts based on:

- Topic (e.g., Software Engineering, Motivation)
- Length (Short / Medium / Long)
- Language (English / Hinglish)
- Tone (Motivational, Professional, Emotional, Funny, Inspirational)

✨ Built with **Streamlit + LangChain + Groq (LLaMA 3.3)**

---

🌟 Features

✔ AI-Generated LinkedIn Posts  
Creates high-quality posts using LLaMA 3.3 models.

✔ Hashtag Generator  
Automatically generates relevant hashtags.

✔ Smart Sidebar Dashboard  
- Motivational quote  
- Post generation counter  
- Post history  
- “About Me” section  

✔ Download Generated Post  
Export as `.txt` file.

✔ Fully Deployable  
Runs perfectly on **Streamlit Cloud**.

---

🗂️ Project Structure
├── main.py
├── few_shot.py
├── post_generator.py
├── llm_helper.py
├── preprocess.py
├── requirements.txt
├── data/
│ ├── data.json
│ └── processed_posts.json
└── .streamlit/
