def format_record(rec_str):
    s=rec_str[1:-1]
    parts=[]
    current=''
    in_quotes=False #Проверяет заход в кавычки
    quote_type=''
    for char in s:
        if char in '"\'':
            if not in_quotes:
                in_quotes=True #Отмечает что указатель в кавычках
                quote_type=char
            elif char==quote_type:
                in_quotes=False #Отмечает что вышел из кавычек
        elif char==',' and not in_quotes: #Отмечает, что элемент (фио/группа/гпа) кончился и добавляет в список
            parts.append(current)
            current=''
        else:
            current+=char
    parts.append(current)
    fio_raw=parts[0]
    group_raw=parts[1]
    gpa_raw=parts[2]
    fio_words=[]
    current_word=''
    for char in fio_raw:
        if char!=' ':
            current_word+=char
        else:
            if current_word!='':
                fio_words.append(current_word)
                current_word=''
    if current_word!='':
        fio_words.append(current_word)
    if len(fio_words)==0:
        raise ValueError('Отсутствуют инициалы') 
    surname=fio_words[0].capitalize() #Приводит фамилию в аккуратный вид записи
    initials=''
    if len(fio_words)>1:
        initials+=fio_words[1][0].upper()+'.'
    if len(fio_words)>2:
        initials+=fio_words[2][0].upper()+'.' #Добавляет количество букв-инициалов по количеству слов после фамилии
    fio_res=surname
    if initials!='':
        fio_res+=' '+initials
    group_res=''
    for char in group_raw:
        if char!=' ':
            group_res+=char
    if group_res=='':
        raise ValueError('Отсутствует группа')
    gpa_clean=''
    for char in gpa_raw:
        if char!=' ':
            gpa_clean+=char
    gpa=float(gpa_clean)
    if gpa<0.0 or gpa>5.0:
        raise ValueError('Некорректный гпа')
    return f'{fio_res}, гр. {group_res}, GPA {gpa:.2f}' #{gpa:.2f} донуляет gpa до 2 чисел после точки

a=input('Введите кортеж с ФИО, группой и gpa студента: ')
print(f'format_record: {format_record(a)}')