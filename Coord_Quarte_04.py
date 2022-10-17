def is_that_number(mes):               # Позволяет ввести с коносоли целое число, возвращая
  print(mes)                           # пользователя ко вводу каждый раз, если ввод не корректен
  val = input('=>  ')
  try:
    return int(val)
  except ValueError:
    print('\033[1;31mЭто не число!\033[0m')
    return is_that_number(mes)

print('\n'*3)
print('\t\tЗадача 4')
print('*'*60)
print('  Напишите программу, которая по заданному номеру четверти,\nпоказывает диапазон возможных координат точек в этой чет-\nверти\n(x и y).') 
k = 0
while k < 1:
    coordinate_quarte = is_that_number('  \nВведите число, соответствующее координатной четверти,\nот 1 до 4:')
    if coordinate_quarte == 1:
        print('Для I четверти диапазон координат точек: x > 0 и y > 0')
        k += 1
    elif coordinate_quarte == 2: 
        print('Для II четверти диапазон координат точек: x < 0 и y > 0')
        k += 1
    elif coordinate_quarte == 3: 
        print('Для III четверти диапазон координат точек: x < 0 и y < 0')
        k += 1 
    elif coordinate_quarte == 4: 
        print('Для IV четверти диапазон координат точек: x > 0 и y < 0')
        k += 1           
    else: 
        print('\033[1;31mПожалуйста, будьте внимательнее! Вам нужно ввести число от 1 до 4.\033[0m')
print('*'*60)
print('\n'*3)