from flask  import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About Me")
@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")
@app.route("/skills")
def skills():
    return render_template("skills.html", title="Skills")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Add functionality to handle the message (e.g., save it or send an email)
        return render_template("contact.html", title="Contact", success=True)
    return render_template("contact.html", title="Contact")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

