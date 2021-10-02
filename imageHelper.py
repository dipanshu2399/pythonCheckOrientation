__all__ = [
    'set_dims',
    'get_type'
]

_DIMS = None

def set_dims(dims):
    global _DIMS
    _DIMS = list(map(lambda x: float(x),dims))

def get_type():
    global _DIMS
    rows, cols = _DIMS[0], _DIMS[1]
    if(rows>cols):
        return "portrait"
    elif(rows<cols):
        return "landscape"
    else:
        return "square"
