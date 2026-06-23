from flask import Flask, render_template, request

app = Flask(__name__)

answer_map = {
    "city": "Urban Explorer",
    "shopping": "Urban Explorer",
    "technology": "Urban Explorer",
    "nightlife": "Urban Explorer",
    "metro": "Urban Explorer",
    "skyline": "Urban Explorer",
    "hotel": "Urban Explorer",
    "planned": "Urban Explorer",
    "group": "Urban Explorer",

    "adventure": "Adventure Seeker",
    "sports": "Adventure Seeker",
    "trekking": "Adventure Seeker",
    "extreme": "Adventure Seeker",
    "camping": "Adventure Seeker",
    "spontaneous": "Adventure Seeker",
    "highrisk": "Adventure Seeker",
    "backpack": "Adventure Seeker",

    "nature": "Nature Lover",
    "forest": "Nature Lover",
    "mountains": "Nature Lover",
    "wildlife": "Nature Lover",
    "countryside": "Nature Lover",
    "lowbudget": "Nature Lover",
    "solo": "Nature Lover",
    "quiet": "Nature Lover",

    "culture": "Cultural Explorer",
    "museum": "Cultural Explorer",
    "history": "Cultural Explorer",
    "architecture": "Cultural Explorer",
    "localfood": "Cultural Explorer",
    "guesthouse": "Cultural Explorer",
    "midbudget": "Cultural Explorer",
    "highbudget": "Cultural Explorer",
}

