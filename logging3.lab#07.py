class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance
    def __init__(self):
        self.log_history =[]
    def log_messages (self, message):
        self.log_history.append(message)
    def get_log_history(self):
        return self.log_history

log1 = Logger.get_instance()
log2 = Logger.get_instance()

log1.log_messages("message1")
log2.log_messages("messag2")

print(log1.get_log_history())
print(log2.get_log_history())

print(log1 is log2 )

