import logging
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self):
        logging.info(a * b)
        return a * b