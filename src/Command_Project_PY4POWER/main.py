from functions import handler, user_mistake, exit_func, hello_func, show_commands, exit_func
from constants import hello_words, exit_words


def main():
    while True:
        command = input("Enter command: ").lower().strip()
        if command in handler:
            answer = handler[command]()
            if answer:
                print(answer)
            else:
                continue
        elif command in hello_words:
            hello_func()
        elif command in exit_words:
            exit_func()
        else:
            second_try = user_mistake(command)
            if second_try:
                answer = handler[second_try]()
                if answer:
                    print(answer)
            else:
                print(
                    "-!- Unknown command! -!-\nTry another one!\nTo see all commands enter 'show_commands'")


if __name__ == '__main__':
    main()
