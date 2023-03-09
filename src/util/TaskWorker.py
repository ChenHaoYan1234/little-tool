import multiprocessing
import typing
from multiprocessing import Queue


class Task(typing.TypedDict):
    """类型检查用任务字典类\n
    规定task, args, kwargs, callback的类型"""
    task: typing.Callable
    args: typing.Tuple | None
    kwargs: typing.Dict[str, typing.Any] | None
    callback: typing.Callable[[typing.Any], None] | None


def worker(taskQueue: Queue):
    """任务执行器"""
    while True:
        tk: Task | None = taskQueue.get()
        if not tk is None:
            task = tk["task"]
            args = tk["args"]
            kwargs = tk["kwargs"]
            callback = tk["callback"]
            if callback is not None:
                if (not args is None) and (not kwargs is None):
                    callback(task(*args, **kwargs))
                elif args is None and (not kwargs is None):
                    callback(task(**kwargs))
                elif (not args is None) and kwargs is None:
                    callback(task(*args))
                else:
                    callback(task())
            else:
                if (not args is None) and (not kwargs is None):
                    task(*args, **kwargs)
                elif args is None and (not kwargs is None):
                    task(**kwargs)
                elif (not args is None) and kwargs is None:
                    task(*args)
                else:
                    task()
        else:
            taskQueue.close()
            return


TaskQueue: Queue = Queue()

TaskWorkerProcess = multiprocessing.Process(
    target=worker, args=(TaskQueue,))
