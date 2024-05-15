
from fastapi import APIRouter, Depends, status, HTTPException

from tasks.storage import Storage
from tasks.depends import get_storage
from tasks.service import TaskManager

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
async def create(task: dict, storage: Storage = Depends(get_storage)):
    """
    Route for create new task in storage and returned her name

    :param task: Task entity
    :return: task name
    """
    task_manager = TaskManager(storage)

    try:
        return await task_manager.create_task(task)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Service unavailable: " + str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred: " + str(e))
