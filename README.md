# Movie Reservation System with Data Structures and Algorithms

This project is a movie reservation system that incorporates various data structures and algorithms to handle functionality such as seat reservation, movie showtimes, and user management.

## Features

- **Movie Reservation**: Reserve seats for a movie at a selected theatre and showtime.
- **Movie Listings**: View available movies and their showtimes, sorted alphabetically.
- **User Management**: Register users and view their reservations.
- **Showtime Management**: Add, delete, and search for showtimes based on movie titles.
- **Seat Matrix Display**: Visualize available and reserved seats for a particular showtime.

## Data Structures and Algorithms Used

- **Merge Sort**: Used for sorting movie titles and showtimes.
- **Binary Search**: Used for searching movie titles.
- **Hashmap**: Storing showtimes, movies, theatres, users, and reservations.
- **Linked List**: Used for managing the reservation history of a user.

## Installation

1. Clone this repository to your home folder:

   ```bash
   git clone https://github.com/ihni/movie-system.git
   ```
2. Navigate to the project folder:

    ```bash
    cd movie-system
    ```
3. Install dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:

    ```bash
    python main.py
    ```

## Usage

### 1. Start the CLI:
- Run the following command to start the movie reservation system CLI:

    ```bash
    python main.py
    ```

### 2. Available Commands:
- **reserve <movie_title>**: Reserve a seat for a specific movie.
- **list_movies**: List all available movies sorted alphabetically.
- **view_reservations <email>**: View all reservations for a specific email address.
- **exit**: Exit the application.

 ### 3. Flow of Reservation:
 1. Reserve a seat:
 - 

 ## Contributing

 Contributions are welcome! If you have any suggestions or want to fix a bug, feel free to fork the repository and submit a pull request.
 1. Fork the repository.
 2. Create a new branch (git checkout -b feature-branch).
 3. Make your changes and commit them (git commit -am 'Add new feature').
 4. Push to the branch (git push origin feature-branch)
 5. Open a pull request.