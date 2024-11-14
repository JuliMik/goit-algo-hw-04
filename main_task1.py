import pathlib

doc_salary_path = pathlib.Path('./Salary.txt')


def total_salary(path):
    try:
        with open(doc_salary_path, "r", encoding="utf-8") as file:
            salaries = list()
            for line in file.readlines():
                try:
                    salaries.append(int(line.split(',')[1]))
                except ValueError:
                    print("Salary isn't correct")
        salaries_sum = 0
        for value in salaries:
            salaries_sum += value
        total_and_average_tuple = (salaries_sum, round(salaries_sum / len(salaries)))
        return total_and_average_tuple
    except Exception as e:
        return f"{e}."


total, average = total_salary(doc_salary_path)
print(f'Total salary: {total}, average salary: {average}')
