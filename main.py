from handlers.LogHandler import LogHandler
from clients.CameraClient import CameraClient
from multiprocessing import Process


def main():
    logger.info("Starting...")

    clients = [CameraClient()]
    processes = [Process(target=c.run) for c in clients]

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()


if __name__ == "__main__":
    logger = LogHandler(log_file="logs/main.log")
    main()
