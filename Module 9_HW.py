def input_error(func):
    def inner(*args,**kwargs):
        while True:
            try:
                return func(*args,**kwargs)
            except KeyError:
                print("Give me name and phone please")
            except ValueError:
                print("Give right phone please")
            except IndexError:
                print("Give wright too much information")
    return inner

@input_error
def main():
    notebook = {}
    while True:
        start = input()
        start_l = start.lower()
        if start == "hello":
            print("How can I help you?")
        elif "add" in start_l:
            name_number = start.split()
            name = name_number[1]
            number = int(name_number[2])
            notebook[name] = number
        elif "change" in start_l:
            name_number = start.split()
            name = name_number[1]
            number = int(name_number[2])
            notebook[name] = number
        elif "phone" in start_l:
            print(notebook[start[6:]])
        elif "show all" in start_l:
            print(notebook)

        elif "good bye" or "close" or "exit" in start:
            print("Good bye!")
            break

main()