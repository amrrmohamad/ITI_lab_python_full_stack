class Todo:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class TodoApp:
    def __init__(self):
        self.todos = []

    def create(self, title, description):
        To_Do_List = Todo(title, description)
        self.todos.append(To_Do_List)
        print("Todo '{}' added successfully , description is '{}'".format(title, description))

    def read(self):
        if len(self.todos) == 0:
            print("Todo list is EMPTY")
        else:
            for i, todo in enumerate(self.todos):
                print(i, todo.description, todo.title)

    def update(self, index, title, description):
        if len(self.todos) == 0:
            print("Todo list is EMPTY")
        else:
            var1 = self.todos[index]
            var1.title = title
            var2 = self.todos[index]
            var2.description = description
            print("Todo '{}' updated successfully".format(title))

    def delete(self, index):
        if len(self.todos) == 0:
            print("Todo list is EMPTY")
        else:
            self.todos.pop(index)
            print("Todo '{}' deleted successfully".format(self.todos[index].title))


# example usage 
app = TodoApp()
app.create("Buy groceries", "Milk, Bread, Cheese")
app.create("Learn Python", "Complete OOP exercises")
print("="*30)
app.read()
app.update(1, "Learn Advanced Python", "Complete OOP and Data Structures")
print("="*30)
app.read()
app.delete(0)
print("="*30)
app.read()



##############################################################
# remember to uncomment this and comment the usage upper #
##############################################################

app=TodoApp()