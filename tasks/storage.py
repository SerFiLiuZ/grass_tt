import json
import os
from abc import ABC, abstractmethod
from typing import Any
from datetime import datetime
import time

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

    async def save(self, task: Any) -> str:
        if 'title' not in task:
            raise ValueError("Title is required")
        
        if task['title'] is None or task['title'].strip() == "":
            raise ValueError("The title cannot be empty")
        
        if not isinstance(task['title'], str):
            raise ValueError("Title must be a string")
        
        if not isinstance(task['completed'], bool):
            raise ValueError("Completed type error")

        with open(self._path) as file:
            data = json.load(file)

        new_task  = {
            'id': int(time.time()),
            'title': task['title'],
            'completed': task['completed'],
            'created_at': datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            'updated_at': datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        }

        data['tasks'].append(new_task)

        with open(self._path, 'w') as file:
            json.dump(data, file, indent=4) 

        return new_task
