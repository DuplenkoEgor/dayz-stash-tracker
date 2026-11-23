import storage as st
import core

def format_stash(stash):
    """return stash as one line of text"""
    return (f"{stash['number']} | {stash['city']} | {stash['x']}, {stash['y']} "
            f"| {stash['hint']} | found: {stash['found']}")

def main():
    stashes = st.load_stashes()
    while True:
        print("1 - add, 2 - search, 3 - edit stash, 4 - delete stash, 5 - show, 0 - exit")
        choice = input("Command: ").strip()
        if choice == "1":
            try:
                number = int(input("Enter number: "))
                city = input("Enter city: ")
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
                hint = input("Enter hint: ")
                core.add_stash(stashes, number, city, x, y, hint, False)
                print("Added")
            except ValueError as error:
                print("error: ", error)

        elif choice == "2":
            city = input("Enter city: ")
            result = core.search_by_city(stashes, city)
            if not result:
                print("Nothing found")
            for stash in result:
                print(format_stash(stash))

        elif choice == "3":
            try:
                number = int(input("Enter number: "))
                city = input("Enter city: ")
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
                hint = input("Enter hint: ")
                found = input("Found? (y/n): ").strip().lower() == "y"
                core.edit_stash(stashes, number, city, x, y, hint, found)
                print("Edit done!")
            except ValueError as error:
                print("error: ", error)

        elif choice == "4":
            try:
                number = int(input("Enter number: "))
                core.del_stash(stashes, number)
                print("Deleted!")
            except ValueError as error:
                print("error: ", error)

        elif choice == "5":
            if not stashes:
                print("Nothing found")
            for stash in stashes:
                print(format_stash(stash))

        elif choice == "0":
            return

        else: print("wrong command!")

if __name__ == "__main__":
    main()
    print("All good!")