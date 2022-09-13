# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
#
# Есть список, состоящий из чисел и слов.
#
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
#
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное,
# то записать во вторую таблицу слово: «нечётное»
#
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. Если меньше,
# то обновить 1 запись в первой таблице на «hello»

import sqlite3

conn = sqlite3.connect('test_hw.db')
cur = conn.cursor()

cur.execute('''drop table tab_1''')
cur.execute('''drop table tab_2''')
conn.commit()
cur.execute('''create table if not exists tab_1(id integer primary key autoincrement, col_1 text)''')
conn.commit()
cur.execute('''create table if not exists tab_2(id integer primary key autoincrement, col_1 text)''')
conn.commit()



arr = ['hi world', 55, 'world', 206, 'string', 'NY', 148]
for i in arr:
    if type(i) == str:
        cur.execute('''insert into tab_1(col_1)  values(?)''', (i,))
        conn.commit()
        cur.execute('''insert into tab_2(col_1) values(?)''', (len(i),))
        conn.commit()
    elif type(i) == int:
        if i % 2 == 0:
            cur.execute('''insert into tab_2(col_1) values(?)''', (i,))
            conn.commit()
        else:
            cur.execute('''insert into tab_2(col_1) values('нечётное')''')
            conn.commit()
    else:
        continue

cur.execute('''select count(*) from tab_2''')
conn.commit()
count = cur.fetchone()
for i in count:
    if i > 5:
        cur.execute('''delete from tab_1 where id=1''')
        conn.commit()
    else:
        cur.execute('''update tab_1 set col_1 = 'hello' where id = 1''')
        conn.commit()

print(count)