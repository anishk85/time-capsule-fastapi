# 🚀 Digital Time Capsule - FastAPI Backend

## 📌 Overview

The **FastAPI backend** is an essential part of the **Digital Time Capsule** project, responsible for **AI-powered sentiment analysis** of messages stored in capsules. This microservice provides **fast, efficient, and scalable** NLP-based analysis, enhancing user interaction with AI-generated insights.

---

## **🛠 Technologies Used**

- **FastAPI** – High-performance Python web framework
- **Transformers & DistilBERT** – NLP-based sentiment analysis
- **Torch** – Optimized deep learning inference
- **Uvicorn** – Fast ASGI server for deployment
- **Render** – Cloud hosting for FastAPI service

---

## **🔧 Installation & Setup**

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/anishk85/time-capsule
cd time-capsule/ai-backend
```

### **2️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**

Create a **.env** file inside `ai-backend` and add:

```sh
MODEL_NAME=bhadresh-savani/distilbert-base-uncased-emotion
```

### **4️⃣ Run the FastAPI Server Locally(optional)**

```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## **🌎 Deployment**

- **Render** is used for hosting the FastAPI backend.
- Update the `FASTAPI_URL` in the main backend's **.env** file:

```sh
FASTAPI_URL=https://your-fastapi-url.onrender.com/analyze
```

---

## **📌 API Endpoints**

| Method   | Endpoint   | Description                            |
| -------- | ---------- | -------------------------------------- |
| **POST** | `/analyze` | Analyzes the sentiment of a given text |

Example Request:

```json
{
  "message": "I am feeling happy today!"
}
```

Example Response:

```json
{
  "label": "joy",
  "
}
```

---

## **📌 Conclusion**

The **FastAPI backend** enhances the **Digital Time Capsule** by providing **AI-powered sentiment analysis**, ensuring an **interactive and intelligent** user experience. 🚀

