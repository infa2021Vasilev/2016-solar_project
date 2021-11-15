#coding: utf-8

from solar_objects import Star, Planet
from solar_vis import DrawableObject

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            params = line.split()
            object_type = params[0].lower()
            if object_type == "star":
                star = Star(params[1],params[2],params[3],params[4],params[5],params[6],params[7])
                objects.append(star)
            elif object_type == "planet":
                planet = Planet(params[1],params[2],params[3],params[4],params[5],params[6],params[7])
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]

def write_space_objects_data_to_file(space_objects, output_filename):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    output_filename
    with open(output_filename) as file:
        inp = open(output_filename, 'r')
        board = inp.read()
        out = open(output_filename, 'w')  #R,color,m,x,y,Vx,Vy
        line = ''
        for obj in space_objects:
            if isinstance(obj, Star):
                name = 'Star'
            else:
                name = 'Planet'
            line += name + ' ' + str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.m) + ' ' + str(obj.x) + ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy) + '\n'
        board = line + '\n' + board
        out.write(board)


if __name__ == "__main__":
    print("This module is not for direct call!")
