def Menu(str):
    amarelo_negrito = "\033[1;33m"
    ciano_negrito = "\033[1;36m"
    fim = "\033[m"
    s = '-=' * 60
    # Printa um menu personalizado no terminal
    print(f'{amarelo_negrito}{s}{fim}')
    print(f'{amarelo_negrito}{"!!BEM - VINDO!!":^100}{fim}')
    print(f'{amarelo_negrito}{"À...":^100}{fim}')
    print(f'{ciano_negrito}{str:^100}{fim}')
    print(f'{amarelo_negrito}{s}{fim}')

    print(f'\n{amarelo_negrito}{"Agora resposta as perguntas a seguir..."}{fim}')
    print()
