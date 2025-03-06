# 🚀 GoogleHackBackend - AI News Summarizer

&#x20;  &#x20;

📰 **GoogleHackBackend** is a **FastAPI-powered backend server** that fetches news articles from **NewsAPI** and summarizes them into concise, child-friendly versions using **Gemini 2.0 Flash**.

🚀 **Upgraded from Gemini Pro to Gemini 2.0 Flash** for better speed & efficiency!

---

## 📖 Features

✅ **Fetches real-time news** from [NewsAPI](https://newsapi.org/)\
✅ **Summarizes articles** using [Gemini 2.0 Flash](https://ai.google.dev/)\
✅ **Child-friendly summaries** with easy-to-understand language\
✅ **FastAPI-based** lightweight backend\
✅ **Cross-Origin Resource Sharing (CORS) enabled**\
✅ **Deployed on Vercel** for seamless scalability

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DebaratiD/GoogleHackBackend.git
cd GoogleHackBackend
```

### 2️⃣ Install Dependencies

Ensure you have Python **3.8+** installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys

Create a `.env` file and add the following:

```
NEWSAPI_KEY=your_newsapi_key_here
GOOGLE_GEMINI_KEY=your_gemini_api_key_here
```

- Get a **NewsAPI Key** from [newsapi.org](https://newsapi.org/).
- Get a **Gemini AI Key** from [Google AI](https://ai.google.dev/).

### 4️⃣ Run the FastAPI Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- Open `http://127.0.0.1:8000/docs` for **Swagger UI** API testing.
- Open `http://127.0.0.1:8000/redoc` for **Redoc** API documentation.

---

## 🔥 API Endpoints

| Method | Endpoint     | Description                          |
| ------ | ------------ | ------------------------------------ |
| `GET`  | `/news`      | Fetches the latest news from NewsAPI |
| `POST` | `/getstory`  | Summarizes a given news article      |

📌 **Example Request for **``:

```json
{
  "ques": "What is FastAPI?"
}
```

📌 **Example Response**:

```json
{
  "summary": "A short, child-friendly version of the article."
}
```

---

## 🛠 Deployment

This project is deployed on **Vercel**. To deploy manually:

```bash
vercel --prod
```

---

## 🤝 Contributing

Want to contribute? Follow these steps:

1. **Fork** the repository.
2. **Create a new feature branch**: `git checkout -b feature-name`
3. **Commit changes**: `git commit -m "Added new feature"`
4. **Push to your branch**: `git push origin feature-name`
5. **Submit a Pull Request** 🎉

---


## 📩 Contact

For any queries or collaborations, feel free to reach out:

- **GitHub**: [DebaratiD](https://github.com/DebaratiD)
- **Email**: [debaratidatta.77star@gmail.com](mailto\:debaratidatta.77star@gmail.com)

---

### ⭐ If you like this project, don't forget to star ⭐ the repository!

🚀 Happy coding! 🎉

