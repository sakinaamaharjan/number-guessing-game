
import os
import random
import secrets
from flask import Flask, render_template, request, session, redirect

# Creating the Flask application
app = Flask(__name__)

# Secret key for managing user sessions
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)


# Homepage route
@app.route("/", methods=["GET", "POST"])
def home():

    # Generate a random number when a new game starts
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 7

    if "finished" not in session:
        session["finished"] = False

    message = ""

    # Check whether the user has submitted a guess
    if request.method == "POST" and not session["finished"]:
        guess = request.form.get("guess")

        try:
            guess = int(guess)

            if guess < 1 or guess > 100:
                message = "Please enter a number between 1 and 100."

            elif guess == session["number"]:
                message = "Congratulations! You have guessed the correct number!"
                session["finished"] = True

            elif guess < session["number"]:
                session["attempts"] -= 1
                message = "Too low! Try a higher number."

            else:
                session["attempts"] -= 1
                message = "Too high! Try a lower number."

            # Check whether the player has run out of attempts
            if session["attempts"] == 0 and not session["finished"]:
                message = f"Game Over! The correct number was {session['number']}."
                session["finished"] = True

        except ValueError:
            message = "Please enter a valid number."

    return render_template(
        "index.html",
        message=message,
        attempts=session["attempts"],
        finished=session["finished"]
    )


# Restart the game
@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")


# Start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
