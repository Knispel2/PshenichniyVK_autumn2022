import unittest
import sys
import os
import cross


class TestCross(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = cross.Game()
        sys.stdout = open(os.devnull, 'w', encoding='utf8')
    def test_input(self):
        base_table = [['1', 'X', '3',
                       '4', '5', '6',
                       '7', '8', '9'], # occup
                      ['1', '2', '3',
                       '4', '5', '6',
                       '7', '8', '9'], # out of board
                       ['1', '2', '3',
                       '4', '5', 'O',
                       '7', 'X', '9'], # incorr. input
                       ['1', '2', '3',
                       '4', '5', 'O',
                       '7', 'X', '9']] # OK
        base_input = ['2', '10', 'X', '1']
        base_ans = [False, False, False, True]
        buf_len = len(base_ans)
        for test in range(buf_len):
            self.obj.board = base_table[test]
            self.assertEqual(self.obj.take_input(base_input[test]), base_ans[test])

    def test_draw(self):
        base_table = [['1', 'X', '3',
                       '4', '5', '6',
                       '7', '8', '9'],
                      ['1', '2', '3',
                       '4', '5', '6',
                       '7', '8', '9'],
                       ['1', '2', '3',
                       '4', '5', 'O',
                       '7', 'X', '9'],
                       ['1', '2', '3',
                       '4', '5', 'O',
                       '7', 'X', '9']]
        for i in base_table:
            self.obj.board = i
            self.assertIsNone(self.obj.draw())

    def test_win(self):
        base_table = [['1', 'X', '3',
                       '4', '5', '6',
                       '7', '8', '9'], #Nobody wins
                      ['X', '2', 'O',
                       '4', 'X', 'O',
                       'O', '8', 'X'], #X wins
                       ['1', 'X', '3',
                       'O', 'O', 'O',
                       '7', 'X', 'X']] #O wins
        base_ans = [False, 'X', 'O']
        buf_len = len(base_ans)
        for test in range(buf_len):
            self.obj.board = base_table[test]
            self.assertEqual(self.obj.check_win(), base_ans[test])

    def test_allgame(self):
        games = [['5', '1', '6', '4', '7', '3', '9', '8', '2'],
                      ['5', '6', '3', '8', '7'],]
        result = [0, 1]
        buf_len = len(games)
        for i in range(buf_len):
            self.obj.board = list(range(1,10))
            for x_data in games[i][:-1]:
                self.obj.game_start(auto=True, pos=x_data)
            self.assertEqual(self.obj.game_start(auto=True, pos=games[i][-1]), result[i])

    def tearDown(self) -> None:
        sys.stdout.close()
        sys.stdout = sys.__stdout__
