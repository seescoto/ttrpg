import MiscFunctions as MF


class Ability_Scores:

    ability_scores: list[str]
    ability_modifiers: dict[int, int]

    def __init__(self, ability_scores: list[str]) -> None:
        """set which attributes/stats/ability score categories that a character in a given game will

        Args:
            ability_scores (list[str]): list of ability score categorites. (e.g. in dnd the list would read 
                ["str", "dex", "con", "int", "wis", "cha"])
        """
        self.ability_scores = ability_scores

    def set_char_ability_scores(self, score_list: list[int]) -> dict[str, int]:
        """given a list [x1, x2, ..., xn] of scores, set a character ability_score list of the 
        character ability_scores in self.ability_score set to the scores x1, x2, ..., xn

        Args:
            score_list (list[int]): list of the scores the character will have for each ability_score
                in self.ability_scores

        Returns:
            dict: dictionary in the pattern {ability_score/stat/ability score : score for character}
        """
        score_list = MF.make_same_size(
            self.ability_scores, score_list)
        char_ability_scores = {}
        for i in range(len(score_list)):
            char_ability_scores[self.ability_scores[i]] = score_list[i]

        return char_ability_scores

    def set_ability_modifiers(self, ability_modifiers: dict[int, int]) -> None:
        self.ability_modifiers = ability_modifiers
