import os

##non user function


def del_invalid_simv(user_string):
    user_string = user_string.replace("|", "").strip().split()
    return ";".join(user_string)


def deformator(user_string):
    return user_string.replace(";", " ")


def clear_povtor_spec_simvols(line):
    newlist = []
    for i in range(len(line)):
        if line[i] == ";" and newlist and newlist[-1] == ";":
            continue
        newlist.append(line[i])
    return "".join(newlist)


##user function


def add_new_file():

    name = input("Enter name: ")
    file_name = os.path.isfile(name + ".txt")

    if file_name:
        raise Exception("error: File alredy exists!")
    open(f"{name}.txt", "a").close
    print("done! File create successful!")


def open_file():

    name = input("Enter needed file: ")
    file_name = os.path.isfile(name + ".txt")

    if file_name:
        print("done! File opened successful!")
        return name
    else:
        raise Exception("error: File not created!")


def add_new_stash(current_file):
    while True:
        number = _get_stash_number()
        if number is not None:
            break
        print("Wrong number! Try again! ")

    while True:
        city = _get_stash_city()
        if city is not None:
            break
        print("Wrong city! Try again! ")

    while True:
        coords = _get_stash_coords()
        if coords is not None:
            break
        print("Wrong coords! Try again! ")
    x,y = coords

    while True:
        content_help_hint = _get_stash_contents()
        if content_help_hint is not None:
            break
        print("Wrong content! Try again! ")
    
    _save_stash(current_file, number, city, x, y, content_help_hint)


def _get_stash_number():
    number = input("Enter number: ").strip()
    try:
        number = int(number)
    except:
        return None
    return number


def _get_stash_city():
    city = input("Enter city: ")
    try:
        city = clear_povtor_spec_simvols(del_invalid_simv(city))
    except:
        return None
    return city


def _get_stash_coords():
    try:
        x, y = input('Enter coords("x y"): ').split()
        x = float(x)
        y = float(y)
    except:
        return None
    return x, y


def _get_stash_contents():
    content_help_hint = input("Enter contents and help_hint: ").strip()
    try:
        content_help_hint = clear_povtor_spec_simvols(
            del_invalid_simv(content_help_hint)
        )
    except:
        return None
    return content_help_hint


def _save_stash(current_file, number, city, x, y, content_help_hint):
    filename = f"{current_file}.txt"

    with open(filename, "a+", encoding="utf-8") as file:
        file.seek(0)

        for line in file:
            clear_line = line.strip()
            if not clear_line:
                continue
            data = clear_line.split()
            if data[0] == number:
                raise Exception("error: Wrong number!")

        file.seek(0, 2)
        file.write(f"{number} {city} {x} {y} ||| {content_help_hint}\n")


def search_by_city(current_file):
    search_city = input("Enter city: ")
    filename = f"{current_file}.txt"
    search_city = search_city.replace(" ", ";")
    with open(filename, "r") as file:
        file.seek(0)
        for line in file:
            clear_line = line.split()
            if clear_line[1] == search_city:
                print(deformator(line))


def del_stash(current_file):

    show_all_stashes(current_file)
    id_for_del = input("Enter del id:")
    filename = f"{current_file}.txt"

    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if id_for_del not in line:
                file.write(line)


def show_all_stashes(current_file):
    filename = f"{current_file}.txt"

    with open(filename, "r") as file:
        for line in file:
            print(deformator(line), end='')
        print()


def print_help():
    print("   ####Commands####")
    print("1            - create file")
    print("2            - open file")
    print("3            - add stash")
    print("4            - show all stashes")
    print("5            - search by City")
    print("6            - del stash")
    # print("7            - edit")
    print("0            - stop programm")
