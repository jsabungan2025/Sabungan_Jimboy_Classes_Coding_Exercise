class MagicCard:
    DEFAULT_SET = "Core Set"

    def __init__(self, card_name, mana_cost, type_line, rules_text, flavor_text, power_toughness, DEFAULT_SET=None):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.type_line = type_line
        self.rules_text = rules_text
        self.flavor_text = flavor_text
        self.power_toughness = power_toughness

        if DEFAULT_SET is None:
            self.DEFAULT_SET = MagicCard.DEFAULT_SET
        else:
            self.DEFAULT_SET = DEFAULT_SET

    def display_card(self):
        print("=" * 100)
        print(f"Card Name: {self.card_name}")
        print(f"Mana Cost: {self.mana_cost}")
        print(f"Type Line: {self.type_line}")
        print(f"Rules Text: {self.rules_text}")
        print(f"Flavor Text: {self.flavor_text}")
        print(f"Power/Toughness: {self.power_toughness}")
        print(f"Default Set: {self.DEFAULT_SET}")
        print("=" * 100)


card_1 = MagicCard(
    "Farhaven Elf",
    "2",
    "Creature - Elf Druid",
    "When Farhaven Elf comes into play, you may search your library "
    "for a basic land card and put it into play tapped.",
    "Verdant bloom does exist. It merely hides for its own safety.",
    "1/1"
)

card_2 = MagicCard(
    "Thragtusk",
    "4",
    "Creature — Beast",
    "When Thragtusk enters the battlefield, you gain 5 life.",
    "Always carry two spears.",
    "5/3"
)


def main():
    global input_user_name

    print("=" * 100)
    input_user_name = input("Enter your name: ")
    print(f"Welcome, {input_user_name}!")
    print("=" * 100)

    print("Available Characters:")
    print()

    print("Character 1:")
    card_1.display_card()

    print("Character 2:")
    card_2.display_card()


def choose_character():
    while True:
        print("=" * 100)

        choice = input(
            "Choose a character (character_1 or character_2): "
        ).lower()

        if choice == "character_1" or choice == "1":
            print("You selected Farhaven Elf!")
            card_1.display_card()
            break

        elif choice == "character_2" or choice == "2":
            print("You selected Thragtusk!")
            card_2.display_card()
            break

        else:
            print(
                "Invalid choice. Please choose either "
                "'character_1' or 'character_2'."
            )


def start_game():
    global Health
    global Opponent_Health
    global card_in_hand
    global Opponent_card_in_hand
    global opponent_name

    Health = 20
    Opponent_Health = 20
    card_in_hand = 5
    Opponent_card_in_hand = 5
    opponent_name = "Terrorblade"


def players_status():
    print("=" * 100)
    print(f"{input_user_name}'s Health: {Health}")
    print(f"{opponent_name}'s Health: {Opponent_Health}")
    print(f"{input_user_name}'s Cards in Hand: {card_in_hand}")
    print(f"{opponent_name}'s Cards in Hand: {Opponent_card_in_hand}")
    print("=" * 100)


def play_turn():
    global Health
    global Opponent_Health
    global card_in_hand
    global Opponent_card_in_hand

    while True:
        print("Choose an action:")
        print("1. Declare Attacker")
        print("2. Block")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            Opponent_Health -= 3

            if Opponent_card_in_hand > 0:
                Opponent_card_in_hand -= 1

            print(
                "You declare an attacker and your opponent "
                "receives 3 damage!"
            )
            break

        elif choice == "2":
            Health -= 2

            if card_in_hand > 0:
                card_in_hand -= 1

            print(
                "You declare a blocker and you receive 2 damage!"
            )
            break

        else:
            print(
                "Invalid choice. Please choose either '1' or '2'."
            )

    print("=" * 100)
    print("Updated Game Status:")
    players_status()


def check_winner():
    if Health <= 0:
        print(f"{input_user_name} has been defeated!")
        print("Better luck next time!")
        return True

    if Opponent_Health <= 0:
        print(f"{opponent_name} has been defeated!")
        print("Congratulations! You win the game!")
        return True

    return False


def continuation():
    while True:
        if check_winner():
            return

        choice = input(
            "Do you want to continue playing? (yes/no): "
        ).lower()

        if choice == "yes":
            play_turn()

        elif choice == "no":
            print("Thank you for playing!")
            return

        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
    choose_character()
    start_game()
    players_status()
    play_turn()
    continuation()