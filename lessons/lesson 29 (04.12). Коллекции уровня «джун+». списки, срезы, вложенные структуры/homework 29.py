games = ["шахматы", "шашки", "нарды"]
new_games = ["го", "бридж"]
games.extend(new_games)
print(f"Количество игр:{len(games)},\nПоследняя игра:{games[-1]},\n первая игра:{games[0]},\nвторая игра:{games[1]},")
for i, t in enumerate(games, start=1):
    print(f"{i}. {t}")


results = ["победа", "поражение", "ничья", "победа", "поражение", "ничья", "победа", "поражение"]
print(f"Начало турнира:{results[:3]},\nФинал турнира:{results[4:]},\nОсновные матчи:{results[:-3]},\nКлючевые матчи:{results[::3]}")


participants = ["Анна", "Петр", "Сергей", "Ольга"]
part2=["Иван" , "Мария"]
al="Алексей"
participants.extend(part2)
participants.insert(2,al)
participants.remove("Петр")
last=participants.pop()
participants.insert(0,last)
print(participants)



tournaments = [
    {"название": "Весенний кубок", "дата": "2020-04-15", "победитель": "Иван"},
    {"название": "Летний чемпионат", "дата": "2021-07-20", "победитель": "Анна"},
    {"название": "Осенний турнир", "дата": "2019-10-10", "победитель": "Сергей"},
    {"название": "Зимние игры", "дата": "2022-12-05", "победитель": "Анна"}
]
point=0
for tournament in tournaments:
    print(f"{tournament['название']}: {tournament['дата']} ({tournament['победитель']})")
for tournamen in tournaments:
    if tournamen['победитель']=="Иван":
        print(tournamen['название'])
        break
    else:
        continue
    if tournamen['победитель']=="Анна":
        point+=1
        continue
    else:
        continue
print(point)
