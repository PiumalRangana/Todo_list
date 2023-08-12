import csv
class Todo_Task:
    _current_task_num = 0
    def __init__(self, Name:str, Discription :str, Status = "Incomplete") -> None:
        Todo_Task._current_task_num = self._genarate_next_task_num()
        self.Name = Name
        self.Discription = Discription
        self.Status = Status


    def __str__(self):
        return f'No: {self._current_task_num}., Name: {self.Name}.,  Discription: {self.Discription}., status: {self.Status}.'

    @property
    def get_task_num(self):
        return self._current_task_num

    @staticmethod
    # Get the task num from the last task saved in the 'todo.csv' file
    def _genarate_next_task_num():
        data = []  # Initialize the data list
        current_task_num = 1  # Default value

        try:
            with open("todo.csv","r") as file:
                reader = csv.DictReader(file)
                for raw in reader:
                    data.append(raw)
                
            if len(data) > 0:
                last_task = data[-1]
                last_task_num = last_task["Task_number"]
                last_task_num = int(last_task_num)
                current_task_num = last_task_num + 1

            else:
                current_task_num = 1

        except FileNotFoundError:
            print("File is missing.")


        except Exception as e:
            print(f'something went wrong . ERROR : {e}')

        return current_task_num

    # Add new tasks to todo.csv file
    def add_tsk():
        fieldnames = ['Task_number','Name','Discription','Status']
        Name = input("Enter the task Name:  ")
        Discription = input("Enter the task Discription:  ")
        task = Todo_Task(Name,Discription)
        # Make a dictionary of the object.
        d_task = {"Task_number" : task.get_task_num,
                "Name": task.Name,
                "Discription": task.Discription,
                "Status": task.Status }

        try:
            with open("todo.csv","a",newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(d_task)
                print("Task aded succesfuly")

        except FileNotFoundError as e:
            print(f"The file is missing.{e}")

        except Exception as e:
            print(f"some thing whent wrong.Could not save the task. ERROR : {e}")
   
   
    #Read the file "todo.csv" and print.
    def read_all_tsk():
        with open("todo.csv","r") as file:
            reader = csv.DictReader(file)
            for raw in reader:
                print(raw)
                print("-"*100)


    #Delet all tasks
    def delete_all_tsk():
        print("-"*100)
        print("This will delete all the tasks in the list and there is no way to recover.\nIf you still want to delet all tasks enter 'y'.\nIf you don't want to delet enter'n'.")
        confermation = input("enter 'n' or 'y':  ")
        print("-"*100)
        if confermation.lower() == "n":
            print("----Tasks are not deleted.----")
        
        elif confermation.lower() == "y":
            fieldnames = ['Task_number','Name','Discription','Status']
            try:
                with open("todo.csv","w") as file:
                    writer = csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()# ower write the file with only headers.
                    print("..<<..All tasks are succesfully deleted..>>..")
            except FileNotFoundError:
                print("File is not exist.")
            except Exception as e:
                print(f'Something went wront. ERROR : {e}')

        else:
            print("invalid input. please enter a valid input.")
    
    
    
    def mark_completed():
        #task_num = int(input("Enter the task number you completed: "))
        fieldnames = ['Task_number','Name','Discription','Status']
        data = []
        with open("todo.csv", "r") as file:
            reader = csv.DictReader(file)
            for raw in reader:
                data.append(raw)
        
        completed_task_num = input("Enter the task number that you have completed.:  ")
        if not len(data) > 0:  
            print("There is no data in the file.")  
        elif len(data)< int(completed_task_num):
            print(f"There are only {len(data)} tasks in the list.")
        
        else:    
            for raw in data:
                if raw["Task_number"] == completed_task_num:
                    print(raw)
                    raw["Status"] = "Completed  ."
                    
        with open("todo.csv", "w", newline='') as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for raw in data:
                writer.writerow(raw)

    # search for a input word in each task and print the task..
    def search_task():
        search_word = input("Enter what you want to search.")
        with open("todo.csv","r") as file:
            reader = csv.DictReader(file)
            for raw in reader:
                for key,val in raw.items():
                    if search_word in val:
                        print(raw)




#----------------------------------------------------------------------------------------------------------------------



def show_menu():
    print("------ Todo List ------")
    print("1. Add a task")
    print("2. Mark a task as completed")
    print("3. View all tasks")
    print("4. Delete all tasks")
    print("5. Search for a task")
    print("6. Exit")
    print("-----------------------")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            Todo_Task.add_tsk()
        elif choice == '2':
            Todo_Task.mark_completed()
        elif choice == '3':
            Todo_Task.read_all_tsk()
        elif choice == '4':
            Todo_Task.delete_all_tsk()
        elif choice == '5':
            Todo_Task.search_task()
        elif choice == '6':
            print("Exiting the Todo List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()