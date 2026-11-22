import storage as st

def add_stash(stashes, number, city, x, y, hint, found):

    for block in stashes:
        if block["number"] == number:
            raise ValueError("there’s already one like this")     
    stashes.append({"number": number, "city": city, "x": x, "y": y, "hint": hint, "ound" : found})
    st.save_stashes(stashes)