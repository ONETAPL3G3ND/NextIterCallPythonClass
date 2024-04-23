class user:
    def __init__(self):
        self.stat = {"attack": 10, "hp": 100}
        self.iter = 0

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if self.iter == len(list(self.stat.values())):
            raise StopIteration
        item = list(self.stat.values())[self.iter]
        self.iter += 1
        return item


a = user()
for i in a:
    print(i)