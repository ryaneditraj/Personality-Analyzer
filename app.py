from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    name = request.form.get("name")
    
    scores = {
        "Urban Explorer": 0,
        "Adventure Seeker": 0,
        "Nature Lover": 0,
        "Cultural Explorer": 0
    }

    answers = []

    for i in range(1, 9):
        answer = request.form.get(f"q{i}")
        answers.append(answer)

    answer_map = {
        "city": "Urban Explorer",
        "shopping": "Urban Explorer",
        "technology": "Urban Explorer",
        "nightlife": "Urban Explorer",

        "adventure": "Adventure Seeker",
        "sports": "Adventure Seeker",
        "trekking": "Adventure Seeker",
        "extreme": "Adventure Seeker",

        "nature": "Nature Lover",
        "forest": "Nature Lover",
        "mountains": "Nature Lover",
        "wildlife": "Nature Lover",

        "culture": "Cultural Explorer",
        "museum": "Cultural Explorer",
        "history": "Cultural Explorer",
        "architecture": "Cultural Explorer"
    }

    for answer in answers:
        if answer in answer_map:
            scores[answer_map[answer]] += 2

    total_score = sum(scores.values())

    percentages = {}

    for personality, score in scores.items():
        percentages[personality] = round(
            (score / total_score) * 100
        )

    personality = max(scores, key=scores.get)

    personality_info = {
        "Urban Explorer": {
            "badge": "🏙🏙",
            "description": "You enjoy modern cities, shopping, technology and busy urban life.",
            "places": ["Tokyo", "Singapore", "Seoul"]
        },
        "Adventure Seeker": {
            "badge": "🏔🏙",
            "description": "You enjoy excitement, challenges and outdoor adventures.",
            "places": ["Nepal", "New Zealand", "Patagonia"]
        },
        "Nature Lover": {
            "badge": "🌲",
            "description": "You enjoy peaceful environments and beautiful natural landscapes.",
            "places": ["Switzerland", "Iceland", "Norway"]
        },
        "Cultural Explorer": {
            "badge": "🌲🏙",
            "description": "You love history, culture, traditions and heritage sites.",
            "places": ["Rome", "Kyoto", "Athens"]
        }
    }

    return render_template(
        "result.html",
       name=name,
        personality=personality,
        percentages=percentages,
        details=personality_info[personality]
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)