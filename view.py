from flask import Flask, jsonify, render_template, request
from function.function import getInfo
from model.City import City
from model.ParserKiller import Killer
from variables import PARSER
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html", key_API=os.getenv("key"))

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
