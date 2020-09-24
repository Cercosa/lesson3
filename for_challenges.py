# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Olya', 'Petya', 'Vasia', 'Misha']
for name in names:
   print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Olya', 'Petya', 'Vasia', 'Misha']
for name in names:
    print(name, "-", len(name), "letters in name")


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Olya': False,
  'Petya': True,
  'Vasia': True,
  'Masha': False,
}
names = ['Olya', 'Petya', 'Vasia', 'Masha']
for name in names:
    if name in is_male:
        if is_male[name] == True:
            print(name, '-', 'gender: male')
        else:
            print(name, '-', 'gender: female')


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Vasya', 'Masha'],
  ['Olya', 'Petr', 'Grisha'],
]
print('How many groups are in list -', len(groups))
for group in groups:
    print('Number of group members -', len(group))



# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Vasya', 'Masha'],
  ['Olya', 'Petr', 'Grisha'],
]

groups_counter = 0
for group in groups:
    groups_counter += 1
    print('In group numer', groups_counter, 'number of members is -', len(group))
