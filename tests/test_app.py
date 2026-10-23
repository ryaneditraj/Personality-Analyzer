import app as quiz


def urban_answers():
    return {
        "name": "Ava",
        "q1": "city",
        "q2": "shopping",
        "q3": "technology",
        "q4": "nightlife",
        "q5": "city",
        "q6": "metro",
        "q7": "shopping",
        "q8": "city",
        "q9": "technology",
        "q10": "hotel",
        "q11": "group",
        "q12": "skyline",
        "q13": "planned",
        "q14": "metro",
        "q15": "technology",
    }


def test_homepage_is_the_quiz():
    client = quiz.app.test_client()
    response = client.get("/")
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Travel Personality Quiz" in page
    assert 'name="q1"' in page
    assert 'name="q15"' in page
    assert "application/ld+json" in page
    assert "What is the Travel Personality Analyzer?" in page
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert "script-src" in response.headers["Content-Security-Policy"]


def test_result_scores_a_city_traveller_and_escapes_the_name():
    client = quiz.app.test_client()
    payload = urban_answers()
    payload["name"] = '<img src=x onerror="alert(1)">'
    response = client.post("/result", data=payload)
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Urban Explorer" in page
    assert "Tokyo, Japan" in page
    assert "<img src=x" not in page
    assert "&lt;img" in page
    assert response.headers["Cache-Control"] == "no-store"
    assert "skyscanner.net/transport/flights-to/tokyo/" in page


def test_empty_submission_still_renders():
    client = quiz.app.test_client()
    response = client.post("/result", data={})
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Traveller" in page


def test_itinerary_escapes_destination_html():
    client = quiz.app.test_client()
    response = client.post(
        "/build-itinerary",
        data={
            "personality": "Urban Explorer",
            "place_name": '<script>alert(1)</script>',
            "days": "2",
        },
    )
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "<script>" not in page
    assert "&lt;script&gt;" in page
    assert "Day 1" in page
    assert "Day 2" in page


def test_itinerary_rejects_unknown_personality_and_bad_days():
    client = quiz.app.test_client()

    unknown = client.post(
        "/build-itinerary",
        data={"personality": "<script>", "place_name": "Tokyo", "days": "3"},
    )
    assert unknown.status_code == 400
    assert "<script>" not in unknown.get_data(as_text=True)

    bad_days = client.post(
        "/build-itinerary",
        data={"personality": "Nature Lover", "place_name": "Iceland", "days": "five"},
    )
    assert bad_days.status_code == 400


def test_share_links_encode_reserved_characters():
    client = quiz.app.test_client()
    payload = urban_answers()
    payload["name"] = "Ava & Lee"
    response = client.post("/result", data=payload)
    page = response.get_data(as_text=True)

    assert "wa.me/?text=" in page
    assert "Ava%20%26%20Lee" in page or "Ava+%26+Lee" in page


def test_discovery_files():
    client = quiz.app.test_client()

    robots = client.get("/robots.txt")
    assert robots.status_code == 200
    assert "Disallow: /result" in robots.get_data(as_text=True)
    assert "Sitemap:" in robots.get_data(as_text=True)

    sitemap = client.get("/sitemap.xml")
    assert sitemap.status_code == 200
    assert "<loc>" in sitemap.get_data(as_text=True)

    llms = client.get("/llms.txt")
    text = llms.get_data(as_text=True)
    assert llms.status_code == 200
    assert "Travel Personality Analyzer" in text
    assert "Ryan Editraj" in text


def test_debug_is_off_unless_requested(monkeypatch):
    monkeypatch.delenv("FLASK_DEBUG", raising=False)
    assert quiz.debug_enabled() is False
    monkeypatch.setenv("FLASK_DEBUG", "1")
    assert quiz.debug_enabled() is True
