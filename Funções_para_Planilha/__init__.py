def mostrar_planilha(sheet, max_col, max_row):
    c = 0
    for co in range(1, max_col + 1):
        # printando as colunas da linha 1
        valor_coluna = sheet.cell(row=1, column=co)
        if valor_coluna.value is None or valor_coluna == '':
            pass
        else:
            print(f'\033[1;32m{valor_coluna.value}\033[m')
        for ro in range(1, max_row + 1):
            # printando as linhas da coluna
            valor_linha = sheet.cell(row=ro, column=1 + c)
            if valor_linha.value == valor_coluna.value or valor_linha.value is None or valor_linha.value == '':
                pass
            else:
                print(valor_linha.value)
        c += 1

    return


def remove_caracteres_indesejaveis(cellvalue):
    # função que remove caracteres indesejaveis de uma celula do excel
    import re
    text = re.sub(r"[\r\n\t\x07\x0b]", "", cellvalue)
    return text


def mostrar_pergunta_respostas(sheet, num_perg):
    import re
    for value in sheet['A']:
        if value.value == num_perg:
            # após achar a pergunta, é agr mostrado na tela.
            pergunta = sheet.cell(row=num_perg + 1, column=2)
            print(f'\033[1;33m{num_perg}º) {pergunta.value}\033[m')
            alternativas = sheet.cell(row=num_perg + 1, column=3)
            # retira os caracteres indesejáveis
            alternativas_alterada = remove_caracteres_indesejaveis(alternativas.value)
            # Formata as alternativas
            alternativas_lista = re.split('[/]', alternativas_alterada)
            for alt in alternativas_lista:
                print(f"\n      {alt.replace(':', ')')}")
            print('')

        else:
            pass
