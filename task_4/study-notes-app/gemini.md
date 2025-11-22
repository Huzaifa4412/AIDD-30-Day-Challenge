# Study Notes Summarizer & Quiz Generator Agent  

AI-powered PDF summarizer and quiz generator using **Gemini CLI**, **OpenAgents SDK**, **PyPDF**, **Streamlit**, and **Context7 MCP**.

---

## ⭐ Overview  

This project allows students to upload PDFs, generate structured study notes, and create quizzes (MCQs or Mixed-Style) directly from the document.

It uses:

- Gemini CLI  
- OpenAgents SDK  
- PyPDF  
- Context7 MCP Tool Provider  
- Streamlit (for UI)  
- Python 3.11+

---

## 📌 Features

### ✅ 1. PDF Summarizer

- Upload PDF  
- Extract text using **PyPDF**  
- Generate:
  - Bullet-point notes  
  - Clean structured summaries  
  - Key concepts + definitions  
  - Multi-section insights  

### ✅ 2. Quiz Generator  

Generate quizzes **from the original PDF text**, not the summary.

**Two quiz modes:**

#### • MCQ Mode  

- Question  
- 4 Options  
- Correct Answer  

#### • Mixed Mode  

- MCQs  
- True/False  
- Short-Answer Questions  

---

## 🧩 Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Gemini CLI** | Orchestration & model execution |
| **OpenAgents SDK** | Agent logic, tool calling |
| **Context7 MCP** | Tool provider (filesystem, memory, etc.) |
| **PyPDF** | Extract text from PDF |
| **Streamlit** | App UI |
| **Python 3.11+** | Backend |

---

# 📁 Folder Structure

project/
│
├── gemini.md # Master prompt for Gemini CLI agent
├── README.md # Documentation
├── app.py # Streamlit interface
│
├── modules/
│ ├── extractor.py # PDF → text extraction
│ ├── summarizer.py # Summary generation logic
│ ├── quiz_mcq.py # MCQ-only quiz generator
│ ├── quiz_mixed.py # Mixed-style quiz generator
│
├── assets/
│ └── samples/ # Sample PDFs
│
└── requirements.txt

yaml
Copy code

---

# 📌 How It Works (Flow)

### **1. User uploads a PDF**

→ Saved into memory or filesystem  
→ Passed to PyPDF  

### **2. PyPDF extracts clean text**

→ Returned to agent  

### **3. Agent generates summary**

→ Structured clean notes  

### **4. User clicks "Create Quiz"**

→ Agent reads full PDF text  
→ Generates MCQs or Mixed questions  

### **5. Streamlit displays quiz**

→ User can review or export  

---

# 🚀 Running the App

### **1. Install dependencies**

pip install -r requirements.txt

shell
Copy code

### **2. Launch the Streamlit app**

streamlit run app.py

graphql
Copy code

### **3. Run Gemini CLI with your prompt**

gemini run gemini.md

yaml
Copy code

---

# 🧠 gemini.md (Agent Prompt)

The full agent logic lives inside `gemini.md`.  
It defines:

- System instructions  
- Tool usage  
- How summaries should be generated  
- How quizzes should be formatted  
- How to interact with Context7 tools  
- Code generation rules  

Use the `gemini.md` to control behavior.

---

# 📌 Quiz Format Rules

### **MCQ Format**

Q1: ...
A. Option 1
B. Option 2
C. Option 3
D. Option 4
Correct Answer: C

markdown
Copy code

### **Mixed Format**

MCQ:
Q1: ...
A. Option A
Correct Answer: B

True/False:
Q2: ...
Answer: True

Short Answer:
Q3: ...
Answer (expected keywords): ...

yaml
Copy code

---

# 🛠️ Modules Required

### **PDF Extraction**

- Uses PyPDF  
- Cleans text  
- Removes headers/footers  

### **Summary Generator**

- Uses Gemini model  
- Produces clear multi-level notes  

### **MCQ Generator**

- Uses raw PDF text  
- No hallucinated questions  

### **Mixed Quiz Generator**

- Higher-order question types  

---

# 🌐 Deployment (Optional)

Deploy on:

- Streamlit Cloud  
- Railway  
- Vercel (via API backend)  
- Docker  

---

# 📞 Support

Modify `gemini.md` to change:

- Agent behavior  
- Response formatting  
- Quiz structure  
- Streamlit UI style  

---

# ✅ Status

**Fully configurable AI Study Engine**  
Built for students, educators, and content creators.
