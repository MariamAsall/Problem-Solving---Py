class singletone:
    instance = None
    @staticmethod
    def get_instance():
        if singletone.instance is None:
            singletone.instance = singletone()
        return singletone.instance
    def __init__(self):
        pass

singleton1 = singletone.get_instance()
singletone2 = singletone.get_instance()
print(singleton1 is singletone2)