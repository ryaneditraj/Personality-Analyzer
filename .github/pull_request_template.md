## Summary

What does this change do for someone taking the quiz?

## How to test

1. `pip install -r requirements.txt -r requirements-dev.txt`
2. `pytest`
3. `python app.py` and try the affected page

## Checklist

- [ ] Tests pass locally
- [ ] No `.env` file or new secret is included
- [ ] User-controlled text that becomes HTML is escaped
- [ ] Screenshots are updated if the visible page changed
