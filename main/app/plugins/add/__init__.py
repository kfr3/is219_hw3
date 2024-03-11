from app.commands import Command
import logging

class AddCommand(Command):
    def execute(self):
        logging.info(a + b)
        return a + b