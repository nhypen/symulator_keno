from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = ("symulator_keno")
  # potrzebne do zapisywania historii

@app.route("/", methods=["GET", "POST"])
def index():
    wynik = None
    trafienia = []
    twoje_liczby = []
    wylosowane = []

    if "historia" not in session:
        session["historia"] = []

    if request.method == "POST":
        liczby_input = request.form["liczby"]
        try:
            twoje_liczby = [int(x) for x in liczby_input.replace(",", " ").split()]
        except:
            wynik = "Błąd: wpisz liczby oddzielone spacją lub przecinkiem!"

        if len(twoje_liczby) == 5 and all(1 <= x <= 70 for x in twoje_liczby):
            wylosowane = sorted(random.sample(range(1, 71), 20))
            trafienia = sorted(set(wylosowane) & set(twoje_liczby))
            wynik = f"Trafienia: {len(trafienia)}"

            # zapisz w historii
            nowy_wpis = {
                "wylosowane": wylosowane,
                "twoje_liczby": twoje_liczby,
                "trafienia": trafienia,
                "ile": len(trafienia)
            }
            historia = session["historia"]
            historia.insert(0, nowy_wpis)
            session["historia"] = historia[:5]  # maks 5 ostatnich losowań

        else:
            wynik = "Podaj dokładnie 5 liczb od 1 do 70!"

    return render_template(
        "index.html",
        wynik=wynik,
        trafienia=trafienia,
        twoje_liczby=twoje_liczby,
        wylosowane=wylosowane,
        historia=session.get("historia", [])
    )

if __name__ == "__main__":
    app.run(debug=True)
