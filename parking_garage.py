import time

class ParkingGarage():
    """
       The ParkingGarage have three methods: takeTicket, payForParking
       and leaveGarage.

       Attributes for the class:
       -tickets: expected to be a list
       -parking_spaces: expected to be a list
       -current_tickets: expected to be a dictionary
    """

    def __init__(self, amount_parking_spaces):
        self.tickets = list(range(1, amount_parking_spaces + 1))
        self.parking_spaces = list(range(1, amount_parking_spaces + 1))
        self.current_tickets = {}
        self.current_ticket_timer = {}
    
    #Method to start a timer in seconds and stores it in a dictionary
    def startTimer(self, ticket_num):
        self.current_ticket_timer[ticket_num] = time.time()

    #Method to calculate time in minutes using started timer stored in a dictioanry 
    def calclateTime(self, ticket_num):
        elapsed_time = (time.time() - self.current_ticket_timer[ticket_num]) / 60
        return elapsed_time
    
    #Method to calculate cost by minutes return a float rounded to two decimals places
    def calculateCost(self, elapsed_time):
        cost = round(elapsed_time * 2.99, 2)
        return cost

    #Method to removes the first ticket number available in the list, if theres any available. 
    # Decrease the list of parking spaces available by one and stores that ticket number in the 
    # current_ticket dictionary. Otherwise, prints a message.
    def takeTicket(self):
        if self.tickets:
            ticket_num = self.tickets.pop(0)
            self.parking_spaces.pop(0)
            self.current_tickets[ticket_num] = {"paid" : False, "elapsed time" : 0, "cost" : 0.00}
            print(f"Your ticket number is: {ticket_num}")
            print("Do not forget to grab your ticket!")

            #Start timer
            self.startTimer(ticket_num)
            
        else:
            print("Sorry, the parking Garage is full!")

    #Method ask the user for a ticket number if it pass validation, then ask the 
    #user if the want to pay. If yes this method calls the calculateTime and calculateCost.
    def payForParking(self):
        while True:
            ticket_num = input("Please enter your ticket number or 'quit': ")
            
            if ticket_num.lower() == 'quit':
                break
            try:
                ticket_num = int(ticket_num)

                if ticket_num in self.current_tickets:
                    if self.current_tickets[ticket_num]["paid"] == True:
                            print("Ticket has already been paid.")
                            break 
                    else:
                        #Calculate time
                        elapsed_time = self.calclateTime(ticket_num)

                        #Calculate cost
                        cost = self.calculateCost(elapsed_time)
                        print(f"Your total today is: ${cost}")

                        pay_now = input("Do you wish to pay now? Yes/No: ")
                        if pay_now.lower() == "yes":
                            self.current_tickets[ticket_num]["paid"] = True
                            self.current_tickets[ticket_num]["elapsed time"] = elapsed_time
                            self.current_tickets[ticket_num]["cost"] = cost
                            del self.current_ticket_timer[ticket_num]
                            print("Ticket has been paid. You have 15 minutes to exit.")
                            break
                        elif pay_now.lower() == "no":
                            print("Payment not provided. Please pay to exit.")
                            break
                        else:
                            print("Invalid answer.")
                            break
                        
                else:
                    print("Invalid ticket number. Please enter a valid ticket number!")
            except:
                print("That didn't work. Please enter a number!")
        return ticket_num
        

    #Method to add a ticket to the list and a parkin space to the list once the user 
    #leaves the garage. Calls to the payForParking method to verify if ticket has been paid.
    def leaveGarage(self):
        ticket_num = self.payForParking()
        try:
            ticket_num = int(ticket_num)
                
            if self.current_tickets[ticket_num]["paid"] == True:
                self.parking_spaces.append(ticket_num)
                self.tickets.append(ticket_num)
                print("Thank you, have a nice day!")
        except:
            print("Back to Main Menu")
        

garage = ParkingGarage(3)

#Function to run the ParkingGarage methods on the garage instance
def run():
    while True:
        print("\nPlease select one of the following options:")
        print("1) Take a ticket")
        print("2) Pay for parking")
        print("3) Leave the garage")
        print("4) Quit")
        selection = input("Enter your selection: ")

        if selection == "1":
            garage.takeTicket()
        elif selection == "2":
            garage.payForParking()
        elif selection == "3":
            garage.leaveGarage()
        elif selection == "4":
            break
        else:
            print("Invalid answer. Please enter a number!")

run()






