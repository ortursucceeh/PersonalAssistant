from tabulate import tabulate


def show_in_console(data: list, headers='firstrow', format='fancy_grid'):
    print(tabulate(data, headers=headers,
                   tablefmt=format, showindex='always'))
