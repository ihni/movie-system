# Movie Reservation System with Data Structures and Algorithms

This project is a movie reservation system to display data structures and algorithms for seat reservations, movie showtimes, and user management.

## Features

- **Movie Reservation**: Reserve seats for a movie at a selected theatre and showtime.
- **Movie Listings**: View available movies and their showtimes, sorted alphabetically.
- **User Management**: Register users and view their reservations.
- **Showtime Management**: Add, delete, and search for showtimes based on movie titles.
- **Seat Matrix Display**: Visualize available and reserved seats for a particular showtime.

## Data Structures and Algorithms Used
- **Matrix**: Used for displaying the seats in a row-column order.
- **Merge Sort**: Used for sorting movie titles and showtimes.
- **Binary Search**: Used for searching movie titles.
- **Hashmap**: Storing showtimes, movies, theatres, users, and reservations.
- **Linked List**: Used for managing the reservation history of a user.

## Requirements
- [Python](https://www.python.org/downloads/) (version 3.13.1 above)

## Installation

1. Clone this repository to your home folder:

   ```bash
   git clone https://github.com/ihni/movie-system.git
   ```
2. Navigate to the project folder:

    ```bash
    cd movie-system
    ```
3. Install dependencies:

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