from library_item import LibraryItem


catalog = {}
catalog["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
catalog["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
catalog["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
catalog["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
catalog["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)


def display_catalog():
    output = ""
    for key in catalog:
        item = catalog[key]
        output += f"{key} {item.info()}\n"
    return output


def retrieve_title(key):
    try:
        item = catalog[key]
        return item.name
    except KeyError:
        return None


def retrieve_director(key):
    try:
        item = catalog[key]
        return item.director
    except KeyError:
        return None


def retrieve_rating(key):
    try:
        item = catalog[key]
        return item.rating
    except KeyError:
        return -1


def update_rating(key, rating):
    try:
        item = catalog[key]
        item.rating = rating
    except KeyError:
        return


def retrieve_play_count(key):
    try:
        item = catalog[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = catalog[key]
        item.play_count += 1
    except KeyError:
        return