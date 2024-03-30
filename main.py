#!/usr/bin/python3

from queue import Queue
from threading import Thread

from clients.CameraClient import CameraClient
from clients.NetClient import NetClient
from handlers.LogHandler import LogHandler


def main():
    logger.info("Started")

    captures = Queue()

    clients = [
        CameraClient(captures),
        NetClient(captures),
    ]
    threads = [Thread(target=client.run) for client in clients]

    for thread in threads:
        thread.start()

    logger.info("Running...")

    for thread in threads:
        thread.join()

    logger.info("Finished")


if __name__ == "__main__":
    logger = LogHandler(log_file="logs/main.log")
    main()
