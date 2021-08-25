from api_app.connector import Connector
from api_app.connector import get_item_id

connector = Connector()

star_system_id = get_item_id(connector.get_list("starsystems"),"starsystem")
star_data = {
    "name": input("Input name of star: "),
    "color": input("Input color of star: "),
    "diameter": input("Input diameter of star: "),
    "area": input("Input area of star: "),
    "star_system": star_system_id
}

print(connector.create("stars", star_data))
