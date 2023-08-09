FILEPATH = "todos.txt"


def get_todo_list(filepath=FILEPATH):
    """ This function reads the text file and returns the list
    of the items in the stored list """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todo_list(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


""" if the file is run directly then main is this files name and 
if the file is imported then the name would be different """
if __name__ == "__main__":
    print("Hello")
    print(get_todo_list())
