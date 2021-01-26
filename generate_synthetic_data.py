# Глобальный импорт
import re
from random import randint
import uuid

# генерируем пять рандомных названий файлов с расширением logs
file_names = [str(uuid.uuid4()) + ".logs" for x in range(5)]


# функция генерирует строку
def generate_string():
    action_id_index = randint(0, 10)
    action_number = randint(90, 101)
    user_id_index = randint(0, 10)
    # uid пользователья(в реальной жизни - это юзер id который нужно отлавить)
    user_uid = '"' + str(uuid.uuid4()) + '"'

    original_str: str = """Oct 29 18:10:43 ds-db27-prod1 journal: Oracle Audit[13491]: LENGTH: "433" SESSIONID:[9] "203830992" ENTRYID:[1] "1" STATEMENT:[1] "1" USERID:[14] "ZABBIX_MONITOR" USERHOST:[31] "vm-pr-infra-zabbix01.tcsbank.ru" ACTION:[{}] "{}" RETURNCODE:[1] "0" COMMENT$TEXT:[138] "Authenticated by: DATABASE;AUTHENTICATED IDENTITY: ZABBIX_MONITOR; Client address: (ADDRESS=(PROTOCOL=tcp)(HOST=10.217.12.96)(PORT=42594))" OS$USERID:[{}] {} DBID:[10] "1033166545" PRIV$USED:[1] "5" CURRENT_USER:[14] "ZABBIX_MONITOR""".format(action_id_index, action_number, user_id_index, user_uid)
    return original_str


print("создаем синтеические данные")
for name_file in file_names:
    with open(name_file, "w") as f:
        for i in range(10000):
            f.writelines(generate_string() + "\n")
