import storage as st

def add_stash(stashes, number, city, x, y, hint, found):
    """append new stash"""
    for block in stashes:
        if block["number"] == number:
            raise ValueError("there’s already one like this")     
    stashes.append({"number": number, "city": city, "x": x, "y": y, "hint": hint, "found" : found})
    st.save_stashes(stashes)

def edit_stash(stashes, number, city, x, y, hint, found):
    """edit stash by number"""
    for block in stashes:
        if block["number"] == number:
            block["city"] = city
            block["x"] = x
            block["y"] = y
            block["hint"] = hint
            block["found"] = found
            st.save_stashes(stashes)
            return
    raise ValueError("Number not found!")

def del_stash(stashes, number):
    """delete stash by number"""
    new_stash = []
    for block in stashes:
        if block["number"] != number:
            new_stash.append(block)
    if len(stashes) == len(new_stash):
        raise ValueError("Number not found!")
    stashes[:] = new_stash
    st.save_stashes(stashes)

def search_by_city(stashes, city):
    """Search by city"""
    result = []
    for block in stashes:
        if block["city"] == city:
            result.append(block)
    return result        

if __name__ == "__main__":
    stashes = st.load_stashes()
    try:
        add_stash(stashes, 1, "Berezino", 1.0, 2.0, "under tree", False)
        add_stash(stashes, 2, "Berezino", 3.0, 4.0, "near wall", False)
        add_stash(stashes, 3, "Elektro", 5.0, 6.0, "in barn", False)
    except ValueError as error:
        print("error:", error)

    print(search_by_city(stashes, "Berezino"))   # два тайника
    print(search_by_city(stashes, "Nowhere"))    # []

    edit_stash(stashes, 3, "Elektro", 5.0, 6.0, "in barn", True)  # третий по порядку
    del_stash(stashes, 2)
    try:
        del_stash(stashes, 99)
    except ValueError as error:
        print("error:", error)
    print(stashes)