from prefect import flow,task,get_run_logger

@task
def task1():
    logger = get_run_logger()
    logger.info("Task1 is running")

@task
def task2():
    logger = get_run_logger()
    logger.info("Task2 is running")

@flow
def test_my_flow():
    task1()
    task2()

if __name__ == "__main__":
    test_my_flow()