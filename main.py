from flask import Flask, render_template, request
import requests
from urllib.parse import quote
from dataclasses import dataclass
import json

app = Flask(__name__, template_folder='templates')
port = 5000

full_api_url = "https://api.scryfall.com/cards"

@dataclass
class Card:
    name: str
    img: tuple[str,str,str]
    mana_cost: str
    txt: str
    rarity: str
    type: str


@app.route("/", methods=['GET'])
def index():
    search = request.args.get("search", '')
    page = request.args.get("page", '')

    encoded_search = quote(search)
    url = f"{full_api_url}/search?q={encoded_search}"

    response = requests.get(url)
    
    data = response.json()
    
    cards = []

    err_key = ""

    object = data["object"]

    if data["object"] == "error":
        err_key = data["details"]
    else:
        for card in data["data"]:

            if ("image_uris" and "oracle_text") in card.keys():

                image_pre = card["image_uris"]
                cards.append(
                    Card(
                        name = card["name"],
                        img = (
                            image_pre["small"], 
                            image_pre["normal"],
                            image_pre["large"]
                            ),
                        mana_cost = card["mana_cost"],
                        txt = card["oracle_text"],
                        rarity = card["rarity"].capitalize(),
                        type = card["type_line"]
                        )
                )

    return render_template('index.html', 
                           cards=cards,
                           err=err_key,
                           object=object
                           )

if __name__ == "__main__":
    app.run("0.0.0.0", port, debug=False)