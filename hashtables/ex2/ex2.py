#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Given a list of tickets, return a list of strings representing the sequence of flights.

    First, make hashtable with the sources as the keys, the destinations as the values.
    Find the first ticket by finding the key of "NONE"
    Set the current_destination to be the value of the first ticket.
    While the current_destination is not none,
        append it to the return string
        reassign current_destination to be its value (destination).
    """
    # Make dict
    flight_dict = dict()
    for flight in tickets:
        flight_dict[flight.source] = flight.destination

    print(flight_dict)

    route = []
    current_destination = flight_dict["NONE"]
    # print(current_destination)
    while current_destination != "NONE":
        route.append(current_destination)
        current_destination = flight_dict[current_destination]
    route.append("NONE")
    # print(route)
    return route


'''
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

# expected = ["PDX", "DCA", "NONE"]
print(reconstruct_trip(tickets, 3))
'''
