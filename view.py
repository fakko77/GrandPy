from flask import Flask, jsonify, render_template, request
from flask_googlemaps import GoogleMaps
from function.function import getInfo
from model.City import City
from model.ParserKiller import killer
from variables import PARSER

app = Flask(__name__)
# app.config.from_object('config')
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAr9x7A9TvznnGv43D0ZFB3e3c9IIIm3cQ"
GoogleMaps(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/requestAjax', methods=["GET", "POST"])
def requestAjax():
    msg = request.args.get('msg')
    kil = killer(msg)
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
