from functions import handler


def main():

    command = input("Enter command: ").lower().strip()
    if command in handler:
        result = handler[command]
        if result:
            #Here should be real command,and not print.Print just for showing
            print(result)
        else:
            continue
    else:
        second_try = user_mistake(command)
        if second_try:
            result = handler[second_try]
            if result:
            #Here should be real command,and not print.Print just for showing
                print(result)
        else:
           print("Unknown command. Try another one")

