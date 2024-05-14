import datetime as dt

def now() -> dt.datetime:
    return dt.datetime.now()

def is_old(other: dt.datetime) -> bool:
    current = now()
    diff = current - other
    return (diff.days > 0) #diff.seconds >= 3600
