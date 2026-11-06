import os


def del_invalid_simv(user_string):
    user_string = user_string.replace("|","").strip().split()
    return " ".join(user_string)

 
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

    number = input("Enter number: ").strip()
    try:
        number = int(number)
    except:
        print("Wrong number!")
        return
    
    city = input("Enter city: ")
    try:
        city = del_invalid_simv(city)
    except:
        print("Wrong city name!")
        return
    
    x, y = input('Enter coords("x y"): ').split()
    try:
        x = int(x)
        y = int(y)
    except:
        print("Wrong coords!")
        return

    content_help_hint = input("Enter contents and help_hint: ").strip()
    try:
        content_help_hint = del_invalid_simv(content_help_hint)
    except:
        print("Wrong input!")
        return
    
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

    with open(filename, "r") as file:
        file.seek(0)

        for line in file:
            clear_line = line.split()
            if clear_line[1] == search_city:
                print(line)
                return
        print("not found!")


def show_all_stashes(current_file):
    filename = f"{current_file}.txt"

    with open(filename, "r") as file:
        for line in file:
            print(line)


def print_help():
    print("   ####Commands####")
    print("1            - create file")
    print("2            - open file")
    print("3            - add stash")
    print("4            - show all stashes")
    print("5            - search City")
    print("0            - stop programm")
