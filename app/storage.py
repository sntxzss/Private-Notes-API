USERS: dict[int, dict] = {}
NOTES: dict[int, dict] = {}
_counters: dict[str, int] = {"users": 0, "notes": 0}

def new_id(counter_name: str) -> int:
    _counters[counter_name] += 1
    return _counters[counter_name]