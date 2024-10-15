import Ability_Scores
import Game

dnd_ability_scores = Ability_Scores(["str", "dex", "con", "int", "wis", "cha"])
DND = Game("Dungeons and Dragons", dnd_ability_scores)


witchcraft_ability_scores = Ability_Scores(
    ["str", "dex", "con", "int", "per", "wil"])
WITCHCRAFT = Game("Witchcraft", witchcraft_ability_scores)
