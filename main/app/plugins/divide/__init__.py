from app.commands import Command
import logging

class DivideCommand(Command):
    def execute(self):
        logging.info(a / b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b