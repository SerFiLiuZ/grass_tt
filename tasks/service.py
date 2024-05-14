from storage import Storage


class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage

    async def get_tasks(self) -> dict:
        return await self.storage.read()

    async def create_task(self) -> str:
        ...