personality_info = {
    "Urban Explorer": {
        "description": "You enjoy modern cities, shopping, technology and busy urban life.",
        "strengths": [
            "Good at navigating new cities quickly",
            "Comfortable with public transport and metro systems",
            "Enjoys trying new restaurants and food spots",
            "Adapts fast to fast-paced environments"
        ],
        "weaknesses": [
            "Can get tired of too much nature or silence",
            "Sometimes overspends on city experiences",
            "May skip slower, traditional experiences"
        ],
        "trip_type": "City Hopping",
        "environment": "Modern Cities",
        "trip_length": "7 - 10 Days",
        "season": "Spring",
        "budget": "Medium to High",
        "daily_cost_low": 4000,
        "daily_cost_mid": 8000,
        "daily_cost_high": 16000,
        "places": [
            {
                "name": "Tokyo, Japan",
                "description": "A high tech city with neon streets, bullet trains and endless things to do.",
                "budget": "Medium to High",
                "season": "Spring",
                "trip_length": "7 - 9 Days",
                "why": "You enjoy modern cities and technology."
            },
            {
                "name": "Singapore",
                "description": "A clean, futuristic city state known for its skyline and food culture.",
                "budget": "Medium to High",
                "season": "Year Round",
                "trip_length": "5 - 7 Days",
                "why": "You like organised cities with great transport and shopping."
            },
            {
                "name": "Seoul, South Korea",
                "description": "A fast moving city with a mix of technology, fashion and nightlife.",
                "budget": "Medium",
                "season": "Autumn",
                "trip_length": "6 - 8 Days",
                "why": "You enjoy busy streets, shopping districts and city nightlife."
            },
            {
                "name": "Dubai, UAE",
                "description": "Tall buildings, malls and a city built around modern luxury.",
                "budget": "High",
                "season": "Winter",
                "trip_length": "5 - 7 Days",
                "why": "You like big city energy and modern architecture."
            }
        ],
        "tips": [
            "Use public transportation to get around like a local",
            "Visit local neighborhoods, not just tourist spots",
            "Explore city centers at night when they look different",
            "Book accommodation close to a metro line to save time",
            "Try street food instead of only restaurants",
            "Keep a loose plan so you can explore on foot"
        ],
        "fun_facts": [
            "Urban Explorers often prefer destinations with extensive public transportation systems.",
            "Most Urban Explorers say walking is their favorite way to discover a new city.",
            "Cities with strong nightlife usually score high with Urban Explorer travellers."
        ],
        "packing": [
            "Comfortable walking shoes",
            "Portable phone charger / power bank",
            "Metro card or transit pass",
            "Light jacket for night walks",
            "Universal travel adapter",
            "Daypack for city walking",
            "Camera or phone for photos",
            "Cash in local currency"
        ]
    },
    "Adventure Seeker": {
        "description": "You enjoy excitement, challenges and outdoor adventures.",
        "strengths": [
            "Comfortable with physical challenges",
            "Open to spontaneous plans and last minute changes",
            "Handles uncomfortable situations well",
            "Looks for new experiences instead of relaxing trips"
        ],
        "weaknesses": [
            "Might ignore proper rest during a trip",
            "Can underestimate risk in extreme activities",
            "Sometimes books trips with too little planning"
        ],
        "trip_type": "Adventure Trip",
        "environment": "Mountains and Outdoors",
        "trip_length": "10 - 14 Days",
        "season": "Summer",
        "budget": "Medium",
        "daily_cost_low": 3000,
        "daily_cost_mid": 6500,
        "daily_cost_high": 13000,
        "places": [
            {
                "name": "Nepal",
                "description": "Home to the Himalayas and some of the best trekking routes on earth.",
                "budget": "Medium",
                "season": "Autumn",
                "trip_length": "10 - 14 Days",
                "why": "You enjoy trekking and high adventure tolerance."
            },
            {
                "name": "New Zealand",
                "description": "A country built for outdoor adventure, from bungee jumping to hiking.",
                "budget": "Medium to High",
                "season": "Summer",
                "trip_length": "10 - 12 Days",
                "why": "You like extreme sports and outdoor challenges."
            },
            {
                "name": "Patagonia, Chile",
                "description": "A remote region with glaciers, mountains and long distance trails.",
                "budget": "Medium",
                "season": "Summer",
                "trip_length": "12 - 14 Days",
                "why": "You enjoy raw nature combined with physical challenge."
            },
            {
                "name": "Manali, India",
                "description": "A mountain town with trekking trails, river rafting and paragliding.",
                "budget": "Low to Medium",
                "season": "Summer",
                "trip_length": "5 - 7 Days",
                "why": "You like easy access to outdoor adventure activities."
            }
        ],
        "tips": [
            "Pack light but always bring proper gear for the activity",
            "Book adventure activities a few days in advance",
            "Talk to local guides, they know hidden trails",
            "Keep a basic first aid kit with you",
            "Check weather conditions before heading into the mountains",
            "Leave some days unplanned for spontaneous activities"
        ],
        "fun_facts": [
            "Adventure Seekers usually rank trekking as their top travel activity.",
            "Most Adventure Seekers prefer trip itineraries with at least one flexible day.",
            "Mountain destinations score highest in matches for this personality type."
        ],
        "packing": [
            "Sturdy hiking shoes",
            "Quick dry clothing",
            "Rain jacket",
            "Small first aid kit",
            "Headlamp or flashlight",
            "Refillable water bottle",
            "Power bank",
            "Backpack with rain cover"
        ]
    },
    "Nature Lover": {
        "description": "You enjoy peaceful environments and beautiful landscapes.",
        "strengths": [
            "Great at slowing down and enjoying the moment",
            "Comfortable travelling solo or in small groups",
            "Appreciates simple, low cost experiences",
            "Notices small details in nature others miss"
        ],
        "weaknesses": [
            "May get bored in busy or crowded cities",
            "Can avoid destinations with heavy tourism",
            "Sometimes skips cultural sites for nature spots"
        ],
        "trip_type": "Nature Escape",
        "environment": "Countryside and Wilderness",
        "trip_length": "5 - 8 Days",
        "season": "Autumn",
        "budget": "Low to Medium",
        "daily_cost_low": 2500,
        "daily_cost_mid": 5500,
        "daily_cost_high": 11000,
        "places": [
            {
                "name": "Switzerland",
                "description": "Calm lakes, snowy peaks and quiet countryside villages.",
                "budget": "Medium to High",
                "season": "Summer",
                "trip_length": "6 - 8 Days",
                "why": "You enjoy peaceful landscapes and mountain views."
            },
            {
                "name": "Norway",
                "description": "Fjords, forests and small towns far from crowded cities.",
                "budget": "Medium to High",
                "season": "Summer",
                "trip_length": "7 - 9 Days",
                "why": "You like quiet environments and natural scenery."
            },
            {
                "name": "Iceland",
                "description": "A land of waterfalls, volcanoes and wide open countryside.",
                "budget": "Medium",
                "season": "Summer",
                "trip_length": "5 - 7 Days",
                "why": "You enjoy untouched nature and slower paced travel."
            },
            {
                "name": "Munnar, India",
                "description": "Tea gardens, misty hills and a slow paced quiet atmosphere.",
                "budget": "Low",
                "season": "Winter",
                "trip_length": "3 - 5 Days",
                "why": "You like quiet countryside without the high cost of flights."
            }
        ],
        "tips": [
            "Rent a car so you can stop wherever the view looks good",
            "Travel slightly outside peak season for fewer crowds",
            "Pack for changing weather in countryside areas",
            "Choose smaller guesthouses over big hotels",
            "Bring a camera, nature trips are easy to forget photos for",
            "Plan fewer locations and spend more time in each one"
        ],
        "fun_facts": [
            "Nature Lovers often prefer destinations with low population density.",
            "Most Nature Lovers say a quiet evening view matters more than nightlife.",
            "Countryside trips score higher for this personality than big city trips."
        ],
        "packing": [
            "Comfortable outdoor shoes",
            "Light layers for changing weather",
            "Insect repellent",
            "Sunscreen",
            "Camera or binoculars",
            "Reusable water bottle",
            "Small backpack",
            "Power bank, charging points may be limited"
        ]
    },
    "Cultural Explorer": {
        "description": "You love history, museums and cultural experiences.",
        "strengths": [
            "Genuinely interested in learning about new places",
            "Patient with longer museum and heritage tours",
            "Respectful of local customs and traditions",
            "Plans trips with a clear structure"
        ],
        "weaknesses": [
            "Can over plan and leave little room for spontaneity",
            "May spend too much time reading instead of exploring",
            "Sometimes skips outdoor adventure activities"
        ],
        "trip_type": "Cultural Tour",
        "environment": "Historic Cities",
        "trip_length": "6 - 9 Days",
        "season": "Spring",
        "budget": "Medium",
        "daily_cost_low": 3500,
        "daily_cost_mid": 7000,
        "daily_cost_high": 14000,
        "places": [
            {
                "name": "Rome, Italy",
                "description": "Ancient ruins, classic architecture and centuries of history.",
                "budget": "Medium",
                "season": "Spring",
                "trip_length": "6 - 8 Days",
                "why": "You enjoy history and architecture from past centuries."
            },
            {
                "name": "Kyoto, Japan",
                "description": "Traditional temples, gardens and a slower paced culture.",
                "budget": "Medium",
                "season": "Spring",
                "trip_length": "6 - 8 Days",
                "why": "You like traditional culture and historical sites."
            },
            {
                "name": "Athens, Greece",
                "description": "The birthplace of ancient history with museums on every corner.",
                "budget": "Medium",
                "season": "Spring",
                "trip_length": "5 - 7 Days",
                "why": "You enjoy ancient history and cultural landmarks."
            },
            {
                "name": "Jaipur, India",
                "description": "Forts, palaces and a city full of color and history.",
                "budget": "Low to Medium",
                "season": "Winter",
                "trip_length": "3 - 5 Days",
                "why": "You enjoy heritage architecture without a long flight."
            }
        ],
        "tips": [
            "Book guided tours for the major historical sites",
            "Try local food instead of international chains",
            "Visit museums early to avoid large tour groups",
            "Read a little history before visiting a heritage site",
            "Talk to locals, they often know stories guidebooks miss",
            "Balance museum days with slower café or walking days"
        ],
        "fun_facts": [
            "Cultural Explorers usually rate museums as a top travel activity.",
            "Most Cultural Explorers prefer mid range budgets with planned itineraries.",
            "Historic cities consistently score highest for this personality type."
        ],
        "packing": [
            "Comfortable walking shoes",
            "Modest clothing for religious or heritage sites",
            "Small notebook or travel journal",
            "Camera",
            "Portable charger",
            "Day bag for museum visits",
            "Printed or downloaded museum tickets",
            "Light scarf or shawl"
        ]
    }
}

