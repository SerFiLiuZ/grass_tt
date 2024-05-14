import json
import os
from abc import ABC, abstractmethod
from typing import Any


class Storage(ABC):
    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def save(self, **kwargs):
        raise NotImplementedError


class JSONStorage(Storage):
    """
    JSONStorage является наследником класса Storage

    Methods:
        read: Чтение данных из JSON файла
        save: Сохранение данных в хранилище
    """
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    _path = os.path.join(curr_dir, 'data.json')

    async def read(self) -> dict:
        with open(self._path) as file:
            return json.load(file)

    def save(self, task: Any) -> str:
        return 'TaskName'
