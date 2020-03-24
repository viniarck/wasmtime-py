from .ffi import *
from ctypes import *
from wasmtime import Engine

class Store:
    def __init__(self, engine = None):
        if engine is None:
            engine = Engine()
        elif not isinstance(engine, Engine):
            raise TypeError("expected an Engine")
        self.__ptr__ = cast(dll.wasm_store_new(engine.__ptr__), P_wasm_store_t)
        self.engine = engine

    def __del__(self):
        if hasattr(self, '__ptr__'):
            dll.wasm_store_delete(self.__ptr__)