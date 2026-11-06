import functions as func


def main():
    br = True
    while br:
        func.print_help()
        unswer = input("Enter commands: ")

        if unswer == "1":
            func.add_new_file()

        elif unswer == "2":
            current_file = func.open_file()

        elif unswer == "3":
            func.add_new_stash(current_file)

        elif unswer == "4":
            func.show_all_stashes(current_file)

        elif unswer == "5":
            func.search_by_city(current_file)

        elif unswer == "0":
            break

        else:
            print("wrong command!")


if __name__ == "__main__":
    main()
    print("END!")
