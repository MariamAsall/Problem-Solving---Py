class singletone:
    _instance = None 
    @staticmethod
    def get_instance():
        if singletone._instance is None:
            singletone._instance = singletone()
        return singletone._instance
    def __init__(self):
        self.data = []
    def add_data(self, value):
        self.data.append(value)
    def get_data(self):
        return self.data

singletone1 = singletone.get_instance()
singletone2 = singletone.get_instance()
singletone1.add_data(10)
singletone2.add_data(20)
print(singletone1.get_data())
print(singletone2.get_data())
print(singletone1 is singletone2)



