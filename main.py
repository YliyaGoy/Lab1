# в питоне нет указателя. В Python отсутствуют явные указатели, как в языках программирования C++ или C. Вместо этого,
# в Python используются ссылки на объекты.
class Rectangle: # Класс прямоугольник
    def __init__(self, height=1, width=1):#конструктор
        self.set_height(height)
        self.set_width(width)

    def set_height(self, height): #Функция для установления нового значения высоты
        if height > 0: #проверка на корректность значения
            self.height = height # установка нового значения
        else:
            print("Высота должна быть положительным числом.")

    def set_width(self, width):# Функция для установления нового значения ширины
        if width > 0: #проверка на корректность значения
            self.width = width # установка нового значения
        else: #если проверка не корректна вылетает уведомление
            print("Ширина должна быть положительным числом.")

    def get_area(self): # Функция вычисления площади  прямоугольника
        return self.height * self.width # Умножение ширины на длину

    def get_perimeter(self):# Функция вычисления периметра прямоугольника
        return 2 * (self.height + self.width) # Удвоенная сумма ширины и длины

    def print_info(self): # Функция вывода информации о классе прямоугольник
        print(f"Прямоугольник со сторонами {self.height} x {self.width}")
        print(f"Площадь: {self.get_area()}")
        print(f"Периметр: {self.get_perimeter()}")

class Matrix:
    def __init__(self, rows=1, cols=1):
        self.rows = rows  # Инициализация количества строк
        self.cols = cols  # Инициализация количества столбцов
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]  # Создание матрицы с нулевыми значениями

    def __del__(self):  # Деструктор
        self.data = None  # освобождение памяти путем установки data в None

    def get_element(self, i, j):  # Значение элемента
        return self.data[i][j]  # Возвращение значения элемента (i, j)

    def get_element_address(self, i, j):  # Адрес жлемента
        return id(self.data[i][j])  # Возвращение адреса элемента (i, j)

    def print_m_info(self):  # Печать матрицы
        for row in self.data:  # по строке
            print(" ".join(str(elem) for elem in row))

    def add(self, other):  # Сложение
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать")  # Проверка размеров для сложения
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]  # Сложение матриц
        return result

    def subtract(self, other):  # Вычитание
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать!")  # Проверка размеров для вычитания
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]  # Вычитание матриц
        return result

    def multiply(self, other):  # Умножение
        if self.cols != other.rows:
            raise ValueError("Проблема в размерах матриц!")  # Проверка размеров для умножения
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]  # Умножение матриц
        return result

    def multiply_by_scalar(self, scalar):  # Умножение на скаляр
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * scalar  # Умножение матрицы на число
        return result


class Vector:
    total_objects = 0  # статическая переменная для подсчета числа объектов типа Vector

    def __init__(self, size=1, initial_value=0.0):
        self.elements = [initial_value] * size  # инициализация вектора значениями по умолчанию
        self.size = size  # количество элементов вектора
        self.error_code = 0  # код ошибки
        Vector.total_objects += 1  # увеличение счетчика объектов

    def __del__(self):
        del self.elements  # освобождение памяти
        Vector.total_objects -= 1  # уменьшение счетчика объектов при удалении

    def set_element(self, index, value=0.0):
        self.elements[index] = value  # присваивание значения элементу массива
        self.error_code = 0  # сброс кода ошибки

    def get_element(self, index):
        try:
            return self.elements[index]  # получение значения элемента массива
        except IndexError:
            self.error_code = 2  # установка кода ошибки в случае выхода за пределы массива
            return None

    def print_vector(self):
        print(self.elements)  # вывод вектора

    def add_scalar(self, scalar):
        new_vector = Vector(self.size)  # создание нового объекта типа Vector
        new_vector.elements = [element + scalar for element in self.elements]  # сложение вектора с числом
        return new_vector

    def multiply_scalar(self, scalar):
        new_vector = Vector(self.size)  # создание нового объекта типа Vector
        new_vector.elements = [element * scalar for element in self.elements]  # умножение вектора на число
        return new_vector

    def subtract_scalar(self, scalar):
        new_vector = Vector(self.size)  # создание нового объекта типа Vector
        new_vector.elements = [element - scalar for element in self.elements]  # вычитание числа из вектора
        return new_vector

    def compare(self, other_vector):
        if self.size != other_vector.size:
            raise ValueError("Размеры векторов должны совпадать для сравнения")
        for i in range(self.size):
            if self.elements[i] > other_vector.elements[i]:
                return print("Первый вектор больше второго")  # текущий вектор больше
            elif self.elements[i] < other_vector.elements[i]:
                return print("Второй вектор больше первого")  # текущий вектор меньше
        return print("Векторы равны")  # векторы равны


def rec():
    print("\n_________________________________________")
    print("Проверка работы класса Прямоугольник:")
    rectangle1 = Rectangle(5.0, 3.0)  # Начальные значения прямоугольника, могут быть произвольные
    rectangle1.print_info()  # Вывод информации о прямоугольнике
    print("\nУстановка новых значений:")
    rectangle1.set_height(10.0)  # Установка новой высоты
    rectangle1.set_width(7.0)  # Установка новой ширины
    rectangle1.print_info()  # Вывод обновленной информации о прямоугольнике


def matrix():
    print("____________________________________")
    print("\nПроверка работы класса Матрица:")
    # Создание матриц
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]
    # Работа с классом
    result_sum = matrix1.add(matrix2)  # Сложение матриц
    result_subtract = matrix1.subtract(matrix2)  # Вычитание матриц
    result_multiply = matrix1.multiply(matrix2)  # Умножение матриц
    result_scalar = matrix1.multiply_by_scalar(2)  # Умножение матрицы на число

    # Проверка работы класса
    print("Матрица 1:")
    matrix1.print_m_info()
    print("\nМатрица 2:")
    matrix2.print_m_info()

    print("\nПроверка вывода значения элемента и адреса:")
    print("Значение:", matrix1.get_element(0, 0))
    print("Адрес:", matrix1.get_element_address(0, 0))

    print("\nВывод сложения матриц:")
    result_sum.print_m_info()
    print("Вывод вычитания матриц:")
    result_subtract.print_m_info()
    print("Вывод умножения матриц:")
    result_multiply.print_m_info()
    print("Вывод умножения матрицы на скаляр(число):")
    result_scalar.print_m_info()

    # Использование деструктора
    del matrix1
    # Проверка того, что матрица была успешно удалена, не находит ее после деструктора
    # print("\nЗначение:", matrix1.get_element(0,0))

def vec():
    print("_________________________________________")
    print("Проверка работы класса Вектор")
    # Создание вектора
    v1 = Vector(3, 0.0)
    v1.set_element(0, 1.0)
    v1.set_element(1, 2.0)
    v1.set_element(2, 3.0)
    print("Первый вектор:")
    v1.print_vector()

    # Проверка сложения с числом
    print("\nСложкние вектора с числом:")
    v2 = v1.add_scalar(5.0)
    v2.print_vector()
    print("\nУмножение вектора с числом:")
    v4 = v1.multiply_scalar(4.0)
    v4.print_vector()
    print("\nВычитание вектора с числом:")
    v5 = v1.subtract_scalar(2.0)
    v5.print_vector()

    # Сравнение векторов
    print("\nСравнение векторов:")
    v3 = Vector(3, 4.0)
    print("Вектор для сравнения 1:")
    v1.print_vector()
    print("Вектор для сравнения 2:")
    v3.print_vector()
    v1.compare(v3)

    # Подсчет числа объектов данного типа
    print("\nКоличество векторов")
    print(Vector.total_objects)


vec()
rec()
matrix()