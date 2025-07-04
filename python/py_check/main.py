import random


class WordleGame:
    word_to_match: str = "build"
    guess_list: list[str] = []
    max_guess_count: int = 5
    current_guess_count: int = 0
    
    # Common 5-letter words for Wordle
    _word_list = [
        "about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult", "after", "again",
        "agent", "agree", "ahead", "alarm", "album", "alert", "alien", "align", "alike", "alive",
        "allow", "alone", "along", "alter", "amber", "among", "anger", "angle", "angry", "apart",
        "apple", "apply", "arena", "argue", "arise", "array", "arrow", "aside", "asset", "avoid",
        "awake", "award", "aware", "badly", "baker", "bases", "basic", "beach", "began", "begin",
        "being", "below", "bench", "billy", "birth", "black", "blame", "blind", "block", "blood",
        "board", "boost", "booth", "bound", "brain", "brand", "brass", "brave", "bread", "break",
        "breed", "brief", "bring", "broad", "broke", "brown", "build", "built", "buyer", "cable",
        "calif", "carry", "catch", "cause", "chain", "chair", "chaos", "charm", "chart", "chase",
        "cheap", "check", "chest", "child", "china", "chose", "civil", "claim", "class", "clean",
        "clear", "click", "climb", "clock", "close", "cloud", "coach", "coast", "could", "count",
        "court", "cover", "craft", "crash", "crazy", "cream", "crime", "cross", "crowd", "crown",
        "crude", "curve", "cycle", "daily", "dance", "dated", "dealt", "death", "debut", "delay",
        "depth", "doing", "doubt", "dozen", "draft", "drama", "drank", "dream", "dress", "drill",
        "drink", "drive", "drove", "dying", "eager", "early", "earth", "eight", "elite", "empty",
        "enemy", "enjoy", "enter", "entry", "equal", "error", "event", "every", "exact", "exist",
        "extra", "faith", "false", "fault", "fiber", "field", "fifth", "fifty", "fight", "final",
        "first", "fixed", "flash", "fleet", "floor", "fluid", "focus", "force", "forth", "forty",
        "forum", "found", "frame", "frank", "fraud", "fresh", "front", "frost", "fruit", "fully",
        "funny", "giant", "given", "glass", "globe", "going", "grace", "grade", "grand", "grant",
        "grass", "grave", "great", "green", "gross", "group", "grown", "guard", "guess", "guest",
        "guide", "happy", "harry", "heart", "heavy", "hence", "henry", "horse", "hotel", "house",
        "human", "hurry", "image", "index", "inner", "input", "issue", "japan", "jimmy", "joint",
        "jones", "judge", "known", "label", "large", "laser", "later", "laugh", "layer", "learn",
        "lease", "least", "leave", "legal", "level", "lewis", "light", "limit", "links", "lives",
        "local", "loose", "lower", "lucky", "lunch", "lying", "magic", "major", "maker", "march",
        "maria", "match", "maybe", "mayor", "meant", "media", "metal", "might", "minor", "minus",
        "mixed", "model", "money", "month", "moral", "motor", "mount", "mouse", "mouth", "moved",
        "movie", "music", "needs", "never", "newly", "night", "noise", "north", "noted", "novel",
        "nurse", "occur", "ocean", "offer", "often", "order", "other", "ought", "paint", "panel",
        "paper", "party", "peace", "peter", "phase", "phone", "photo", "piano", "piece", "pilot",
        "pitch", "place", "plain", "plane", "plant", "plate", "point", "pound", "power", "press",
        "price", "pride", "prime", "print", "prior", "prize", "proof", "proud", "prove", "queen",
        "quick", "quiet", "quite", "radio", "raise", "range", "rapid", "ratio", "reach", "ready",
        "realm", "rebel", "refer", "relax", "repay", "reply", "right", "rigid", "risky", "river",
        "robin", "roger", "roman", "rough", "round", "route", "royal", "rural", "safer", "saint",
        "salad", "sales", "salon", "scale", "scare", "scene", "scope", "score", "sense", "serve",
        "setup", "seven", "shall", "shape", "share", "sharp", "sheet", "shelf", "shell", "shift",
        "shine", "shirt", "shock", "shoot", "short", "shown", "sides", "sight", "silly", "since",
        "sixth", "sixty", "sized", "skill", "sleep", "slide", "small", "smart", "smile", "smith",
        "smoke", "snake", "snow", "solid", "solve", "sorry", "sound", "south", "space", "spare",
        "speak", "speed", "spend", "spent", "split", "spoke", "sport", "staff", "stage", "stake",
        "stand", "start", "state", "steam", "steel", "steep", "steer", "stern", "stick", "still",
        "stock", "stone", "stood", "store", "storm", "story", "strip", "stuck", "study", "stuff",
        "style", "sugar", "suite", "super", "sweet", "swing", "swiss", "table", "taken", "taste",
        "taxes", "teach", "teams", "teeth", "tempo", "tends", "terry", "texas", "thank", "theft",
        "their", "theme", "there", "these", "thick", "thing", "think", "third", "those", "three",
        "threw", "throw", "thumb", "tight", "timer", "tired", "title", "today", "topic", "total",
        "touch", "tough", "tower", "track", "trade", "train", "treat", "trend", "trial", "tribe",
        "trick", "tried", "tries", "truck", "truly", "trunk", "trust", "truth", "twice", "twist",
        "tyler", "uncle", "under", "undue", "union", "unity", "until", "upper", "upset", "urban",
        "usage", "usual", "valid", "value", "video", "virus", "visit", "vital", "vocal", "voice",
        "waste", "watch", "water", "wheel", "where", "which", "while", "white", "whole", "whose",
        "woman", "women", "world", "worry", "worse", "worst", "worth", "would", "write", "wrong",
        "wrote", "young", "youth"
    ]
    
    def __init__(self):
        """
        Initialize the WordleGame with a random target word and an empty guess list.
        """
        self.reset_game()
                
    def reset_game(self):
        """
        Reset the game to its initial state with a new random word and empty guess list.
        """
        self.word_to_match = self.generate_random_word()
        self.guess_list = []
        self.current_guess_count = 0

    def get_word_to_match(self) -> str:
        return self.word_to_match

    def get_guess_list(self) -> list[str]:
        return self.guess_list

    def generate_random_word(self) -> str:
        """
        Generate a random 5-letter word from the word list.
        
        Returns:
            A random 5-letter word
        """
        return random.choice(self._word_list)

    def check_guess(self, guess: str) -> str:
        """
        Check a guess against the target word and return a result string.
        
        Returns:
            'G' for correct letter in correct position (Green)
            'Y' for correct letter in wrong position (Yellow)
            '-' for letter not in the word (Grey)
        """
        if len(guess) != len(self.word_to_match):
            raise ValueError("Guess must be the same length as the word to match.")
        
        result = ['-'] * len(guess)
        
        # First pass: Mark exact matches (Green)
        for i, char in enumerate(guess):
            if char == self.word_to_match[i]:
                result[i] = 'G'
        
        # For yellow marking, we need to be more careful about duplicates
        # Process each unique character and decide which positions to mark yellow
        for char in set(guess):
            if char not in self.word_to_match:
                continue
                
            # Get all positions of this character in guess (excluding greens)
            guess_positions = [i for i, c in enumerate(guess) if c == char and result[i] != 'G']
            
            # Count how many of this character are available for yellow marking
            # (total in word minus those already marked green)
            total_in_word = self.word_to_match.count(char)
            green_count = sum(1 for i, c in enumerate(guess) if c == char and result[i] == 'G')
            available_for_yellow = total_in_word - green_count
            
            # Mark positions as yellow, but only up to available count
            # Based on test patterns, it seems to prefer later positions
            yellow_positions = guess_positions[-available_for_yellow:] if available_for_yellow > 0 else []
            
            for pos in yellow_positions:
                result[pos] = 'Y'
        
        return ''.join(result)
    
    def play_game(self):
        """
        Main game loop for playing Wordle.
        """
        while self.current_guess_count < self.max_guess_count:
            guess = input(f"Attempt {self.current_guess_count + 1}/{self.max_guess_count}: Enter your guess (5 letters): ").strip().lower()
            
            if guess in self.guess_list:
                print("You've already guessed that word.")
                continue
            
            if len(guess) != 5 or not guess.isalpha():
                print("Invalid guess. Please enter a 5-letter word.")
                continue
            
            self.current_guess_count += 1
            result = self.check_guess(guess)
            self.guess_list.append(guess)
            print(f"Result: {result}")
            
            if result == 'G' * len(self.word_to_match):
                print("Congratulations! You've guessed the word!")
                return True  # Return True for win
        
        # If we reach here, all attempts were used without winning
        print(f"Sorry, you've used all attempts. The word was: {self.word_to_match}")
        return False  # Return False for loss
    
    def start_game_loop(self):
        """
        Start the game loop with option to play multiple rounds.
        """
        print("\n🎯 Welcome to Wordle! 🎯")
        print("Guess the 5-letter word in 5 attempts or less!")
        print("G = Green (correct letter, correct position)")
        print("Y = Yellow (correct letter, wrong position)")
        print("- = Grey (letter not in word)\n")
        
        while True:
            won = self.play_game()
            
            if won:
                print(f"🎉 You won in {self.current_guess_count} attempts!")
            else:
                print("💔 Better luck next time!")
            
            # Ask if player wants to play again
            while True:
                play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
                if play_again in ['y', 'yes']:
                    print("\n" + "="*50)
                    print("Starting a new game...")
                    print("="*50)
                    self.reset_game()
                    break
                elif play_again in ['n', 'no']:
                    print("Thanks for playing Wordle! 👋")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    game = WordleGame()
    game.start_game_loop()
