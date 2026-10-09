import logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG
)
logging.info("Program started")
logging.info("Taking input from user")
logging.warning("Low balance")
logging.error("Something went wrong")