from src.VISELICA.VISELICA import Game
from src.VISELICA.gameStatus import GameStatus

game = Game()
word = game.generate_word()

letters_count = len(word) # Count of letters in random word
print(f'Ugaday slovo sostoin iz {letters_count} bukv')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('guess letter:')
    state = game.set_letter(letter)

    print(game.get_current_string())
    print(f'Remaining tries: {game.get_count_tries()}')
    print(f'your letters: {game.get_my_letters()}') # All letters, which player used
    if GameStatus.WIN == game.game_status:
        print('congratulations you WON!')
    elif game.game_status == GameStatus.LOSE:
        print('sorry you LOST')
        print(f'The word was: {game.random_word}')
