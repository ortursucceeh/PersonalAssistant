import sys
import os
folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(folder)
from constants import exit_words, hello_words
from functions import handler, exit_func, hello_func, user_mistake



def main():
    hello_func()
    while True:
        command = input(">>> Enter command: ").lower().strip()
        if command in handler:
            data = handler[command]
            func = data[0]
            args = data[1] if len(data) > 1 else ()
            info = data[2] if len(data) > 2 else ()
            answer = func(*(f(descr) for f, descr in zip(args, info)))
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
                data = handler[second_try]
                func = data[0]
                args = data[1] if len(data) > 1 else ()
                info = data[2] if len(data) > 2 else ()
                answer = func(*(f(descr) for f, descr in zip(args, info)))
                if answer:
                    print(answer)
            else:
                print(
                    "-!- Unknown command! -!-\nTo see all commands enter 'show_commands'")


if __name__ == '__main__':
    exit(main())
