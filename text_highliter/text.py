def print_big_message(text):
    big_letters = {
        'A': ['  AA  ', ' A  A ', 'AAAAAA', 'A    A', 'A    A'],
        'B': ['BBBBB ', 'B    B', 'BBBBB ', 'B    B', 'BBBBB '],
        'C': [' CCCC ', 'C    C', 'C     ', 'C    C', ' CCCC '],
        'D': ['DDDD  ', 'D   D ', 'D    D', 'D   D ', 'DDDD  '],
        'E': ['EEEEE ', 'E     ', 'EEEE  ', 'E     ', 'EEEEE '],
        'F': ['FFFFF ', 'F     ', 'FFFF  ', 'F     ', 'F     '],
        'G': [' GGGG ', 'G     ', 'G  GG ', 'G   G ', ' GGGG '],
        'H': ['H    H', 'H    H', 'HHHHHH', 'H    H', 'H    H'],
        'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
        'J': [' JJJJ ', '   J  ', '   J  ', 'J  J  ', ' JJ   '],
        'K': ['K   K ', 'K  K  ', 'KK    ', 'K  K  ', 'K   K '],
        'L': ['L     ', 'L     ', 'L     ', 'L     ', 'LLLLL '],
        'M': ['M    M', 'MM  MM', 'M MM M', 'M    M', 'M    M'],
        'N': ['N    N', 'NN   N', 'N N  N', 'N  N N', 'N   NN'],
        'O': [' OOO  ', 'O   O ', 'O   O ', 'O   O ', ' OOO  '],
        'P': ['PPPP  ', 'P   P ', 'PPPP  ', 'P     ', 'P     '],
        'Q': [' QQQ  ', 'Q   Q ', 'Q   Q ', 'Q  QQ ', ' QQQ Q'],
        'R': ['RRRR  ', 'R   R ', 'RRRR  ', 'R  R  ', 'R   R '],
        'S': [' SSSS ', 'S     ', ' SSS  ', '    S ', 'SSSS  '],
        'T': ['TTTTT ', '  T   ', '  T   ', '  T   ', '  T   '],
        'U': ['U   U ', 'U   U ', 'U   U ', 'U   U ', ' UUU  '],
        'V': ['V   V ', 'V   V ', ' V V  ', ' V V  ', '  V   '],
        'W': ['W   W ', 'W   W ', 'W W W ', 'WW WW ', 'W   W '],
        'X': ['X   X ', ' X X  ', '  X   ', ' X X  ', 'X   X '],
        'Y': ['Y   Y ', ' Y Y  ', '  Y   ', '  Y   ', 'Y   Y '],
        'Z': ['ZZZZZ ', '    Z ', '   Z  ', '  Z   ', 'ZZZZZ '],
        'A': ['  АА  ', ' А  А ', 'АААААА', 'А    А', 'А    А'],
        'Б': ['ББББ  ', 'Б    Б', 'ББББ  ', 'Б    Б', 'ББББ  '],
        'В': ['ВВВВ  ', 'В    В', 'ВВВВ  ', 'В    В', 'ВВВВ  '],
        'Г': ['ГГГГ  ', 'Г     ', 'Г     ', 'Г     ', 'Г     '],
        'Д': ['ДДД   ', 'Д  Д  ', 'Д   Д ', 'Д   Д ', 'ДДДД  '],
        'Е': ['ЕЕЕЕЕ ', 'Е     ', 'ЕЕЕЕ  ', 'Е     ', 'ЕЕЕЕЕ '],
        'Ё': ['ЕЕЕЕЕ ', 'Е     ', 'ЕЕЕЕ  ', 'Е     ', 'ЕЕЕЕЕ '],
        'Ж': ['Ж   Ж ', 'Ж   Ж ', 'ЖЖ ЖЖ ', 'Ж   Ж ', 'Ж   Ж '],
        'З': [' ЗЗЗ  ', 'З   З ', '   ЗЗ ', '  З   ', ' ЗЗЗ  '],
        'И': ['И   И ', 'ИИ  И ', 'И И И ', 'И  ИИ ', 'И   И '],
        'Й': ['И   И ', 'ИИ  И ', 'И И И ', 'И  ИИ ', 'И   И '],
        'К': ['К   К ', 'К  К  ', 'КК    ', 'К  К  ', 'К   К '],
        'Л': [' Л    ', ' Л    ', ' Л    ', ' Л    ', 'ЛЛЛЛ  '],
        'М': ['М   М ', 'ММ ММ ', 'М М М ', 'М   М ', 'М   М '],
        'Н': ['Н   Н ', 'Н   Н ', 'ННННН ', 'Н   Н ', 'Н   Н '],
        'О': [' ООО  ', 'О   О ', 'О   О ', 'О   О ', ' ООО  '],
        'П': ['ПППП  ', 'П   П ', 'П   П ', 'П   П ', 'П   П '],
        'Р': ['РРР   ', 'Р   Р ', 'РРР   ', 'Р     ', 'Р     '],
        'С': [' ССС  ', 'С   С ', 'С     ', 'С   С ', ' ССС  '],
        'Т': ['ТТТТТ ', '  Т   ', '  Т   ', '  Т   ', '  Т   '],
        'У': ['У   У ', 'У   У ', 'У   У ', 'У   У ', ' УУУ  '],
        'Ф': [' ФФФ  ', 'Ф Ф Ф ', 'Ф Ф Ф ', ' ФФФ  ', '  Ф   '],
        'Х': ['Х   Х ', ' Х Х  ', '  Х   ', ' Х Х  ', 'Х   Х '],
        'Ц': ['Ц     ', 'Ц     ', 'Ц     ', 'Ц     ', 'ЦЦЦЦЦ'],
        'Ч': ['ЧЧЧ   ', 'Ч   Ч ', 'Ч   Ч ', 'Ч   Ч ', 'ЧЧЧ   '],
        'Ш': ['Ш   Ш ', 'Ш   Ш ', 'Ш Ш Ш ', 'ШШ ШШ ', 'Ш   Ш '],
        'Щ': ['Щ   Щ ', 'Щ   Щ ', 'Щ Щ Щ ', 'ЩЩ ЩЩ ', 'Щ   Щ '],
        'Ъ': ['  Ъ   ', ' Ъ Ъ  ', 'Ъ   Ъ ', 'Ъ   Ъ ', ' ЪЪЪ '],
        'Ы': ['Ы    Ы', 'Ы    Ы', 'Ы   Ы ', 'Ы  Ы  ', 'ЫЫЫЫ '],
        'Ь': ['Ь     ', 'Ь     ', 'ЬЬЬ   ', 'Ь   Ь ', 'ЬЬЬ   '],
        'Э': [' ЭЭЭ  ', 'Э     ', 'ЭЭЭЭ  ', 'Э     ', ' ЭЭЭ  '],
        'Ю': ['Ю   Ю ', 'Ю   Ю ', 'Ю   Ю ', 'Ю   Ю ', ' ЮЮЮ  '],
        'Я': [' ЯЯЯЯ ', 'Я   Я ', 'Я Я Я ', 'ЯЯ  Я ', 'Я   Я '],
        ' ': ['      ', '      ', '      ', '      ', '      ']
    }

    for row in range(5):
        for char in text:
            print(big_letters.get(char.upper(), big_letters[' '])[row], end='  ')
        print()
while True:
    text = input("Введите текст: ")
    print_big_message(text)
