from tabulate import tabulate


def show_in_console(data: list, headers='firstrow'):
    print(tabulate(data, headers=headers,
                   tablefmt='fancy_grid', showindex='always'))
