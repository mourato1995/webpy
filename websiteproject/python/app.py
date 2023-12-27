from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='templates')

# Define a function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, birthdate DATE)")
    conn.commit()
    conn.close()

# Root route to display the form
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    birthdate = request.form.get("birthdate")
    
    create_table()
    
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, birthdate) VALUES (?, ?)", (name, birthdate))
    conn.commit()
    conn.close()
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
