from flask import Flask, jsonify, render_template, request
from gpapp.function.function import getInfo
from gpapp.model import City
from gpapp.model.ParserKiller import Killer
from gpapp.variables import PARSER
from gpapp.config import KEY

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", key_API=KEY)

@app.route('/requestAjax', methods=["GET", "POST"])
def requestAjax():
    msg = request.args.get('msg')
    # print(msg)
    kil = Killer(msg)
    msg = str(kil.parser(PARSER))
    city = City(msg, KEY)
    cord = city.searchCity()
    if cord != "ERROR":
        id = city.getId(cord)
        extract = getInfo(id)
        lat = cord['lat']
        lng = cord['lng']
        return jsonify(result=extract, lat=lat, lng=lng)
    else:
        msg = "Désolé papy bot n'a pas compris! Essaye a nouveau!"
        return jsonify(result=msg, lat=48.856614, lng=2.3522219)


if __name__ == "__main__":
    app.run()
