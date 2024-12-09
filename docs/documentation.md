# Initializing the project

## Data structures and Algoritms to be used and reasoning why:
- Hashmaps for storing user information, user id for key and user data for the value, quick lookup
- Linked List for storing the history of a user's bookings
- Merge sort for sorting a movie by the title, year, &c..
- Matrix to represent the seat availability and seating plan of a theatre/showtime
- Set to store booked seatings to prevent duplication
- Queue to store the booking process
- Stack where users can undo their actions in a booking process such as cancel or go back
- Binary search for looking at a sorted movie array

## Models
- **Showtime** critical piece of the system so having constant time lookup, search, insertion, deletions, &c is important. We used hashmaps and sets for their O(1) time complexity to store information about the seating plans(booking a seat, checking if a seat is available, releasing a seat).
- **Theatre** generates a matrix as the most appropriate data structure for showcasing a seating plan that has rows and columns. This makes access to a seat easy by calling its respective row and column
- **Reservation** stores an instance of a movie, showtime, user, theatre, and a string for the seatname

## Services
- **Reservation Service** is a mediator between the reservations and showtimes. it uses a linked list to keep track of the users' reservation history where the tail node is the latest reservation. it also uses a hashmap for global reservations based on the reservation id for constant lookup