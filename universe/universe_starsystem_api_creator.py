from api_app.connector import Connector
from api_app.connector import get_item_id

connector = Connector()

galaxy_id = get_item_id(connector.get_list("galaxies"),"galaxy")
starsystem_data = {
    "name": input("Input name of star system: "),
    "pos_x": input("Input x-coordinate of star system: "),
    "pos_y": input("Input y-coordinate of star system: "),
    "galaxy": galaxy_id
}

print(connector.create("starsystems", starsystem_data))

