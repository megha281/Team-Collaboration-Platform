class TeamCollaborationPlatform:
    def __init__(self):
        self.communications = {}  # To store communications, using communication_id as key
        self.efficiency_tracker = {}  # To store efficiency data, using efficiency_id as key

    # CRUD operations for communications
    def create_communication(self, communication_id, message):
        if communication_id in self.communications:
            print("Communication ID already exists.")
        else:
            self.communications[communication_id] = message
            print(f"Communication '{communication_id}' created.")

    def read_communication(self, communication_id):
        if communication_id in self.communications:
            print(f"Communication ID: {communication_id}, Message: {self.communications[communication_id]}")
        else:
            print("Communication ID not found.")

    def update_communication(self, communication_id, new_message):
        if communication_id in self.communications:
            self.communications[communication_id] = new_message
            print(f"Communication '{communication_id}' updated.")
        else:
            print("Communication ID not found.")

    def delete_communication(self, communication_id):
        if communication_id in self.communications:
            del self.communications[communication_id]
            print(f"Communication '{communication_id}' deleted.")
        else:
            print("Communication ID not found.")

    # CRUD operations for tracking efficiency
    def create_efficiency_record(self, efficiency_id, efficiency_score):
        if efficiency_id in self.efficiency_tracker:
            print("Efficiency ID already exists.")
        else:
            self.efficiency_tracker[efficiency_id] = efficiency_score
            print(f"Efficiency record '{efficiency_id}' created.")

    def read_efficiency_record(self, efficiency_id):
        if efficiency_id in self.efficiency_tracker:
            print(f"Efficiency ID: {efficiency_id}, Score: {self.efficiency_tracker[efficiency_id]}")
        else:
            print("Efficiency ID not found.")

    def update_efficiency_record(self, efficiency_id, new_score):
        if efficiency_id in self.efficiency_tracker:
            self.efficiency_tracker[efficiency_id] = new_score
            print(f"Efficiency record '{efficiency_id}' updated.")
        else:
            print("Efficiency ID not found.")

    def delete_efficiency_record(self, efficiency_id):
        if efficiency_id in self.efficiency_tracker:
            del self.efficiency_tracker[efficiency_id]
            print(f"Efficiency record '{efficiency_id}' deleted.")
        else:
            print("Efficiency ID not found.")

    # Menu-driven program
    def menu(self):
        while True:
            print("\n--- Team Collaboration Platform ---")
            print("1. Create Communication")
            print("2. Read Communication")
            print("3. Update Communication")
            print("4. Delete Communication")
            print("5. Create Efficiency Record")
            print("6. Read Efficiency Record")
            print("7. Update Efficiency Record")
            print("8. Delete Efficiency Record")
            print("9. Exit")
            choice = input("Enter your choice (1-9): ")

            if choice == '1':
                communication_id = input("Enter Communication ID: ")
                message = input("Enter Message: ")
                self.create_communication(communication_id, message)
            elif choice == '2':
                communication_id = input("Enter Communication ID: ")
                self.read_communication(communication_id)
            elif choice == '3':
                communication_id = input("Enter Communication ID: ")
                new_message = input("Enter New Message: ")
                self.update_communication(communication_id, new_message)
            elif choice == '4':
                communication_id = input("Enter Communication ID: ")
                self.delete_communication(communication_id)
            elif choice == '5':
                efficiency_id = input("Enter Efficiency ID: ")
                efficiency_score = input("Enter Efficiency Score: ")
                self.create_efficiency_record(efficiency_id, efficiency_score)
            elif choice == '6':
                efficiency_id = input("Enter Efficiency ID: ")
                self.read_efficiency_record(efficiency_id)
            elif choice == '7':
                efficiency_id = input("Enter Efficiency ID: ")
                new_score = input("Enter New Efficiency Score: ")
                self.update_efficiency_record(efficiency_id, new_score)
            elif choice == '8':
                efficiency_id = input("Enter Efficiency ID: ")
                self.delete_efficiency_record(efficiency_id)
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")


# Initialize and run the program
if __name__ == "__main__":
    platform = TeamCollaborationPlatform()
    platform.menu()
