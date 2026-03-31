from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        mood=request.form.get("mood")
        sleep=request.form.get("sleep")
        stress=request.form.get("stress")
        energy=request.form.get("energy")
        anxiety=request.form.get("anxiety")
        notes=request.form.get("notes")

        print(mood,sleep,stress,energy,anxiety,notes)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)