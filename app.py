from flask import Flask, render_template, request, redirect
from database import init_db, add_message, get_messages

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        add_message(name, email, message)

        return redirect("/messages")

    return render_template("contact.html")


@app.route("/messages")
def messages():
    all_messages = get_messages()
    return render_template("messages.html", messages=all_messages)


if __name__ == "__main__":
    app.run(debug=True)