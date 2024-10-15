from Ability_Scores import Ability_Scores


class Game:

    stat_system: Ability_Scores  # system to store/record ability scores
    health_formula: dict
    name: str
    dice: list[int]

    def __init__(self, name: str, stat_system: Ability_Scores, dice: list[int] = [20]) -> None:

        self.name = name
        self.stat_system = stat_system
        # says base heath is 0, no other changes
        self.health_formula = {"base": 0}
        self.dice = dice

    def set_health_formula(self, base_health: int = 0, **kwargs) -> None:
        """changes the health formula based on kwargs. if keys match up to attributes in the ability 
        score categories, then the formula uses the coefficient to add it up. for example if the inputs are 
        set_health_formula(base_health = 10, str = 4 con = 4) then the formula for health is 
        health = 10 + (4*str) + (4*con), like in 5e dnd.

        Args:
            base_health (int, optional): _description_. Defaults to 0.
            ability_score = number
        """
        self.health_formula["base"] = base_health
        for k, v in kwargs:
            # if it's an ability score category AND the value is a number then add it to the formula
            if (k in (self.stat_system.ability_scores)) and (isinstance(v, (int, float)) and not isinstance(v, bool)):
                self.health_formula[k] = v

    def get_char_health(self, char_ability_scores: dict[str, int]) -> int:
        """returns a character's health based on the game's health formula and the character's ability scores.

        Args:
            char_ability_scores (dict): with keys being {ability score : score} (e.g. {"cha": 5}, etc.)

        Returns:
            number : character's health based on the game's health formula and their ability scores/stats
        """
        formula = self.health_formula
        health = self.health_formula["base"]

        # if the game's formula is {"con": 4, "str": 4, "base": 10} then the formula for getting health would be
        # health = 10 + 4(con_score) + 5(con_score)
        # where con_score and con_score are keys in char_ability_scores.
        for k, v in char_ability_scores.items():
            if (k in formula.keys()):
                health += char_ability_scores[k] * formula[k]

        return health
