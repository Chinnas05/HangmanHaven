from flask import Flask, render_template, request, jsonify, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

class HangmanGame:
    def __init__(self):
        self.words = {
            "Animals": ["elephant", "giraffe", "kangaroo", "alligator", "zebra"],
            "Fruits": ["banana", "orange", "grapes", "mango", "pineapple"],
            "Countries": ["india", "germany", "brazil", "australia", "canada"],
            "Sports": ["basketball", "football", "tennis", "swimming", "volleyball"],
            "Colors": ["red", "blue", "green", "yellow", "purple"],
            "Vehicles": ["car", "truck", "motorcycle", "bicycle", "airplane"],
            "Professions": ["doctor", "teacher", "engineer", "artist", "chef"],
            "Clothing": ["shirt", "pants", "dress", "jacket", "shoes"],
            "Food": ["pizza", "hamburger", "sushi", "pasta", "salad"],
            "Drinks": ["water", "coffee", "tea", "juice", "soda"],
            "Instruments": ["guitar", "piano", "drums", "violin", "flute"],
            "Planets": ["earth", "mars", "jupiter", "saturn", "venus"],
            "Birds": ["eagle", "parrot", "penguin", "owl", "sparrow"],
            "Fish": ["salmon", "tuna", "clownfish", "shark", "goldfish"],
            "Vegetables": ["carrot", "broccoli", "potato", "tomato", "cucumber"],
            "Desserts": ["cake", "icecream", "cookie", "pie", "pudding"],
            "Cities": ["london", "paris", "tokyo", "newyork", "sydney"],
            "Movies": ["titanic", "inception", "avatar", "jaws", "matrix"],
            "Books": ["harrypotter", "lordoftherings", "hungergames", "twilight", "narnia"],
            "Flowers": ["rose", "tulip", "daisy", "sunflower", "lily"],
            "Trees": ["oak", "pine", "maple", "birch", "willow"],
            "Insects": ["butterfly", "bee", "ant", "grasshopper", "beetle"],
            "Reptiles": ["snake", "lizard", "turtle", "crocodile", "gecko"],
            "Mammals": ["lion", "tiger", "bear", "wolf", "deer"],
            "Tools": ["hammer", "screwdriver", "wrench", "drill", "saw"],
            "Furniture": ["chair", "table", "bed", "sofa", "desk"],
            "Weather": ["rain", "snow", "sun", "cloud", "storm"],
            "Emotions": ["happy", "sad", "angry", "scared", "excited"],
            "Shapes": ["circle", "square", "triangle", "rectangle", "oval"],
            "Numbers": ["one", "two", "three", "four", "five"],
            "Months": ["january", "february", "march", "april", "may"],
            "Days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
            "Seasons": ["spring", "summer", "autumn", "winter", "monsoon"],
            "Elements": ["fire", "water", "earth", "air", "metal"],
            "Metals": ["gold", "silver", "copper", "iron", "aluminum"],
            "Gems": ["diamond", "ruby", "emerald", "sapphire", "opal"],
            "Languages": ["english", "spanish", "french", "german", "chinese"],
            "Hobbies": ["reading", "painting", "gaming", "cooking", "dancing"],
            "School": ["math", "science", "history", "english", "art"],
            "Body": ["head", "arm", "leg", "hand", "foot"],
            "Organs": ["heart", "brain", "lungs", "liver", "kidney"],
            "Toys": ["doll", "car", "ball", "puzzle", "kite"],
            "Games": ["chess", "poker", "monopoly", "scrabble", "sudoku"],
            "Tech": ["computer", "phone", "tablet", "laptop", "camera"],
            "Software": ["word", "excel", "photoshop", "chrome", "python"],
            "Companies": ["apple", "google", "microsoft", "amazon", "tesla"],
            "Brands": ["nike", "adidas", "gucci", "prada", "levis"],
            "Music": ["rock", "pop", "jazz", "classical", "hiphop"],
            "Dance": ["ballet", "salsa", "tango", "hiphop", "tap"],
            "Art": ["painting", "sculpture", "drawing", "photography", "pottery"],
            "Space": ["star", "planet", "galaxy", "moon", "comet"],
            "Ocean": ["wave", "coral", "fish", "shark", "whale"],
            "Beach": ["sand", "shell", "wave", "towel", "umbrella"],
            "Forest": ["tree", "bear", "deer", "bird", "fox"],
            "Mountain": ["peak", "ridge", "valley", "cliff", "slope"],
            "River": ["stream", "bank", "bridge", "fish", "boat"],
            "Farm": ["cow", "pig", "chicken", "tractor", "barn"],
            "Zoo": ["lion", "elephant", "monkey", "giraffe", "tiger"],
            "Circus": ["clown", "acrobat", "lion", "ring", "tent"],
            "Magic": ["wand", "hat", "rabbit", "card", "trick"],
            "Science": ["physics", "chemistry", "biology", "astronomy", "geology"],
            "Math": ["addition", "subtraction", "multiplication", "division", "fraction"],
            "History": ["war", "king", "queen", "battle", "treaty"],
            "Myth": ["dragon", "unicorn", "phoenix", "mermaid", "giant"],
            "Fantasy": ["wizard", "elf", "dwarf", "orc", "goblin"],
            "Horror": ["ghost", "vampire", "zombie", "werewolf", "monster"],
            "Jobs": ["pilot", "nurse", "farmer", "writer", "actor"],
            "Places": ["park", "mall", "beach", "museum", "library"],
            "Buildings": ["house", "school", "hospital", "church", "tower"],
            "Rooms": ["kitchen", "bedroom", "bathroom", "livingroom", "garage"],
            "Kitchen": ["fork", "spoon", "knife", "plate", "cup"],
            "Bathroom": ["sink", "toilet", "shower", "mirror", "towel"],
            "Bedroom": ["bed", "pillow", "blanket", "lamp", "closet"],
            "Garden": ["flower", "tree", "grass", "fence", "bench"],
            "Party": ["cake", "balloon", "gift", "music", "dance"],
            "Holiday": ["christmas", "halloween", "easter", "thanksgiving", "newyear"],
            "Religion": ["god", "prayer", "church", "temple", "mosque"],
            "Time": ["clock", "watch", "hour", "minute", "second"],
            "Money": ["dollar", "coin", "bank", "wallet", "cash"],
            "Shopping": ["cart", "bag", "store", "price", "sale"],
            "Travel": ["plane", "train", "bus", "car", "boat"],
            "Camping": ["tent", "fire", "marshmallow", "forest", "lake"],
            "Fishing": ["rod", "bait", "fish", "lake", "boat"],
            "Cooking": ["pan", "pot", "oven", "stove", "recipe"],
            "Baking": ["flour", "sugar", "butter", "oven", "cake"],
            "Exercise": ["run", "jump", "lift", "stretch", "yoga"],
            "Health": ["doctor", "medicine", "hospital", "nurse", "pill"],
            "Weather": ["sunny", "rainy", "cloudy", "windy", "snowy"],
            "Disaster": ["flood", "earthquake", "tornado", "hurricane", "fire"],
            "Emergency": ["police", "fireman", "ambulance", "siren", "rescue"],
            "Crime": ["thief", "robber", "jail", "gun", "detective"],
            "Law": ["judge", "jury", "lawyer", "court", "prison"],
            "Military": ["soldier", "tank", "gun", "plane", "ship"],
            "Politics": ["vote", "president", "senator", "law", "election"],
            "News": ["tv", "radio", "newspaper", "report", "anchor"],
            "Media": ["movie", "song", "book", "game", "show"],
            "Social": ["friend", "family", "party", "chat", "group"],
            "Feelings": ["love", "hate", "fear", "joy", "sorrow"],
            "Senses": ["see", "hear", "touch", "taste", "smell"],
            "Directions": ["north", "south", "east", "west", "up"],
            "Sizes": ["big", "small", "tall", "short", "wide"]
        }
        self.difficulties = {"Easy": 8, "Medium": 6, "Hard": 4}
        self.reset_game()

    def reset_game(self):
        self.category = "Animals"
        self.difficulty = "Medium"
        self.word = ""
        self.correct_guesses = set()
        self.used_letters = set()
        self.attempts_left = 0
        self.game_over = False
        self.score = 0
        self.timer = 60  # 60 seconds per game

    def start_game(self, category, difficulty):
        self.category = category
        self.difficulty = difficulty
        self.word = random.choice(self.words[category]).lower()
        self.correct_guesses = set()
        self.used_letters = set()
        self.attempts_left = self.difficulties[difficulty]
        self.game_over = False
        self.score = 0
        self.timer = 60

    def get_hint(self):
        if self.score >= 10 and not self.game_over:
            unguessed = [char for char in self.word if char not in self.correct_guesses]
            if unguessed:
                hint_letter = random.choice(unguessed)
                self.correct_guesses.add(hint_letter)
                self.score -= 10
                return hint_letter
        return None

