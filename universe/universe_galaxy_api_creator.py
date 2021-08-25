from api_app.connector import Connector
from api_app.connector import get_item_id

connector = Connector()

galaxy_data = {
    "name": input("Input name of galaxy: "),
    "size_x": input("Input size x of galaxy: "),
    "size_y": input("Input size y of galaxy: ")
}

print(connector.create("galaxies", galaxy_data))

