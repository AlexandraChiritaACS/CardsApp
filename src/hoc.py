import itertools, random

'''References:
    https://www.programiz.com/python-programming/examples/shuffle-card
    https://www.youtube.com/watch?v=VW7yBYBN6hs
    https://www.youtube.com/watch?v=zvXn5ppVB2c
'''

class Cards:
    def __init__(self):
        # Pake a deck of cards
        self.deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
        self.symbol = {"Club": "\u2663",
                        "Spade": "\u2660",
                        "Diamond": "\u2666",
                        "Heart": "\u2665"}

    def pick_a_card(self, pos):
        # Pick a card from the list
        return self.deck[pos][0], self.deck[pos][1]

    def print_card(self, number, name):
        # Display card from the deck
        print(number, "of", name)

    def simple_shuffle(self):
        # Simple shuffle (for everybody)
        random.shuffle(self.deck)

    def overhand_shuffle(self, seconds, speed, error):
        
        # Classic overhand shuffle
        length = len(self.deck)

        for i in range(seconds * speed):
            # Get the 2 halfs of the deck
            middle_index = random.randint(length//2 - error, length//2 + error)
            first_half = self.deck[:middle_index]
            second_half = self.deck[middle_index:]
            self.deck.clear()
            self.deck.extend(second_half)
            self.deck.extend(first_half)

    def riffle_shuffle(self, seconds, speed, error, long_shuffle=False):
        
        length = len(self.deck)

        for i in range(seconds * speed):
            middle_index = random.randint(length//2 - error, length//2 + error)
            first_half = self.deck[:middle_index]
            second_half = self.deck[middle_index:]
            # The long shuffle has also a random step
            if (long_shuffle == True):
                random.shuffle(first_half)
                random.shuffle(second_half)
            self.deck.clear()
            
            for j in range(min(len(first_half), len(second_half))):
                r = random.randint(0, 1)
                # Mix the cards in the hand
                if (r == 0):
                    self.deck.append(first_half[j])
                    self.deck.append(second_half[j])
                else:
                    self.deck.append(second_half[j])
                    self.deck.append(first_half[j])
            
            # Put the rest of the cards in the pack
            if (len(first_half) > len(second_half)):
                self.deck.extend(first_half[len(second_half):])
            else:
                self.deck.extend(second_half[len(first_half):])

    def get_all(self):

        # Display all cards

        print("You got:")
        for i in range(len(self.deck)):
            number, name = self.pick_a_card(i)
            self.print_card(number, self.symbol[name])

    def pop_card(self):
        return self.deck.pop()

    def pop_all(self):

        # Display all cards

        print("You got:")
        for i in range(len(self.deck)):
            card = self.pop_card()
            number = card[0]
            name = card[1]
            self.print_card(number, self.symbol[name])

class Test:
    def __init__(self):
        self.pack = Cards()
    
    def basic_test(self):
        # Test random shuffle
        self.pack.simple_shuffle()
        print("Test 0 (simple random shuffle)")
        self.pack.get_all()
    
    def overhand_shuffle_test(self):
        # Test overhand shuffle
        self.pack.overhand_shuffle(5, 3, 9)
        print("Test 1.1 (simple overhand shuffle)")
        self.pack.get_all()
        print("Test 1.2 (multiple overhand shuffle)")
        self.pack.overhand_shuffle(1, 10, 5)
        self.pack.overhand_shuffle(5, 30, 4)
        self.pack.overhand_shuffle(10, 1, 3)
        self.pack.get_all()

    def riffle_shuffle_test(self):
        # Test riffle and long shuffle
        self.pack.riffle_shuffle(5, 3, 9)
        print("Test 2.1 (simple riffle shuffle)")
        self.pack.get_all()
        print("Test 2.2 (multiple riffle shuffle)")
        self.pack.riffle_shuffle(1, 10, 5)
        self.pack.riffle_shuffle(5, 30, 4)
        self.pack.riffle_shuffle(10, 1, 3)
        self.pack.get_all()
        print("Test 2.3 (multiple long shuffle)")
        self.pack.riffle_shuffle(1, 10, 5, True)
        self.pack.riffle_shuffle(5, 30, 4)
        self.pack.riffle_shuffle(10, 1, 3, True)
        self.pack.get_all()
    
    def test_all(self):
        # Test all the shuffle techniques
        print("Test 3 (final test with all types of shuffle)")
        self.pack.simple_shuffle()
        self.pack.simple_shuffle()
        self.pack.riffle_shuffle(1, 12, 5, True)
        self.pack.riffle_shuffle(5, 20, 4)
        self.pack.overhand_shuffle(1, 10, 3)
        self.pack.riffle_shuffle(10, 10, 4)
        self.pack.overhand_shuffle(2, 30, 5)
        self.pack.overhand_shuffle(3, 40, 2)
        self.pack.riffle_shuffle(1, 10, 3, True)
        self.pack.pop_all()
