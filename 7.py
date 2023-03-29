inputingString = input()
searchSymbol = "f"
coordinate1 = inputingString.find(searchSymbol)
# ищем ближайшую f с начала списка и передаем её индекс перемнной coordinate1
coordinate2 = inputingString.rfind(searchSymbol)
# ищем ближайшую f с конца списка и передаем её индекс переменной coordinate2
print(*([coordinate1], [coordinate1,coordinate2])[coordinate2 != coordinate1])
# если две координаты совпадают, то выводим только одну из них