import pathlib

doc_data_cats_path = pathlib.Path('./data_cats.txt')


def get_cats_info(path):
    try:
        with open(doc_data_cats_path, "r", encoding="utf-8") as file:
            cats = list()
            list_dict_cats_info = list()

            for line in file.readlines():
                cats.append(line.split(','))
            for cat in cats:
                try:
                    list_dict_cats_info.append({'id': cat[0], 'name': cat[1], 'age': int(cat[2])})
                except ValueError:
                    list_dict_cats_info.append({'id': cat[0], 'name': cat[1], 'age': None})
                    print('Invalid age!')
        return list_dict_cats_info
    except Exception as e:
        return f"{e}."


print(get_cats_info(doc_data_cats_path))