total_questions = 15


def calculate_results(form_data):
    scores = {
        "Urban Explorer": 0,
        "Adventure Seeker": 0,
        "Nature Lover": 0,
        "Cultural Explorer": 0
    }

    question_number = 1
    while True:
        field_name = "q" + str(question_number)
        if field_name not in form_data and question_number > total_questions:
            break
        answer = form_data.get(field_name)
        if answer in answer_map:
            personality = answer_map[answer]
            scores[personality] = scores[personality] + 2
        question_number = question_number + 1
        if question_number > total_questions:
            break

    total_score = 0
    for personality in scores:
        total_score = total_score + scores[personality]

    if total_score == 0:
        total_score = 1

    percentages = {}
    for personality in scores:
        percentages[personality] = round((scores[personality] / total_score) * 100)

    sorted_scores = sorted(percentages.items(), key=lambda item: item[1], reverse=True)

    primary = sorted_scores[0][0]
    secondary = sorted_scores[1][0]

    top_score = sorted_scores[0][1]
    second_score = sorted_scores[1][1]

    if top_score >= 75:
        confidence_label = "Very Strong Match"
    elif top_score >= 50:
        confidence_label = "Strong Match"
    else:
        confidence_label = "Mixed Personality"

    gap = top_score - second_score
    match_score = top_score + round(gap / 2)
    if match_score > 100:
        match_score = 100

    result = {}
    result["scores"] = scores
    result["percentages"] = percentages
    result["sorted_scores"] = sorted_scores
    result["primary"] = primary
    result["secondary"] = secondary
    result["confidence_label"] = confidence_label
    result["match_score"] = match_score
    return result