game = HangmanGame()

@app.route('/')
def index():
    if 'username' not in session:
        session['username'] = ''
    if 'history' not in session:
        session['history'] = []
    return render_template('index.html', 
                         categories=game.words.keys(), 
                         difficulties=game.difficulties.keys(),
                         username=session['username'],
                         history=session['history'])

@app.route('/set_username', methods=['POST'])
def set_username():
    username = request.form['username']
    session['username'] = username
    return jsonify({'message': f'Welcome, {username}!'})

@app.route('/start', methods=['POST'])
def start_game():
    category = request.form['category']
    difficulty = request.form['difficulty']
    game.start_game(category, difficulty)
    return jsonify({
        'word_display': ' '.join(['_' for _ in game.word]),
        'attempts_left': game.attempts_left,
        'used_letters': '',
        'message': 'Game started!',
        'score': game.score,
        'timer': game.timer
    })

@app.route('/guess', methods=['POST'])
def guess():
    if game.game_over:
        return jsonify({'message': 'Game is over! Please start a new game.'})

    guess = request.form['guess'].lower()
    if not guess.isalpha() or len(guess) != 1:
        return jsonify({'message': 'Please enter a single letter'})

    if guess in game.used_letters:
        return jsonify({'message': 'Letter already guessed'})

    game.used_letters.add(guess)
    message = ''
    
    if guess in game.word:
        game.correct_guesses.add(guess)
        message = 'Good guess!'
        game.score += 5  # +5 points for correct guess
    else:
        game.attempts_left -= 1
        message = 'Wrong guess!'

    word_display = ' '.join([char if char in game.correct_guesses else '_' for char in game.word])
    
    if '_' not in word_display:
        game.game_over = True
        message = 'You won!'
        game.score += game.attempts_left * 10  # Bonus for remaining attempts
        session['history'].append({
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'word': game.word,
            'result': 'Won',
            'difficulty': game.difficulty,
            'score': game.score
        })
    elif game.attempts_left == 0:
        game.game_over = True
        message = f'You lost! The word was: {game.word}'
        session['history'].append({
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'word': game.word,
            'result': 'Lost',
            'difficulty': game.difficulty,
            'score': game.score
        })

    session.modified = True
    return jsonify({
        'word_display': word_display,
        'attempts_left': game.attempts_left,
        'used_letters': ', '.join(sorted(game.used_letters)),
        'message': message,
        'score': game.score,
        'timer': game.timer,
        'hangman_stage': game.difficulties[game.difficulty] - game.attempts_left
    })

@app.route('/hint', methods=['POST'])
def hint():
    if game.game_over:
        return jsonify({'message': 'Game is over! No hints available.'})

    hint_letter = game.get_hint()
    if hint_letter:
        word_display = ' '.join([char if char in game.correct_guesses else '_' for char in game.word])
        return jsonify({
            'message': f'Hint: Letter {hint_letter} revealed!',
            'word_display': word_display,
            'score': game.score
        })
    return jsonify({'message': 'Not enough points for a hint!'})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['history'] = []
    session.modified = True
    return jsonify({'message': 'History cleared!'})

if __name__ == '__main__':
    app.run(debug=True)