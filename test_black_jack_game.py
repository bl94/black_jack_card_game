import unittest

from black_jack_game_code_to_unit_test import Card,main

class TestBlackJackGame(unittest.TestCase):
    def test_black_jack_game(self):
        cards=[Card("Spades","Nine"),Card("Hearts","Ten"),Card("Hearts","Ten"),Card("Hearts","Seven"),Card("Clubs","Two"),Card("Diamonds","Three")]
        self.assertEqual(main(cards),2) #1-means win dealer,2-means win player
  
if __name__=='__main__':
    unittest.main()