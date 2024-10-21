class Animal:
    def __init__(self, arms, legs, eyes, tail, fur):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.fur = fur

    def print(self):
        print("Animal Characteristics")
        print(f"Length of Arms = {self.arms}")
        print(f"Length of Legs = {self.legs}")
        print(f"Number of Eyes = {self.eyes}")
        print(f"Has a Tail: {'Yes' if self.tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.fur else 'No'}")

# Example usage
cheetah = Animal(arms=93.5, legs=85.3, eyes=2, tail=True, fur=True)
cheetah.print()