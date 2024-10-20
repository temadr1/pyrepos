def find_common_participants(one, two, razd=','):
    s1 = one.split(razd)
    s2 = two.split(razd)
    ans = []
    for i in s1:
        if i in s2:
            ans.append(i)
    return sorted(ans)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))