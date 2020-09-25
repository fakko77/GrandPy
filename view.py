from flask import Flask, jsonify, render_template, request
from function.function import get_info
from model.City import City
from model.ParserKiller import Killer
from variables import PARSER
from config import KEY
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", key_API=KEY)


@app.route('/requestAjax')
def request_ajax():
    msg = request.args.get('msg')
    kil = Killer(msg)
    msg = str(kil.parser(PARSER))
    city = City(msg, KEY)
    cord = city.search_city()
    if cord != "ERROR":
        page_id = city.get_id(cord)
        extract = get_info(page_id)
        lat = cord['lat']
        lng = cord['lng']
        return jsonify(result=extract, lat=lat, lng=lng)
    else:
        msg = "Désolé papy bot n'a pas compris! Essaye a nouveau!"
        return jsonify(result=msg, lat=48.856614, lng=2.3522219)


if __name__ == "__main__":
    app.run()
