class Game():

    board = list(range(1,10))
    counter = 0
    sym = {0 : 'X', 1 : 'O'}

    def draw(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0+i*3], "|", self.board[1+i*3], "|", self.board[2+i*3], "|")
            print("-" * 13)

    def take_input(self, player_answer):
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Incorrect input!")
            return False
        if player_answer >= 1 and player_answer <= 9:
            if (str(self.board[player_answer-1]) not in "XO"):
                self.board[player_answer-1] = self.sym[self.counter % 2]
                self.counter += 1
                return True
            else:
                print("This cell is occupied!")
                return False
        else:
            print("Incorrect input!")
            return False

    def check_win(self):
        win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
        for each in win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def game_start(self, auto = False, pos = ''):
        while True:
            self.draw()
            while not self.take_input(input(f"Enter the position ({self.sym[self.counter % 2]}): ")
                                      if not auto else pos):
                pass
            if self.counter > 3:
                buf = self.check_win()
                if buf:
                    print(buf, "wins!")
                    self.draw()
                    return 1
            if self.counter == 9:
                print("Nobody wins!")
                self.draw()
                return 0
            if auto:
                break


if __name__ == '__main__':
    process = Game()
    process.game_start()
