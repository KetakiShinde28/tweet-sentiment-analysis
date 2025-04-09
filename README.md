# 🧠 Tweet Sentiment & Emotion Classifier

A full-stack sentiment analysis app that predicts **emotions** (like *joy*, *anger*, *sadness*, etc.) from tweets using a trained machine learning model. Built with **Flask** for the backend and **React** for the frontend.

---

## 📁 Project Structure

```
tweet-sentiment-analysis/
│
├── backend/
│   ├── app.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── model/ (auto-created after training)
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── App.css
│       ├── index.js
│       └── index.css
│
└── README.md
```

---

## ⚙️ 1. Backend Setup

1. Open terminal and navigate to the backend folder:

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Download the dataset from [Emotion Dataset](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp) and place it inside a new folder named `data` like this:

```
backend/
└── data/
    ├── train.txt
    ├── test.txt
    └── val.txt
```

4. Train the model:

```bash
python train_model.py
```

✅ This creates `sentiment_model.pkl` and `vectorizer.pkl` inside `model/` folder.

5. Run the Flask server:

```bash
python app.py
```

By default, it runs on: `http://localhost:5000`

---

## 💅 2. Frontend Setup

1. Open a new terminal window, go to the frontend folder:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React app:

```bash
npm start
```

The app runs on: `http://localhost:3000`

---

## 🔹 3. How to Use

1. Start both backend and frontend.
2. Go to `http://localhost:3000` in your browser.
3. Type a tweet or sentence and click **Analyze Sentiment**.
4. The result will show an emotion like `joy`, `anger`, `sadness`, etc.

---

### 🔹 4. Important: Files Not Included in This Repo

To keep the repository clean and due to GitHub file size limitations, some folders/files are intentionally not pushed:

| Not Uploaded       | Reason |
|--------------------|--------|
| `node_modules/`     | Auto-generated during `npm install` |
| `venv/` (or `.venv/`)| Virtual environments shouldn't be version-controlled |
| `model/`            | Created after training the model |
| `data/`             | You must manually download the dataset |
| `__pycache__/`      | Python cache files are excluded |

📌 **But don't worry!** Everything you need is here. Just follow the setup steps above, and you'll be up and running in minutes.

Refer to these files in the repo:
- **Backend**: `app.py`, `train_model.py`, `preprocess.py`
- **Frontend**: `App.js`, `App.css`, and other React files under `src/`

---

## 🚀 Technologies Used

- Python, Flask, scikit-learn, NLTK
- React.js, Axios, CSS

---

## 🙌 Author

Made with 💖 by Ketaki Shinde
