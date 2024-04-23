#!/usr/bin/python3

from queue import Queue
from threading import Thread

from clients.CameraClient import CameraClient
from clients.NetClient import NetClient
from clients.AltimeterClient import AltimeterClient
from clients.GpsClient import GpsClient

from handlers.LogHandler import LogHandler


def main():
    logger = LogHandler(log_file="logs/main.log")

    captures = Queue()  # connect clients via queue

    clients = [
        CameraClient(captures),
        NetClient(captures),
        AltimeterClient(),
        GpsClient(),
    ]
    threads = [Thread(target=client.run) for client in clients]

    logger.info("Ready!")
    for thread in threads:
        thread.start()

    logger.info("Running...")

    for thread in threads:
        thread.join()

    logger.info("Finished")


if __name__ == "__main__":
    main()
