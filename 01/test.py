import Cross
import unittest


class TestCross(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Cross.Game()
    def test_input(self):
        self.base_table = [['1', 'X', '3',
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
        self.base_input = ['2', '10', 'X', '1']
        self.base_ans = [False, False, False, True]
        for test in range(len(self.base_ans)):
            self.obj.board = self.base_table[test]
            self.assertEqual(self.obj.take_input(self.base_input[test]), self.base_ans[test])
                      
    

    def test_draw(self):
        self.base_table = [['1', 'X', '3',
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
        for i in self.base_table:
            self.obj.board = i
            self.assertIsNone(self.obj.draw())

    def test_win(self):
        self.base_table = [['1', 'X', '3',
                       '4', '5', '6',
                       '7', '8', '9'], #Nobody wins
                      ['X', '2', 'O',
                       '4', 'X', 'O',
                       'O', '8', 'X'], #X wins
                       ['1', 'X', '3',
                       'O', 'O', 'O',
                       '7', 'X', 'X']] #O wins                      
        self.base_ans = [False, 'X', 'O']
        for test in range(len(self.base_ans)):
            self.obj.board = self.base_table[test]
            self.assertEqual(self.obj.check_win(), self.base_ans[test])
