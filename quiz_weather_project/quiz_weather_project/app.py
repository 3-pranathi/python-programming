from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ---------------- WEATHER CONFIG ----------------
API_KEY = "92ae672786a1a580be30806e815e20ba" 
BASEURL = "https://api.openweathermap.org/data/2.5/weather"

# ---------------- QUIZ QUESTIONS ----------------
quiz_questions = [
   {
        "question": "Which instrument is used to measure temperature?",
        "options": ["Barometer", "Thermometer", "Anemometer", "Hygrometer"],
        "answer": "Thermometer"
    },
    {
        "question": "What does a barometer measure?",
        "options": ["Humidity", "Wind speed", "Air pressure", "Rainfall"],
        "answer": "Air pressure"
    },
    {
        "question": "Which gas is mainly responsible for the greenhouse effect?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
]

@app.route("/", methods=["GET", "POST"])
def dashboard():
    weather = None
    error = None
    score = None

    if request.method == "POST":
        # -------- WEATHER LOGIC --------
        city = request.form.get("city")

        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            response = requests.get(BASEURL, params=params)

            if response.status_code == 200:
                data = response.json()
                weather = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"]
                }
            else:
                error = "City not found"

        # -------- QUIZ LOGIC --------
        score = 0
        for i, q in enumerate(quiz_questions):
            user_answer = request.form.get(f"q{i}")
            if user_answer == q["answer"]:
                score += 1
    return render_template(
        "dashboard.html",
        weather=weather,
        quiz_questions=quiz_questions,
        score=score,
        error=error
    )
if __name__ == "__main__":
    app.run(debug=True)
