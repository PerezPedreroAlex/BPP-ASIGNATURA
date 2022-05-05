import csv
import pandas as pd


# **************************** LECTURA ************************************

datos = pd.read_csv('finanzas2020.csv', delimiter =';')

print(datos)

def _read_csv_file(file_name):
    data = {}
    months = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        row_count = 0
        for row in csv_reader:
            if row_count == 0:
                months = row
                data = {month: [] for month in row}
            else:
                for index, value in enumerate(row):
                    try:
                        data[months[index]].append(int(value))
                    except:
                        print(f"Valor {value} del mes {months[index]} no valido")

            row_count += 1
    return data

# ********************** FUNCIONES *************************************************

def _get_month_with_the_highest_expenditure(data):
    month_with_highest_expenditure = ""
    total_expenses = _get_total_expenses_by_month(data)
    lowest_value = total_expenses["Enero"]

    for month in total_expenses:
        if total_expenses[month] < lowest_value:
            lowest_value = total_expenses[month]
            month_with_highest_expenditure = month

    return month_with_highest_expenditure


def _get_month_with_the_lowest_expenditure(data):
    month_with_lowest_expenditure = ""
    total_expenses = _get_total_expenses_by_month(data)
    highest_value = total_expenses["Enero"]

    for month in total_expenses:
        if total_expenses[month] > highest_value:
            highest_value = total_expenses[month]
            month_with_lowest_expenditure = month

    return month_with_lowest_expenditure


def _get_annual_expenditure_mean(data):
    return sum(_get_total_expenses_by_month(data).values()) / 12


def _get_annual_total_expenses(data):
    return sum(_get_total_expenses_by_month(data).values())


def _get_annual_total_incomes(data):
    return sum(_get_total_incomes_by_month(data).values())


def _get_total_incomes_by_month(data):
    result = {}
    for month in data:
        result[month] = sum([value for value in data[month] if value > 0])

    return result


def _get_total_expenses_by_month(data):
    result = {}
    for month in data:
        result[month] = sum([value for value in data[month] if value < 0])

    return result


def _get_total_balance_by_month(data):
    result = {}
    for month in data:
        result[month] = sum([value for value in data[month]])

    return result


def _get_abs_list_values(data):
    return [abs(value) for value in data]

# ************************************ PRINTS ********************************************************    

def main():
    data = _read_csv_file("finanzas2020.csv")
    

    print("APARTADO 1")
    print(f"El mes con mayor gasto es {_get_month_with_the_highest_expenditure(data)}")
    print(f"El mes con menor gasto es {_get_month_with_the_lowest_expenditure(data)}")
    print(f"La media de gasto anual (solo gastos) es {abs(_get_annual_expenditure_mean(data))}")
    print(f"los gastos anuales han sido {abs(_get_annual_total_expenses(data))}")
    print(f"Los ingresos anuales han sido {_get_annual_total_incomes(data)}")
   

    print("APARTADO 2")
    print(f"El numero de columnas del fichero son {len(data.keys())}")
    print(f"Las columnas son: {data.keys()}")
    print(f"El contenido por mes es (solo incluye datos correctos): {data}")

    return 0    


if __name__ == "__main__":
    main()
     