# Entry point to the app.

# MVP:
# Using JSON as a backend system.
# Basically a JSON parser for HTTP requests.
# Built by coolerputt btw, cos I've seen JSON servers as an idea some JS devs cooked up but mine is different.


# Obviously I would be suing the default json parser lol.
import json

# Just testing out if the file runs lol. - ok it does let's comment out the check.
# print(f"Hello World!")

# Let's start from reading and writing from a simple JSON file.

# Holding my demo JSON file in here.
JSON_FILE = "./data.json"

json_object = None
json_objects = []
JSON_DATA = {
        "name":"Some Rando person lol.",
        "bio":"Surving is winning franklin."
    }

# I'm using a tutorial to learn JSON parsing btw.
# with open(JSON_FILE,'r') as json_file:
#     data = json_file.read()

#     # parsing
#     json_object = json.loads(data)

# for x in json_object:
#     print(json_object[x]["name"])
#     if type(json_object) == dict:
#         print("It was a dict all along.")
#     json_objects += json_object[x]

# Now let's comment this out and try writing to file. Overall JSON parsing with python is weird. I would obvoiusly prefer nlohmann cpp JSON parser if not the fact that I have to pay up to a Tesla car to keep the server running lol.

# with open(JSON_FILE,'a') as json_file:
with open(JSON_FILE,'w') as json_file:
    

    # Wonderful parsing. honestly, I thought reading and writing would be like an async function but I would love to do more research that anywsy...Would drop codes soon to setup my Rust game engine lol.
    # json.dumps(JSON_DATA)

    # Now left the 'dumps' and sidetrack to check how to setup my Rust game proj lol.I feel I keep leaving unneccsary comments.
    # Turns out the dumb in me actually thought 'dumps' was for writing in files without overwriting the current JSON data.
    json.dump(JSON_DATA,json_file)
    # Now I'm on a random site to learn how I can write to a JSON file without overwriting any existing data.
    # Me remembering Godot launched the new Rust supported update.
    # Me actually seeing SDL2 with Rust, I am literally laughing rn.
    # Probably stick with my SFML cpp library system, but I want to apply my Rust knowlegde on something, guess I would hold unto full stack web dev with prob Actix framework.
    # This stuff has been loading for a long time lol, might as well commit and close as progress for today.
    # Are you fr? I have been waiting for a long time only to find out that the docs is an audio note lol.
    # Imagine me finally getting info to read from the json file, appending manually and then writing lol.
    # Turns out there is an append mode for opening files for parsing. 
    # I just tried it out and it works.