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
    """Напиши комментарий"""
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    _path = os.path.join(curr_dir, 'data.json')

    async def read_data(self) -> dict:
        # TODO Метод не работает...
        with open(self._path) as file:
            return json.load(file)

    def save(self, task: Any) -> str:
        return 'TaskName'
