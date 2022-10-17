
def is_that_number(mes):               # Позволяет ввести с коносоли вещественное число, возвращая
  print(mes, end='')                   # пользователя ко вводу каждый раз, если ввод не корректен
  val = input()
  try:
    return float(val)
  except ValueError:
    print('\033[1;31mЭто не число!\033[0m')
    return is_that_number(mes)

print('\n'*3)
print('\t\tЗадача 5')
print('*'*60)
print('  Напишите программу, которая принимает на вход координаты\nдвух точек и находит расстояние между ними в 2D пространстве.') 
x1 = is_that_number('Введите координаты первой точки\nx1 = ')
y1 = is_that_number('y1 = ')
x2 = is_that_number('Введите координаты второй точки\nx2 = ')
y2 = is_that_number('y2 = ')
distance = print(f'Расстояние между точками с координатами {x1, y1} и {x2, y2}:\n{round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)}')
print('*'*60)
print('\n'*3)