**README.md:**

```
# Automated Code Generator

## Setup:

### Backend:

1. Navigate to the backend directory:
```
cd backend
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. Run the Flask API:
```
python app.py
```

### Frontend:

1. Navigate to the frontend directory:
```
cd frontend
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. Run the Streamlit app:
```
streamlit run streamlit_app.py
```

## Usage:

1. Open the Streamlit app in your browser.
2. Enter a natural language description of the software requirement.
3. Click "Generate Code" to get the corresponding code snippet.
```

**Note**: The Hugging Face model used here (`gpt2-medium`) is just an example. You can choose other models from the Hugging Face model hub. However, remember that the model isn't specifically trained for code generation, so the results might not always be accurate. Fine-tuning the model on a code generation dataset would yield better results.