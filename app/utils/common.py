from datetime import datetime

from sqlalchemy.orm import class_mapper


def object_to_dict(obj, found=None):
    if found is None:
        found = set()
    mapper = class_mapper(obj.__class__)
    columns = [column.key for column in mapper.columns]
    get_key_value = lambda c: (c, getattr(obj, c).isoformat()) if isinstance(getattr(obj, c), datetime) else (c, getattr(obj, c))
    out = dict(map(get_key_value, columns))
    for name, relation in mapper.relationships.items():
        if relation not in found:
            found.add(relation)
            related_obj = getattr(obj, name)
            if related_obj is not None:
                if relation.uselist:
                    out[name] = [object_to_dict(child, found) for child in related_obj]
                else:
                    out[name] = object_to_dict(related_obj, found)
    return out