# HangmanHaven

A dynamic Hangman game built with Flask, featuring 100+ word categories, scoring, hints, timers, and smooth SVG animations. Fully responsive with a scrollable UI, perfect for word-guessing fun! Deployable on Heroku or Render.

## Features
- **Extensive Word Bank**: Over 100 categories (e.g., Animals, Movies, Tech) for diverse gameplay.
- **Scoring System**: Earn points for correct guesses and bonus points for remaining attempts.
- **Hints**: Reveal a letter for 10 points to aid gameplay.
- **Timer**: 60-second countdown per game for added challenge.
- **Animations**: Smooth SVG-based hangman figure and wave background.
- **Responsive Design**: Works seamlessly on desktop and mobile.
- **Game History**: Tracks past games with scores and outcomes, with a clear history option.

## Project Structure
HangmanHaven/
├── main.py              # Flask app with game logic
├── static/
│   ├── style.css        # Styles with animations and responsive design
│   └── script.js        # Client-side logic for gameplay and animations
├── templates/
│   └── index.html       # Main game interface
├── requirements.txt     # Python dependencies
├── Procfile             # Deployment configuration for Heroku/Render
└── README.md            # Project documentation


## Setup Instructions
### Prerequisites
- Python 3.8+
- Git
- Heroku CLI (for Heroku deployment) or Render account

### Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HangmanHaven.git
   cd HangmanHaven
