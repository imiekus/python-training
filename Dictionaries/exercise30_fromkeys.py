# Use dict.fromkeys to generate a new dictionary using the provided game_properties list. Initialize all values to 0.
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]

initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)