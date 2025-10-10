# Write Code Below This Line 👇

print("-------------------------------------------------------")
print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")
print("-------------------------------------------------------")

print("-- Welcome to the Treasure Island --")
print("Your mission is to find the treasure 💰")

death = 0  # Keeps track of whether player died

# ---------- LEVEL 1 ----------
direction = input('Choose a direction — "Left" or "Right": ').strip().lower()

if direction == "left":
    print("You took the left path. It’s dark and spooky... 🕯️")
elif direction == "right":
    print("You fell into a pit full of spikes! ☠️")
    print("GAME OVER!!")
    death += 1
else:
    print("Restart the game and enter a valid direction (Left/Right).")
    death += 1


# ---------- LEVEL 2 ----------
if death == 0:
    travel = input('Do you want to "Swim" across or "Wait" for a boat? ').strip().lower()

    if travel == "wait":
        print("You waited patiently, and a kind old fisherman gave you a lift 🚤")
    elif travel == "swim":
        print("Congo big brain! You got eaten by crocodiles 🐊💀")
        print("GAME OVER!!")
        death += 1
    else:
        print('Restart the game and enter either "Swim" or "Wait".')
        death += 1


# ---------- LEVEL 3 ----------
if death == 0:
    door = input('You reach three doors: "Red", "Blue", or "Green". Which do you choose? ').strip().lower()

    if door == "red":
        print("🔥 The room bursts into flames! You are toast!")
        print("GAME OVER!!")

    elif door == "blue":
        print("💀 It’s my favourite color but sike—it’s not correct either!")
        print("Don’t you know green = money, you small brain?!")
        print("GAME OVER!!")

    elif door == "green":
        print("💎 You found the treasure room!")
        print("But plot twist: we donated all your treasure 💰")
        print("The real treasure was kindness all along 💚")
        print("🏆 GAME COMPLETED!")

    else:
        print("🤦‍♂️ You were supposed to choose Red, Blue, or Green. Try again, bozo.")


print("\nThanks for playing Treasure Island Adventure! 🏴‍☠️")






