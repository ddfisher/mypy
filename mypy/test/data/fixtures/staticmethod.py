import typing

class object:
    def __init__(self) -> None: pass

class type:
    def __init__(self, x) -> None: pass

class function: pass

staticmethod = object() # Dummy definition.

class bool: pass  # needed for automatic True, False, and __debug__ definitions
class int:
    @staticmethod
    def from_bytes(bytes: bytes, byteorder: str) -> int: pass

class str: pass
class bytes: pass
