import os
from itertools import islice

from parsers import log_event, get_user_id, get_sension_id, get_os_user_id

file_name_result_chapter_two = "result_chapter_two.txt"
file_errors_two = "errors_two.txt"
user_ids = ["ZABBIX_MONITOR"]
n = 1000

arr_os_user_id_cond: list = []
arr_errors_two: list = []
j = 0
for file in os.listdir():
    if "log" in file:
        with open(file) as f:
            # читаем чанками файлы чтобы не использовать много оперативной памяти
            while True:
                next_n_lines = list(islice(f, n))
                if not next_n_lines:
                    break
                else:
                    # тут процессим наши строки
                    for lines in next_n_lines:

                        try:

                            if log_event(lines) == "100" and get_user_id(lines) in user_ids:
                                # тут бизнес смысл
                                arr_os_user_id_cond.append("файл:" + file + "|  "+"ид сессии:"+ get_sension_id(lines) +"|  "+"os_user_id:"+ get_os_user_id(lines) + "\n")
                                j = j + 1
                        except:
                            arr_errors_two.append(lines)
print("успешно оббработанных строк:{}".format(j))
print("неуспешных:{}".format(len(arr_errors_two)))
print("пишем результат и ошибки")
with open(file_name_result_chapter_two, "w") as f:
    f.writelines(arr_os_user_id_cond)

with open(file_errors_two, "w") as f:
    f.writelines(arr_errors_two)