from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from database import create_database, add_user, get_user
import re

app = Flask(__name__)

# Secret key for session management
app.secret_key = "change-this-secret-key"

# Secure session cookie settings
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False

# Create database
create_database()


@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))

    return """
    <h1>🔐 Cybersecurity Authentication Toolkit</h1>
    <a href="/register">Register</a><br>
    <a href="/login">Login</a>
    """


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        # Username validation
        if len(username) < 3:
            return "Username must contain at least 3 characters."

        # Password strength validation
        if len(password) < 8:
            return "Password must be at least 8 characters long."

        if not re.search(r"[A-Z]", password):
            return "Password must contain at least one uppercase letter."

        if not re.search(r"[a-z]", password):
            return "Password must contain at least one lowercase letter."

        if not re.search(r"\d", password):
            return "Password must contain at least one number."

        if not re.search(r"[!@#$%^&*]", password):
            return "Password must contain at least one special character."

        # Secure password hashing
        hashed_password = generate_password_hash(password)

        # Store user
        user_created = add_user(username, hashed_password)

        if not user_created:
            return "Username already exists. Please choose another username."

        return """
        <h2>Registration successful!</h2>
        <p>Your password was securely hashed and stored.</p>
        <a href="/login">Go to Login</a>
        """

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        # Find user
        user = get_user(username)

        if user is None:
            return "Invalid username or password."

        # Verify hashed password
        if check_password_hash(user[2], password):

            # Create authenticated session
            session["username"] = username

            return redirect(url_for("dashboard"))

        return "Invalid username or password."

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    # Protect dashboard from unauthenticated users
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


@app.route("/logout")
def logout():

    # Clear authenticated session
    session.clear()

    return """
    <h2>You have been logged out.</h2>
    <a href="/login">Login again</a>
    """


if __name__ == "__main__":
    app.run(debug=True)