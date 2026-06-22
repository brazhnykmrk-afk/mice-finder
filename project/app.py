import json
import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

with open("mice.json", "r", encoding="utf-8") as f:
    mice = json.load(f)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        purpose = request.form["purpose"]
        budget = int(request.form["budget"])
        wireless = request.form["wireless"]
        hand_size = request.form["hand_size"]
        comfort = request.form["comfort"]

        best_mouse = None
        best_score = -1

        for mouse in mice:

            score = 0

            if purpose in mouse["recommended_for"]:
                score += 5

            if mouse["price_usd"] <= budget:
                score += 3

            if hand_size in mouse["hand_size"]:
                score += 2

            if wireless == "any":
                score += 1

            elif wireless == str(mouse["wireless"]).lower():
                score += 3

            if score > best_score:
                best_score = score
                best_mouse = mouse

        result = best_mouse

    return render_template(
        "index.html",
        result=result
    )



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
