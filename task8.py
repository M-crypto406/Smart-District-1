import logging
import time
from functools import wraps

logging.basicConfig(
    filename="api.log",
    level=logging.INFO
)

def middleware(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        try:
            logging.info("Function started")
            return func(*args, **kwargs)
        except Exception:
            logging.exception("Function failed")
            raise
        finally:
            print("Time taken:", round(time.time() - start, 4))

    return wrapper

def check_token(func):
    @wraps(func)
    def wrapper(token, *args, **kwargs):
        if token != "demo-token":
            raise PermissionError("Invalid token")
        return func(*args, **kwargs)
    return wrapper

@middleware
@check_token
def get_student(student_id):
    return {"id": student_id, "name": "Ali"}

try:
    print(get_student("demo-token", 101))
except PermissionError as error:
    print(error)