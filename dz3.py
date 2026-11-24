# функция принимает любое количество баллов через *scores
def analyze_scores(*scores):
    # если баллов нет то возвращаю нули чтобы не было деления на ноль
    if len(scores) == 0:
        return 0, 0, 0
    # считаю сумму всех баллов
    summa = sum(scores)
    # количество результатов
    kolichestvo = len(scores)
    # средний балл
    srednee = summa / kolichestvo
    # возвращаю сразу три значения
    return summa, kolichestvo, srednee

# функция выводит название команды и все переданные характеристики
def print_report(nazvanie_komandy, **info):
    # сначала вывожу название команды
    print("Команда:", nazvanie_komandy)
    # потом все именованные параметры
    for kluch, znachenie in info.items():
        print(kluch + ":", znachenie)

# проверяю работу analyze_scores
# набор (8, 10, 7, 9)
print(analyze_scores(8, 10, 7, 9))
# набор (5, 5)
print(analyze_scores(5, 5))
# вызов без аргументов
print(analyze_scores())

# аызываю print_report с названием и двумя характеристиками
print_report("Комета", coach="Иванов", city="Москва")