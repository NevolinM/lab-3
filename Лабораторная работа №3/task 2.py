# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, sep = ","):
    participants_1 = set(group_1.split(sep))
    participants_2 = set(group_2.split(sep))
    result = list(participants_1.intersection(participants_2))
    return sorted(result)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sep="|"))
