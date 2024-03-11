import logging
from app.commands import Command

class SubtractCommand(Command):
    def execute(self):
        logging.info(a - b)
        return a - b