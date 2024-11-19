import pathlib


def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = list()
            for line in file.readlines():
                try:
                    salaries.append(float(line.split(',')[1]))
                except ValueError:
                    print("Salary isn't correct")
        salaries_sum = 0
        for value in salaries:
            salaries_sum += value
        if len(salaries) > 0 :
            total_and_average_tuple = (salaries_sum, salaries_sum / len(salaries))
            return total_and_average_tuple
        else:
            total_and_average_tuple = ()
    except Exception as e:
        return f"{e}."


# Приклад використання функції
total, average = total_salary('./Salary.txt')
print(f'Total salary: {total}, average salary: {average}')
