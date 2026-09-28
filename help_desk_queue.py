# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return None
        
        dequeued_node = self.front
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        dequeued_node.next = None
        return dequeued_node.value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value
    
    def print_queue(self):
        current = self.front
        items = []
        while current is not None:
            items.append(str(current.value))
            current = current.next
        print(" -> ".join(items) if items else "Queue is empty.")
    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = queue.dequeue()
            if name is not None:
                print(f"Helping {name} now.")
            else:
                print("No customers in the queue.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            name = queue.peek()
            if name is not None:
                print(f"Next customer: {name}")
            else:
                print("No customers in the queue.")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

#A stack would be the right choice for undo/redo because it is following the order of the last in- first out. This order is the same as how undo/redo would function. Also the most recent edit is typically what you want to be reversed first and pushing from a single end reflects the most recent action. 
#A queue allows you to add people to the back of the line and ensure that you are helping whoever has been waiting for the longest time. This is similar to how a waitlist list works in the reality where the individual who arrived first is helped first. Enqueing and dequeing keeps fairness within the line and doesn't have to search through the different customers. If a stack were to have been used then it would be helping the latest person who has joined the line instead of having them wait and help others who had arrived much earlier. People who arrive first and early would be waiting forever since a stack works in the opposite order.
#My implementations are different from Python’s built-in lists as lists are like long shelves where everything is sitting next to each other. If you wanted to remove something that was at the front then you would be having to move everything down in order to fill in that gap. By doing all of this it creates more work and if the list is lengthy it would also involve more work too. My stack and queue are built from linked nodes where every operation only touches one or two pointers and runs in constant time. My implementations are also different from built in python lists because there it limits access to the front or top which is making it use the correct pattern and avoid mistakes. 


