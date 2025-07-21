import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 SMS Spam Classifier")

message = st.text_area("Enter your message:")

if st.button("Predict"):
    if message.strip() != "":
        msg_vector = vectorizer.transform([message])
        prediction = model.predict(msg_vector)
        result = "🚫 Spam" if prediction[0] == "spam" else "✅ Not Spam"
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter a message.")
