# Game Web App

A fun and interactive web application featuring four different games, a dashboard to track usernames and high scores, and the ability for users to compete with each other to achieve the top scores!

---

## Features

- **Four Engaging Games**: Play and enjoy a variety of games to challenge your skills.
- **User Dashboard**:
  - Displays usernames and their highest scores.
  - Tracks progress and allows users to compete for the top spot.
- **Competitive Gameplay**: Users can play the games and beat each other’s high scores.

---

## Tech Stack

### Frontend
- **HTML**: For structuring the web pages.
- **CSS**: For styling and making the interface visually appealing.

### Backend
- **Flask Framework**: Used to handle the server-side logic and API requests.

### Database
- **PostgreSQL**: Stores user information, scores, and game-related data.

---

## Installation and Setup

Follow these steps to set up the project locally:

### Prerequisites
1. Python 3.10 or later
2. PostgreSQL installed on your system
3. Flask and required dependencies (see `requirements.txt`)


1. Clone the repository:
   ```bash
   git clone https://github.com/rujutamedhi/GameLab
   cd game-webapp
   ```



2. Set up the PostgreSQL database:
   - Create a database named `game_app`.
   - Update the database connection string in the Flask configuration file (`config.py`) with your PostgreSQL credentials.


3. Run the development server:
   ```bash
   flask run
   ```

7. Open the app in your browser at `http://127.0.0.1:5000`.

---

## How to Play

1. Register or log in with your username.
2. Choose one of the four games from the dashboard.
3. Play the game and try to achieve the highest score.
4. Check the dashboard to see your username and score.
5. Compete with other users to beat their scores!

---

