import random
import time

rock_stats = {
    "name": input("Give your geological entity a name: "),
    "life": 1000,
    "mood": 0,
    "has_soul": False,
    "ideology": "neutral",
    "currency": 100,
    "inventory": [],
    "location": "Base" 
}
print(rock_stats)

while True:
    print("\n=== THE GEOLOGICAL CONTROL PANEL ===")
    print("What do you wanna do with da rock?")
    print("1. Check stats")
    print("2. Pet rock")
    print("3. acces black market (shop)")
    print("4. Explore ze wasteland")
    print("5. Battle Mode (+ end boss)")
    print("6. Access inventory")
    print("7. power down (exit)")
    print("00. Admin command (cheat codes)")
    action = input("Execute command (1-6): ")
    
    match action:
        case "1":
            print("Accessing stat matrix...")
            time.sleep(1)
            print(rock_stats)
            
        case "2":
            print("\nInitializing petting protocol...")
            time.sleep(1)
            pet_roll = random.randint(0, 100)

            if pet_roll > 90:
                rock_stats["life"] += 60
                rock_stats["mood"] += 5
                print("CRITICAL PET! The rock absorbs your kinetic energy.")
                print("Life increased by 60. Mood increased by 5.")

            elif pet_roll > 70:
                rock_stats["life"] += 30
                rock_stats["mood"] += 2
                print("Great Pet! The rock absorbs your mood.")
                print("Life increased by 30. Mood increased by 2.")

            else:
                print("The rock breaks your hand. Now you can't pet it. RIP.")
                
        case "3":
            print("\n=== THE BLACK MARKET ===")
            print("Always up to no good, comrade.")
            time.sleep(1)
            print(f"Available funds: {rock_stats['currency']} pebbles.")
            print("1. A comrade's shovel - 20 pebbles.")
            print("2. A comrade's pickaxe - 20 pebbles.")
            print("3. A comrade's fishing rod - 20 pebbles.")
            print("4. mini rimac nevera (speed trait) - 100 pebbles.")
            print("5. mini jeep wrangler (defense trait) - 100 pebbles.")
            print("6. mini tesla cybertruck (attack trait) - 100 pebbles.")
            print("7. Slightly evil robot (?) - 1000 pebbles.")
            print("8. Return to non-capitalist activities.")
            buy_choice = input("Pick your contraband (1 - 8): ")

            if buy_choice == "1":
                if rock_stats["currency"] >= 20:
                    rock_stats["inventory"].append("Comrade's Shovel")
                    rock_stats["currency"] -= 20
                    print("You purchased a comrade's shovel.")
                else:
                    print("Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "2":
                if rock_stats["currency"] >= 20:
                    rock_stats["inventory"].append("Comrade's Pickaxe")
                    rock_stats["currency"] -= 20
                    print("You purchased a comrade's pickaxe.")
                else:
                    print("Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "3":
                if rock_stats["currency"] >= 20:
                    rock_stats["inventory"].append("Comrade's Fishing Rod")
                    rock_stats["currency"] -= 20
                    print("You purchased a comrade's fishing rod.")
                else:
                    print("Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "4":
                if rock_stats["currency"] >= 100:
                    rock_stats["inventory"].append("Mini Rimac Nevera")
                    rock_stats["currency"] -= 100
                    print("You purchased the Mini Rimac Nevera.")
                else:
                    print("Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "5":
                if rock_stats["currency"] >= 100:
                    rock_stats["inventory"].append("Mini Jeep Wrangler")
                    rock_stats["currency"] -= 100
                    print("You purchased the Mini Jeep Wrangler.")
                else:
                    print("Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "6":
                if rock_stats["currency"] >= 100:
                    rock_stats["inventory"].append("Mini Tesla Cybertruck")
                    rock_stats["currency"] -= 100
                    print("You purchased the Mini Tesla Cybertruck.")
                else:
                    print("Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "7":
                if rock_stats["currency"] >= 1000:
                    rock_stats["inventory"].append("Slightly Evil Robot")
                    rock_stats["currency"] -= 1000
                    print("You purchased the Slightly Evil Robot.")
                else:
                    print("Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "8":
                print("Returning to non-capitalist activities.")
                time.sleep(1)
            else:
                print("Invalid transaction. The Vendor glares at u.")
                time.sleep(1)
                
        case "4":
            print("\n===EXPLORATION MODE ACTIVATED===")
            print("1. Deploy Shovel (scorched earth)")
            print("2. Deploy Pickaxe (mineshaft)")
            
            common_loot = ["BMW hub caps", "glitter bottles", "brick pillows", "rusty cans", "tiny phone fragments", "old circuits", "shattered glass", "cat hair", "mysterious bones", "empty sour patch wrappers", "wolf fangs"]
            uncommon_loot = ["ancient artifact", "Ivan's boots", "vintage frame", "soft pillows", "broken laptop", "ice fox plushie", "bob marley vinyl", "Bubble tea pearls", "golden logs"]
            rare_loot = ["shiny chicken nuggets", "cocaine bricks", "shredded toilet paper", "Her Majesty's fake crown", "ONE single grain of sand from the Sahara", "a mini tesla cyberduck", "babushka's lost sock", "grey goo", "cherry blossom"]

            explore_choice = input("Select deployment protocol (1-2): ")

            if explore_choice == "1":
                if "Comrade's Shovel" in rock_stats["inventory"]:
                    print(f"Deploying {rock_stats['name']} to the kitsune's scorched earth...")
                    time.sleep(1)
                    
                    loot_roll = random.randint(1, 100)
                    
                    if loot_roll <= 65:
                        found_item = random.choice(common_loot)
                        print(f"COMMON DROP: You dug up: {found_item}!")
                        rock_stats["inventory"].append(found_item)
                        
                    elif loot_roll <= 90:
                        found_item = random.choice(uncommon_loot)
                        print(f"UNCOMMON DROP: You dug up: {found_item}!")
                        rock_stats["inventory"].append(found_item)
                        
                    else:
                        found_item = random.choice(rare_loot)
                        print(f"RARE DROP: You dug up: {found_item}!")
                        rock_stats["inventory"].append(found_item)
                else:
                    print("Habibi, get ur broke ass a shovel first.")
                    time.sleep(1)
                    
            elif explore_choice == "2":
                print("Mineshaft protocol not yet coded. Retreating.")
                time.sleep(1)
                
            else:
                print("Invalid exploration command. The rock just sits there.")
                time.sleep(1)
                
        case "7":
            print("Shutting down the matrix. Goodbye, comrade.")
            break
            
        case _:
            print("Invalid input. The geological entity judges you silently.")
            time.sleep(1)
            
