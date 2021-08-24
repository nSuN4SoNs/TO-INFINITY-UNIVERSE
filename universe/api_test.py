from api_app.connector import Connector

def beauty_console_view(data):
    return "\n".join([f"{i}:{data[i]['name']}" for i in range(len(data))])

def get_item_id(data, name_data):
    data_str = beauty_console_view(data)
    print(data_str)
    return data[int(input(f"Choose {name_data}:"))]["id"]

"""
    Galaxy
    StarSystem
    Star
    Planet
    Moon
"""

connector = Connector()
# company_id = get_item_id(connector.get_list("companies"),"company")
galaxy_id = get_item_id(connector.get_list("galaxies"),"galaxy")
starsystem_id = get_item_id(connector.get_list("starsystems"),"starsystem")
star_id = get_item_id(connector.get_list("stars"),"star")
planet_id = get_item_id(connector.get_list("planets"),"planet")
moon_id = get_item_id(connector.get_list("moons"),"moon")

# 1 universe = several galaxies, starsystems, stars, etc. :(
universe_data = {
    "name": input("Input name of universe:"),
    "galaxies": galaxy_id,
    "starsystems": starsystem_id,
    "stars": star_id,
    "planets": planet_id,
    "moons": moon_id
}

print(connector.create("galaxies", universe_data))


