from datetime import datetime


def get_timestamp_for_directory():
    return datetime.today().strftime("%Y-%m-%d %H-%M-%S")
