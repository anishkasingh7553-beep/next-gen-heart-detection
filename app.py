from flask import Flask, render_template, request

app = Flask(__name__)

prediction_data = {}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    global prediction_data

    age = int(request.form['age'])
    bp = int(request.form['bp'])
    cholesterol = int(request.form['cholesterol'])
    sugar = int(request.form['sugar'])
    heart_rate = int(request.form['heart_rate'])

    score = 0

    if age > 50:
        score += 20
    if bp > 140:
        score += 20
    if cholesterol > 200:
        score += 20
    if sugar > 120:
        score += 20
    if heart_rate > 100:
        score += 20

    if score >= 60:
        result = "High Risk"
        suggestion = "Immediate medical consultation, low-fat diet, regular monitoring and daily walking."
    elif score >= 30:
        result = "Moderate Risk"
        suggestion = "Monitor health regularly and improve diet."
    else:
        result = "Low Risk"
        suggestion = "Maintain healthy lifestyle."

    prediction_data = {
        "prediction": result,
        "suggestion": suggestion,
        "score": score
    }

    return render_template(
        'index.html',
        prediction=result,
        suggestion=suggestion,
        score=score
    )


@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query'].lower()

    if "diet" in user_query:
        answer = "Recommended: fruits, vegetables, oats and low-oil food."
    elif "exercise" in user_query:
        answer = "30 minutes walking or light cardio daily is beneficial."
    elif "bp" in user_query:
        answer = "Reduce salt intake and monitor blood pressure daily."
    else:
        answer = "Please consult a healthcare professional for detailed advice."

    return render_template(
        'index.html',
        prediction=prediction_data.get("prediction"),
        suggestion=prediction_data.get("suggestion"),
        score=prediction_data.get("score"),
        answer=answer
    )


if __name__ == '__main__':
    app.run(debug=True)