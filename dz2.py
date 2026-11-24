# функция считает стоимость билетов без скидки
def ticket_total(kolichestvo, cena=12):
    # умножаю количество на цену
    return kolichestvo * cena

# функция считает итоговую цену с учётом скидки для школьной группы
def final_price(kolichestvo, is_school_group=False):
    # сначала получаю стоимость без скидки через уже написанную функцию
    total = ticket_total(kolichestvo)
    # если это школьная группа то применяю скидку 25%
    if is_school_group:
        return total * 0.75
    # иначе возвращаю полную стоимость
    return total

# 3 обычных билета 
print(final_price(3))
# 4 билета для школьной группы 
print(final_price(4, is_school_group=True))
# 2 билета по изменённой цене 15 рублей 
print(ticket_total(2, cena=15))