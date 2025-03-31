class Game():
    def __init__(self, turn='X'):
        self.turn = turn
        self.tie = False
        self.winner = None
        self.board = {

            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,

        }

    def make_move(self):
        move = input('Choose your square:').lower()
        if move in self.board and self.board[move] is None:
            self.board[move] = self.turn
            return f'{move} marked with {self.turn}'
        else:
            return 'Invalid move. Try again.'

    def render(self):

        b = self.board
        print(f"""
      A   B   C
    1) {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
       -----------
    2) {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
       -----------
    3) {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
    """)

        if self.tie and not self.winner:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    
    def place_piece(self):
        while True:
            move = input(f"Enter a valid movie (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print('Invalid move. Try again')
    
    
    def check_for_winner(self):
        winning_combinations = [
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
        ]
        for combo in winning_combinations:
            marks = [self.board[pos] for pos in combo]
            if marks == [self.turn] * 3:
                self.winner = self.turn

                return True
        return False            
    
    def check_for_tie(self):
        if not self.check_for_winner() and all(value is not None for value in self.board.values()):
            self.tie = True 
            print('Its a Tie!, Play again?')

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"

        else:
            self.turn = "X"

        print(f"It's {self.turn}'s turn")

     
    def play_game(self):
        print("Shall we play a game?")
        
        while self.winner is None and not self.tie:
            self.render()
            self.place_piece()
            if self.check_for_winner():
                self.render()
                break
            self.check_for_tie()
            if self.tie:
                self.render()
                break
            self.switch_turn()


           

   
    
    



game_instance = Game()
game_instance.play_game()

