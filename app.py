from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    scores = {
        "Urban Explorer": 0,
        "Adventure Seeker": 0,
        "Nature Lover": 0,
        "Cultural Explorer": 0
    }

    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")


    if q1 == "city":   
        scores["Urban Explorer"] += 2 
    elif q1 == "adventure":
        scores["Adventure Seeker"] += 2
    elif q1 == "nature":
        scores["Nature Lover"] += 2
    elif q1 == "culture":
     scores["Cultural Explorer"] += 2


    if q2 == "shopping":
        scores["Urban Explorer"] += 2
    elif q2 == "sports":
        scores["Adventure Seeker"] += 2
    elif q2 == "forest":
        scores["Nature Lover"] += 2
    elif q2 == "museum":
        scores["Cultural Explorer"] += 2


    if q3 == "hotel":
        scores["Urban Explorer"] += 2
    elif q3 == "camp":
        scores["Adventure Seeker"] += 2
    elif q3 == "cabin":
        scores["Nature Lover"] += 2
    elif q3 == "heritage":
        scores["Cultural Explorer"] += 2


    if q4 == "tokyo":
        scores["Urban Explorer"] += 2
    elif q4 == "nepal":
        scores["Adventure Seeker"] += 2
    elif q4 == "switzerland":
        scores["Nature Lover"] += 2
    elif q4 == "rome":
        scores["Cultural Explorer"] += 2

    personality = max(scores, key=scores.get)

    return render_template(
        "result.html",
        personality=personality
 )


if __name__ == "__main__":
    app.run(debug=True)