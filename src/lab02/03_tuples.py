def format_record(rec_tuple):
    if type(rec_tuple)!=tuple:
        raise TypeError('На вход нужен кортеж')
    if len(rec_tuple)!=3:
        raise ValueError('В кортеже должно быть 3 элемента')
    fio_raw=rec_tuple[0]
    group_raw=rec_tuple[1]
    gpa_raw=rec_tuple[2]
    if type(fio_raw)!=str or type(group_raw)!=str:
        raise TypeError('Неверный тип данных строк')
    if type(gpa_raw)!=int and type(gpa_raw)!=float:
        raise TypeError('Неверный тип GPA')
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
    surname=fio_words[0].capitalize()
    initials=''
    if len(fio_words)>1:
        initials+=fio_words[1][0].upper()+'.'
    if len(fio_words)>2:
        initials+=fio_words[2][0].upper()+'.'
    fio_res=surname
    if initials!='':
        fio_res+=' '+initials
    group_res=''
    for char in group_raw:
        if char!=' ':
            group_res+=char
    if group_res=='':
        raise ValueError('Отсутствует группа')
    if gpa_raw<0.0 or gpa_raw>5.0:
        raise ValueError('Некорректный гпа')
    return f'{fio_res}, гр. {group_res}, GPA {gpa_raw:.2f}'

if __name__=='__main__':
    t1=("Иванов Иван Иванович", "БИВТ-25", 4.6)
    print(f"format_record: {format_record(t1)}")
    t2=("Петров Пётр", "ИКВО-12", 5.0)
    print(f"format_record: {format_record(t2)}")
    t3=("Петров Пётр Петрович", "ИКВО-12", 5.0)
    print(f"format_record: {format_record(t3)}")
    t4=("  сидорова   анна   сергеевна  ", "АВВ-01", 3.999)
    print(f"format_record: {format_record(t4)}")