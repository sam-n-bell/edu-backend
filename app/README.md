# Setup virtual env (Windows 11 | Python 3.9)
0. pip install virtualenv
1. Create a venv: `python -m virtualenv .venv`
2. Activate venv: `.\.venv\Scripts\activate`
3. Deactivate venv: `deactivate`

# Custom Requirements
1. Make a `requirements.txt`
2. in an active venv, run `pip install -r requirements.txt`

# Running App Locally (outside Docker)
1. In terminal, run: `uvicorn app:app`

# To see README:
1. run app
2. `<localhost>:<port>/docs`