
from fastapi import APIRouter, Depends, status, HTTPException

from storage import Storage
from depends import get_storage
from service import TaskManager

router = APIRouter(prefix='/tasks')


@router.get('/', status_code=status.HTTP_200_OK)
async def tasks(storage: Storage = Depends(get_storage)):
    """
    Route to view all tasks

    :param storage: actual storage instance
    """
    task_manager = TaskManager(storage)
    return await task_manager.get_tasks()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(task: dict):
    """
    Route for create new task in storage and returned her name

    :param task: Task entity
    :return: task name
    """
    ...
