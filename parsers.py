import re


def get_user_id(lg_str: str):
    return re.findall('"([^"]*)"', lg_str.split("USERID")[1].split("USERHOST")[0])[0]


def get_os_user_id(lg_str: str):
    return re.findall('"([^"]*)"', lg_str.split("OS$USERID")[1].split("DBID")[0])[0]


def log_event(lg_str: str):
    return re.findall('"([^"]*)"', lg_str.split("ACTION")[1].split("RETURNCODE")[0])[0]


def get_sension_id(lg_str: str):
    return re.findall('"([^"]*)"', lg_str.split("SESSIONID")[1].split("ENTRYID")[0])[0]
