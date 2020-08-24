from flask import Flask, jsonify, render_template, request
import function.function as getInfo
from model.City import City
from model.ParserKiller import Killer
from variables import PARSER

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/requestAjax', methods=["GET", "POST"])
def requestAjax():
    msg = request.args.get('msg')
    kil = Killer(msg)
    msg = str(kil.parser(PARSER))
    city = City(msg)
    cord = city.searchCity()
    if cord != "ERROR":
        id = city.getId(cord)
        extract = getInfo(id)
        lat = cord['lat']
        lng = cord['lng']
        return jsonify(result=extract, lat=lat, lng=lng)
    else:
        msg = "sorry"
        return jsonify(result=msg, lat=48.856614, lng=2.3522219)


if __name__ == "__main__":
    app.run()
