class db:

  def __init__(self):
    self.db = []

  def __call__(self, name):
    self.db.append(name)

if __name__ == "__main__":
  DB = db()
  DB("username")
  print(DB.db)
  
