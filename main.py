#!/usr/bin/python3
 
from handlers.LogHandler import LogHandler
from clients.CameraClient import CameraClient

from threading import Thread


def main():
    logger.info("Started")

    clients = [CameraClient(),]
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
