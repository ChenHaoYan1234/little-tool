import multiprocessing
import typing
from multiprocessing import Queue


class Task(typing.TypedDict):
    task: typing.Callable
    args: typing.Tuple | None
    kwargs: typing.Dict[str, typing.Any] | None
    callback: typing.Callable[[typing.Any], None] | None


def worker(taskQueue: Queue):
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
            return


TaskQueue: Queue = Queue()

TaskWorkerProcess = multiprocessing.Process(
    target=worker, args=(TaskQueue,))
