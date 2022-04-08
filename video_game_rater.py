##
# video_game_rater.py
# Rates video games

def print_dictionary(dictionary):
    """
    Accepts a dictionary , loops through it and
    prints out the game and its rating
    """
    # outer dictionary
    for id, game in dictionary.items():
        print("Id: {} Game: {}\tRating: {}".format (id,
                                                    game["name"],
                                                    game["rating"]))

if __name__ == "__main__":
    
    videogames = {1:{"name":"Minecraft", "rating":5}
                  2:{"name":"Call of Duty","rating":1}
                  3:{"name":"Angry Birds", "rating":4}
                  4:{"name":"Splatoon 2", "rating":5}
                  5:{"name":"Animal Crossing","rating":4}}
    
    print_dictionary(video_games)
    
