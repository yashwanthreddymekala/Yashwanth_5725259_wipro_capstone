import logging


class LogGenerator:

    @staticmethod
    def loggen():

        logging.basicConfig(
            filename="logs/automation.log",
            format='%(asctime)s : %(levelname)s : %(message)s',
            datefmt='%d/%m/%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger()

        return logger