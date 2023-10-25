import datetime as dt

def now() -> dt.datetime:
    return dt.datetime.now()

def is_old(string: str) -> bool:
    current = now()
    other = dt.datetime.fromisoformat(string)
    diff = current - other
    return (diff.seconds >= 3600 or diff.days > 0)
