from Game import Game
import random


class Character:

    game: Game
    ability_scores: dict[str, int]
    health: int
    level: int
    char_class: str
    char_name: str

    def __init__(self, game: Game, char_name: str, ability_score_list: list[int], char_class: str = None,
                 char_health: int = 0, level: int = 1) -> None:
        """initializes an instance of Character

        Args:
            game (class Game): what type of game this character is in (e.g. dnd 5e, pathfinder, etc.)
            char_name (str): the character's name
            char_class (str, optional): what class/type/designation the character has. Defaults to None.
            char_health (int, optional): does this character have a non-standard health value that isn't correctly calculated by the game?
        """
        self.game = game
        self.name = char_name
        self.ability_scores = self.set_ability_scores(
            ability_score_list)  # is a dictionary
        self.health = game.get_char_health(self.ability_scores)
        self.char_class = char_class

    def set_ability_scores(self, ability_score_list: list[int]) -> None:
        # sets or resets a character's stats/ability scores
        self.ability_scores = self.game.stat_system.set_char_ability_scores(
            ability_score_list)

    def level_up(self) -> None:
        self.level += 1

    def roll(self, dice_sides: int = 20) -> int:
        return random.randint(1, dice_sides)

    def roll_saving_throw(self, saving_throw: int, throw_type: str = None, dice_sides: int = 20):
        roll = self.roll(dice_sides)
        bonus = 0
        # add bonuses based on modifiers
        if (throw_type in self.game.stat_system.ability_scores) and (self.game.ability_modifiers is not None):
            score = self.ability_scores[throw_type]
            bonus = self.game.stat_system.ability_modifiers.get(score, 0)

        outcome = ["Yes!", "succeeded"]
        if (roll + bonus <= saving_throw):
            outcome = ["Oh no!", "failed"]

        print(
            f'{outcome[0]} {self.name} {outcome[1]} their saving throw with a roll of a {roll}')
        if (bonus != 0):
            print(
                f'and a bonus ability modifier of {bonus} for a total value of {roll+bonus}')

        print(f'.\n')
