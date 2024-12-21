from typing import Any

def all_thing_is_obj(object: Any) -> str:
    obj_type = type(object)
    if obj_type in (list, tuple, set, dict):
        print(f"{obj_type})")
    elif obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")
    return 42
