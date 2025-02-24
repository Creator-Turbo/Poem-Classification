from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


# Load the trained model
with open("model/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the vectorizer (TF-IDF or CountVectorizer)
with open("model/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    poem_text = request.form["poem"]
    transformed_text = vectorizer.transform([poem_text])
    prediction = model.predict(transformed_text)[0]
    
    return render_template("result.html", poem=poem_text, category=prediction)

if __name__ == "__main__":
    app.run(debug=True)
