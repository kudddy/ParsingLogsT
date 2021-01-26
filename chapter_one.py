import os
from itertools import islice
from parsers import get_user_id

file_name_result_chapter_one = "result_chapter_one.txt"
file_errors_one = "errors_one.txt"
n = 1000

# создаем массив с учетками, которые нужно найти
# ДОБАВИТЬ СЮДА ЧЕРЕЗ ЗАПЯТУЮ недостающие учетки
user_ids = ["ZABBIX_MONITOR"]

arr_line_logs_result:list = []
arr_errors_one:list = []
i = 0
for file in os.listdir():
    if "log" in file:
        with open(file) as f:
            while True:
                next_n_lines = list(islice(f, n))
                if not next_n_lines:
                    break
                else:
                    # тут процессим наши строки
                    for lines in next_n_lines:
                        i = i + 1
                        try:
                            user_id = get_user_id(lines)
                            # реализация бизнес логики
                            if user_id in user_ids and len(user_ids) > 0:
                                arr_line_logs_result.append(lines)
                                user_ids.remove(user_id)
                        except:
                            arr_errors_one.append(lines)
print("успешно оббработанных строк:{}".format(i))
print("неуспешных:{}".format(len(arr_errors_one)))

print("пишем результат")
with open(file_name_result_chapter_one, "w") as f:
    f.writelines(arr_line_logs_result)
print("пишем строки в которых были ошибки")
with open(file_errors_one, "w") as f:
    f.writelines(arr_errors_one)
