from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def calculate():
    bmi = ''
    height = ''
    weight = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = round(weight / (height * height) * 703, 1)

    return render_template("index.html", bmi=bmi, height=height, weight=weight)
