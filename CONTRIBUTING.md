# Contributing

Thanks for wanting to improve Travel Personality Analyzer. The quiz, the result page, and the copy are all in this repository, so small changes are easy to try locally.

## Set up

You need Python 3.12.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
python app.py
```

Open http://127.0.0.1:5001 and take the quiz once before you change scoring or templates.

## Tests

```bash
pytest
```

Add a test when you change scoring, the itinerary endpoint, or anything that handles form input. The existing tests cover the homepage, a full result, and the itinerary escaping.

## Pull requests

1. Branch from `main`.
2. Keep the change focused. A quiz question and a documentation rewrite are easier to review separately.
3. Run `pytest` before you push.
4. Describe what a visitor can do after the change.
5. Do not commit `.env`, screenshots of someone else's personal data, or API keys. This app does not need keys.

## Project notes

- Personality text, destinations, and itinerary lines live in `app.py`.
- The homepage quiz is `templates/index.html` plus `static/quiz.js`.
- The result page is `templates/result.html` plus `static/results.js`.
- Each answer adds 2 points to one of the four travel styles. If you add a question, give every option a value that exists in `answer_map`, and keep `total_questions` in sync with the form.
- User-controlled text that is turned into HTML must be escaped. The itinerary endpoint is the place this matters.
- Leave `FLASK_DEBUG` off unless you are on your own machine.

## Reporting a vulnerability

Please use the process in [SECURITY.md](SECURITY.md) instead of opening a public issue.
