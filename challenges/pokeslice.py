#!/usr/bin/env python3
# https://github.com/JasonTrespel/Python/blob/master/challenges/API%20CHALLENGE-%20ISS.md
import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # print(pokeapi)

    #     Part 1- Slicing (NO for loop!)
    #     Find the "sprites" key. Print the URL to "front_default", which is a link to an image of your Pokemon!

    img = pokeapi['sprites']['front_default']

    wget.download(img, "/home/student/static/")

    # Part 2- Slicing WITH a for loop!
    # Look at the "moves" key. It returns a list of dictionaries; each dictionary contains the name of one of the Pokemon's "moves."
    # Print out the "name"s of ALL the selected Pokemon's "moves".

    # for move in pokeapi['moves']:
    #     print(move['move']['name'])

    # Part 3- Loop or NOT to Loop
    # Look at the "game_indices" key. This returns a list of dictionaries; each dictionary contains the name of each Pokemon game this character appeared in! (Pokemon Red, Pokemon Black, Pokemon Crystal, etc.
    # Count up the total number of games this Pokemon character appeared in. You can solve this with a loop or without a loop... your choice!
    # Print the count of how many games the selected Pokemon has been in!

    print("\nTotal games appeared: ", str(len(pokeapi['game_indices'])))

    game_indices = 0

    for g in pokeapi['game_indices']:
        game_indices += 1

    print('Total games appeared: ', game_indices)

main()