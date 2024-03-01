from app.commands import Command

class DivideCommand(Command):
    def execute(self):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b