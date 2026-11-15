# Number Guessing Game

A simple number guessing game built with Python. This repository includes a browser-based version powered by Flask and an earlier terminal-based version.

## Browser Game

The computer randomly selects a number between 1 and 100. You have seven attempts to guess the correct number, with hints provided after each guess.

### How to Run Locally

1. Install Python 3.10 or later.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependency:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask application:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

Press `Control + C` in the terminal to stop the server.

## Terminal Version

Run the original command-line version using:

```bash
python3 numberGuessingGame.py
```

## Technologies Used

- Python
- Flask
- HTML
- CSS

## Project Structure

```text
number-guessing-game/
│
├── app.py
├── numberGuessingGame.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Project Files

- `app.py` — Flask routes and game logic.
- `templates/index.html` — Game interface.
- `static/style.css` — Styling and responsive design.
- `numberGuessingGame.py` — Terminal-based game.
- `requirements.txt` — Python dependency list.

The virtual environment and machine-specific files are excluded from Git. The Flask session key is generated at runtime unless `FLASK_SECRET_KEY` is set in the environment.