data_dictionary = {
    "name": "Jose",
    "favorite_color": "Black",
    "favorite_planet": "Mars",
    "other_fun_fact": "I am a father of two children",
}

def group_by_planet(pythoners):
    """Group people from pythoners by their favorite planet."""
    grouped = {}
    for person in pythoners:
        name = person["name"]