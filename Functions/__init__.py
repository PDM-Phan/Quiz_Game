def remove_caracteres_indesejaveis(cellvalue):
    # função que remove caracteres indesejaveis de uma celula do excel
    import re
    text = re.sub(r"[\r\n\t\x07\x0b]", "", cellvalue)
    return text


def mostrar_pergunta_respostas(sheet, limite_perg):
    import re
    for value in sheet['A']:
        if value.value == limite_perg:
            # após achar a pergunta, é agr mostrado na tela.
            pergunta = sheet.cell(row=limite_perg + 1, column=2)
            print(f'\033[1;33m{limite_perg}º) {pergunta.value}\033[m')
            alternativas = sheet.cell(row=limite_perg + 1, column=3)
            # retira os caracteres indesejáveis
            alternativas_alterada = remove_caracteres_indesejaveis(alternativas.value)
            # Formata as alternativas
            alternativas_lista = re.split('[/]', alternativas_alterada)
            for alt in alternativas_lista:
                print(f"\n   {alt.replace(':', ')')}")
            print('')

        else:
            pass


def verificar_resposta(sheet, num_perg, rep):
    # verifica a resposta do usuario com a resposta correta
    resposta_correta = sheet.cell(row=num_perg + 1, column=4)
    if 2 <= (num_perg + 1) <= 14:
        # Pergunta dificil
        p = 2
    elif 14 < (num_perg + 1) <= 25:
        # Pergunta facil
        p = 1

    return p if resposta_correta.value == rep else 0


def caucular_rank(resposta_certas, perguntas_respondidas):
    # Caucula o rank baseado nas perguntas respondidas com as perguntas acertadas
    rank = (resposta_certas * 100) / perguntas_respondidas
    return round(rank)