def build_maps_link(place_name):
    query = place_name.replace(" ", "+").replace(",", "%2C")
    return "https://www.google.com/maps/search/?api=1&query=" + query


def build_skyscanner_link(place_name):
    query = place_name.split(",")[0].strip().replace(" ", "-").lower()
    return "https://www.skyscanner.net/transport/flights-to/" + query + "/"


def build_booking_link(place_name):
    query = place_name.replace(" ", "+").replace(",", "")
    return "https://www.booking.com/searchresults.html?ss=" + query


def build_whatsapp_link(text):
    message = text.replace(" ", "%20").replace("\n", "%0A")
    return "https://wa.me/?text=" + message


@app.route("/")
def home():
    return render_template("index.html", total_questions=total_questions)


@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name")
    if not name:
        name = "Traveller"

    results = calculate_results(request.form)

    primary = results["primary"]
    secondary = results["secondary"]

    primary_info = personality_info[primary]
    secondary_info = personality_info[secondary]

    chart_labels = []
    chart_values = []
    for item in results["sorted_scores"]:
        chart_labels.append(item[0])
        chart_values.append(item[1])

    places_with_links = []
    for place in primary_info["places"]:
        place_copy = dict(place)
        place_copy["maps_link"] = build_maps_link(place["name"])
        place_copy["skyscanner_link"] = build_skyscanner_link(place["name"])
        place_copy["booking_link"] = build_booking_link(place["name"])
        places_with_links.append(place_copy)

    share_text = name + " got " + primary + " as their travel personality on Travel Personality Analyzer! Take the quiz and find your travel style."
    whatsapp_link = build_whatsapp_link(share_text)

    return render_template(
        "result.html",
        name=name,
        primary=primary,
        secondary=secondary,
        primary_info=primary_info,
        secondary_info=secondary_info,
        percentages=results["percentages"],
        sorted_scores=results["sorted_scores"],
        confidence_label=results["confidence_label"],
        match_score=results["match_score"],
        chart_labels=chart_labels,
        chart_values=chart_values,
        places=places_with_links,
        whatsapp_link=whatsapp_link
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
