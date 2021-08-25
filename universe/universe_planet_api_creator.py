from api_app.connector import Connector
from api_app.connector import get_item_id

connector = Connector()

star_system_id = get_item_id(connector.get_list("starsystems"),"starsystem")
planet_data = {
    "name": input("Input name of planet: "),
    "color": input("Input color of planet: "),
    "diameter": input("Input diameter of planet: "),
    "area": input("Input area of planet: "),
    "star_system": star_system_id
}

print(connector.create("planets", planet_data))

