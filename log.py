import os 
import logging
import time


def setup_logging():
    logging.basicConfig(
        filename="command_history.txt",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        filemode="a"
    )
    logging.info("\n\n=== New Session ===\n")

def log_command_and_response(command, response):
    logging.info(f"Command: {command}")
    logging.info(f"Response: {response}")
