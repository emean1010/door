import datetime


def log(*args, **kwargs):
    time_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now()
    dt = now.strftime(time_format)
    with open('running.log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
        print(dt, *args, **kwargs)


def main_page():
    return 'message.index'
