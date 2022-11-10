from functions import handler


def main():

    while True:

        command = input("Enter command: ").lower().strip()

        if command in handler:
            result = handler[command]()
            if result:
                print(result)
            else:
                continue
        else:
            print("Unknown command. Try another one")
