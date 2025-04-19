let timerInterval = null;

function drawHangman(stage) {
    const parts = [
        'base', 'pole', 'top', 'rope', 'head', 
        'body', 'left-arm', 'right-arm', 'left-leg', 'right-leg'
    ];
    parts.forEach((part, index) => {
        const element = document.getElementById(`hangman-${part}`);
        if (element) {
            if (index < stage) {
                element.classList.add('visible');
            } else {
                element.classList.remove('visible');
            }
        }
    });
}

function setUsername() {
    const username = document.getElementById('usernameInput').value.trim();
    if (username) {
        fetch('/set_username', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: `username=${encodeURIComponent(username)}`
        })
        .then(response => response.json())
        .then(data => {
            showMessage(data.message, '#4caf50');
            location.reload();
        })
        .catch(error => showMessage('Error setting username', '#ef5350'));
    } else {
        showMessage('Please enter a username', '#ef5350');
    }
}

function startGame() {
    clearInterval(timerInterval);
    fetch('/start', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `category=${encodeURIComponent(document.getElementById('category').value)}&difficulty=${encodeURIComponent(document.getElementById('difficulty').value)}`
    })
    .then(response => response.json())
    .then(data => {
        updateGame(data);
        startTimer(data.timer);
        document.getElementById('wordDisplay').classList.add('reveal');
        setTimeout(() => document.getElementById('wordDisplay').classList.remove('reveal'), 500);
    })
    .catch(error => showMessage('Error starting game', '#ef5350'));
}

function startTimer(seconds) {
    document.getElementById('timer').textContent = `Time Left: ${seconds}s`;
    timerInterval = setInterval(() => {
        seconds--;
        document.getElementById('timer').textContent = `Time Left: ${seconds}s`;
        if (seconds <= 0) {
            clearInterval(timerInterval);
            endGame('Time’s up! You lost!');
        }
    }, 1000);
}

function makeGuess() {
    const guessInput = document.getElementById('guessInput');
    const guess = guessInput.value.trim().toLowerCase();
    
    // Client-side validation
    if (!guess.match(/^[a-z]$/)) {
        showMessage('Please enter a single letter (a-z)', '#ef5350');
        guessInput.value = '';
        return;
    }

    fetch('/guess', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `guess=${encodeURIComponent(guess)}`
    })
    .then(response => response.json())
    .then(data => {
        guessInput.value = '';
        updateGame(data);
        if (data.message.includes('Good')) {
            document.getElementById('wordDisplay').classList.add('reveal');
            setTimeout(() => document.getElementById('wordDisplay').classList.remove('reveal'), 500);
        }
        if (data.message.includes('won') || data.message.includes('lost')) {
            clearInterval(timerInterval);
        }
    })
    .catch(error => showMessage('Error making guess', '#ef5350'));
}

function getHint() {
    fetch('/hint', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: ''
    })
    .then(response => response.json())
    .then(data => {
        updateGame(data);
        if (data.message.includes('Hint')) {
            document.getElementById('wordDisplay').classList.add('reveal');
            setTimeout(() => document.getElementById('wordDisplay').classList.remove('reveal'), 500);
        }
    })
    .catch(error => showMessage('Error getting hint', '#ef5350'));
}

function clearHistory() {
    fetch('/clear_history', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: ''
    })
    .then(response => response.json())
    .then(data => {
        showMessage(data.message, '#4caf50');
        location.reload();
    })
    .catch(error => showMessage('Error clearing history', '#ef5350'));
}

function resetGame() {
    startGame(); // Simply restart the game
}

function endGame(message) {
    showMessage(message, '#ef5350');
    setTimeout(() => location.reload(), 1500);
}

function showMessage(text, color) {
    const messageEl = document.getElementById('message');
    messageEl.textContent = text;
    messageEl.style.color = color;
}

function updateGame(data) {
    document.getElementById('wordDisplay').textContent = data.word_display || document.getElementById('wordDisplay').textContent;
    document.getElementById('usedLetters').textContent = 'Used Letters: ' + (data.used_letters || '');
    document.getElementById('message').textContent = data.message;
    document.getElementById('score').textContent = `Score: ${data.score || 0}`;
    if (data.hangman_stage !== undefined) {
        drawHangman(data.hangman_stage);
    }

    const messageEl = document.getElementById('message');
    if (data.message.includes('Good') || data.message.includes('Hint')) {
        messageEl.style.color = '#4caf50';
    } else if (data.message.includes('Wrong') || data.message.includes('lost')) {
        messageEl.style.color = '#ef5350';
    } else if (data.message.includes('won')) {
        messageEl.style.color = '#0288d1';
    } else {
        messageEl.style.color = '#006064';
    }
}

// Event Listeners
document.getElementById('guessInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') makeGuess();
});

document.getElementById('category').style.animation = 'slideUp 0.5s ease-out';