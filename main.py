from flask import Flask, render_template, request

import datetime

app = Flask(__name__)


@app.route("/")
def index():
    text = "Pozdrav !!!."
    year = datetime.datetime.now().year

    gradovi = ["Zagreb", "Split", "Rijeka"]

    return render_template("index.html", text=text, year=year, gradovi=gradovi)

@app.route("/o-nama")
def o_nama():
    return render_template("o-nama.html")


@app.route("/kontakt", methods=["POST"])
def kontakt():

    kontakt_ime = request.form.get("kontakt-ime")
    kontakt_adresa = request.form.get("kontakt-adresa")
    kontakt_email = request.form.get("kontakt-email")
    kontakt_poruka = request.form.get("kontakt-poruka")

    print(kontakt_ime)
    print(kontakt_adresa)
    print(kontakt_email)
    print(kontakt_poruka)

    return render_template("uspjeh.html", kontakt_ime = kontakt_ime, kontakt_adresa=kontakt_adresa, kontakt_email=kontakt_email, kontakt_poruka=kontakt_poruka  )


@app.route("/rent")
def rent():
    return render_template("rent.html")

@app.route("/naruci", methods=["POST"])
def naruci():
    ime = request.form.get("ime")
    telefon = request.form.get("telefon")
    cars = request.form.get("cars")

    return render_template("naruci.html", ime=ime, telefon=telefon, cars=cars)


if __name__ == '__main__':
    app.run()

