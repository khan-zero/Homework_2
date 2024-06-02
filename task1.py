class CustomList:


    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)


        #EN(global): In this example, the DatabaseConnection class is created and the database is opened using the __enter__ method.
        #UZ(local): bu method "with" bilan class ochilganda ishga tushadi
    def __enter__(self):
        return self
        
        
        #EN(global): Using the with operator, the object is retrieved and processed in the database. Once done, the __exit__ method is automatically called and the database is closed.
        #UZ(local): bu methond with bilan ochilgan class oz ishini tugatsaisgtushadi 
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
              print("The list was cleared")
              self.items.clear()
            
        else:
            print("data was saved")

#EN(global): Getting objects from class
# UZ(local): yahshiyam 21-asrda yashaymiz otilmagan darsdan vazifa berildi. (davom ettirish shar emasdur) 
with CustomList() as my_list:
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

print(f"Mylist: {my_list.items}") #output: [10, 20, 30]
