from api_app.connector import Connector
from api_app.connector import get_item_id

"""
    Galaxy
    StarSystem
    Star
    Planet
    Moon
"""

connector = Connector()
# galaxy_id = get_item_id(connector.get_list("galaxies"),"galaxy")
# # starsystem_id = get_item_id(connector.get_list("starsystems"),"starsystem")
# # star_id = get_item_id(connector.get_list("stars"),"star")
# # planet_id = get_item_id(connector.get_list("planets"),"planet")
# # moon_id = get_item_id(connector.get_list("moons"),"moon")

# # 1 universe = several galaxies, starsystems, stars, etc. :(
# starsystem_data = {
#     "name": input("Input name of starsystem:"),
#     "galaxy": galaxy_id,
#     # "starsystem": starsystem_id,
#     # "star": star_id,
#     # "planet": planet_id,
#     # "moon": moon_id,
# }

# print(connector.create("starsystem", starsystem_data))

# galaxy_data = {
#     "name": input("Input name of galaxy: "),
# }

# starsystem_id = get_item_id(connector.get_list("starsystems"),"starsystem")
# planet_data = {
#     "name": input("Input name of planet: "),
#     "starsystem": starsystem_id
# }

# star_data = {
#     "name": input("Input name of star: "),
#     "starsystem": starsystem_id
# }

planet_id = get_item_id(connector.get_list("planets"),"planet")
moon_data = {
    "name": input("Input name of moon: "),
    "color": input("Input color of moon: "),
    "diameter": input("Input diameter of moon: "),
    "area": input("Input area of moon: "),
    "planet": planet_id
}

print(connector.create("moons", moon_data))

