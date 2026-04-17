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
    action = input("Execute command: ")

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
                    print(
                        "Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "2":
                if rock_stats["currency"] >= 20:
                    rock_stats["inventory"].append("Comrade's Pickaxe")
                    rock_stats["currency"] -= 20
                    print("You purchased a comrade's pickaxe.")
                else:
                    print(
                        "Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "3":
                if rock_stats["currency"] >= 20:
                    rock_stats["inventory"].append("Comrade's Fishing Rod")
                    rock_stats["currency"] -= 20
                    print("You purchased a comrade's fishing rod.")
                else:
                    print(
                        "Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "4":
                if rock_stats["currency"] >= 100:
                    rock_stats["inventory"].append("Mini Rimac Nevera")
                    rock_stats["currency"] -= 100
                    print("You purchased the Mini Rimac Nevera.")
                else:
                    print(
                        "Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "5":
                if rock_stats["currency"] >= 100:
                    rock_stats["inventory"].append("Mini Jeep Wrangler")
                    rock_stats["currency"] -= 100
                    print("You purchased the Mini Jeep Wrangler.")
                else:
                    print(
                        "Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "6":
                if rock_stats["currency"] >= 100:
                    rock_stats["inventory"].append("Mini Tesla Cybertruck")
                    rock_stats["currency"] -= 100
                    print("You purchased the Mini Tesla Cybertruck.")
                else:
                    print(
                        "Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "7":
                if rock_stats["currency"] >= 1000:
                    rock_stats["inventory"].append("Slightly Evil Robot")
                    rock_stats["currency"] -= 1000
                    print("You purchased the Slightly Evil Robot.")
                else:
                    print(
                        "Insufficient funds. Black Market strictly enforces capitalism.")
            elif buy_choice == "8":
                print("Returning to non-capitalist activities.")
                time.sleep(1)
            else:
                print("Invalid transaction. The Vendor glares at u.")
                time.sleep(1)

        case "4":
            print("\n=== THE EXPANDED WASTELAND ===")
            print("1. Deploy Shovel (The Kitsune's Scorched Earth)")
            print("2. Deploy Pickaxe (Yugoslavian Bunker Ruins)")
            print("3. Deploy Fishing Rod (Toxic Coolant Lake)")
            print("4. Scavenge (Abandoned Datacenter)")
            
            explore_choice = input("Select deployment protocol (1-4): ")

            mythic_roll = random.randint(1, 1000)
            
            mythic_ideologies = [
                "Tito's Golden Star (Communist)", 
                "Physical Bitcoin from 2008 (Capitalist)", 
                "The Golden Ballot (Liberalist)", 
                "RGB Molotov Cocktail (Anarchist)"
            ]

            if mythic_roll == 1000:
                found_mythic = random.choice(mythic_ideologies)
                print(f"\n[!!!] CRITICAL GEOLOGICAL ANOMALY [!!!]")
                time.sleep(2)
                print(f"The holy music suddenly stops. It's dead silent, except your heartbeat.")
                print(f"NO WAY! Your rock unearthed {found_mythic}!")
                rock_stats["inventory"].append(found_mythic)
                # continue command goes back to main menu. YOu already found the mythic item :p
                time.sleep(3)
                continue 
            
            
            if explore_choice == "1":
                if "Comrade's Shovel" in rock_stats["inventory"]:
                    print(f"\nDeploying {rock_stats['name']} to the Kitsune's Scorched Earth...")
                    time.sleep(1)
                    
                    b1_common = ["burnt leaves", "rusty cans", "shattered glass", "mysterious bones"]
                    b1_uncommon = ["ice fox plushie", "soft pillows", "cherry blossom petals"]
                    b1_rare = ["ancient Kitsune mask", "pure energy crystal", "perfectly preserved tail"]
                    
                    loot_roll = random.randint(1, 100)
                    if loot_roll <= 65:
                        item = random.choice(b1_common)
                        print(f"COMMON DROP: You dug up: {item}!")
                    elif loot_roll <= 90:
                        item = random.choice(b1_uncommon)
                        print(f"UNCOMMON DROP: You dug up: {item}!")
                    else:
                        item = random.choice(b1_rare)
                        print(f"RARE DROP: You dug up: {item}!")
                        
                    rock_stats["inventory"].append(item)
                else:
                    print("Access denied. You lack the necessary earth-moving equipment.")
                    time.sleep(1)
            
            elif explore_choice == "2":
                if "Comrade's Pickaxe" in rock_stats["inventory"]:
                    print(f"\nDeploying {rock_stats['name']} to the Yugoslavian Bunker Ruins...")
                    time.sleep(1)
                    
                    b2_common = ["rusty tank bolt", "empty rations wrapper", "spent bullet casing"]
                    b2_uncommon = ["Ivan's left boot", "intact M70 magazine", "abandoned Yugo hubcap"]
                    b2_rare = ["working Geiger counter", "unexploded ordnance", "classified intel folder"]
                    
                    loot_roll = random.randint(1, 100)
                    if loot_roll <= 65:
                        item = random.choice(b2_common)
                        print(f"COMMON DROP: You mined: {item}!")
                    elif loot_roll <= 90:
                        item = random.choice(b2_uncommon)
                        print(f"UNCOMMON DROP: You mined: {item}!")
                    else:
                        item = random.choice(b2_rare)
                        print(f"RARE DROP: You mined: {item}!")
                        
                    rock_stats["inventory"].append(item)
                else:
                    print("Access denied. A pickaxe is required to breach the blast doors.")
                    time.sleep(1)
                    
            elif explore_choice == "3":
                if "Comrade's Fishing Rod" in rock_stats["inventory"]:
                    print(f"\nCasting line into the Toxic Coolant Lake...")
                    time.sleep(1)
                    # to lazy for the loot hehe
                    print("You need to code the fish, comrade!")
                else:
                    print("Access denied. You need a rod to fish in the coolant.")
                    time.sleep(1)

            elif explore_choice == "4":
                print(f"\nScavenging the Abandoned Datacenter...")
                time.sleep(1)
                # my dumbass gotta put loot here too
                print("You need to code the cyber-loot, comrade!")

            else:
                print("Invalid coordinates. The rock remains stationary.")
                time.sleep(1)

        case "7":
            print("Shutting down the matrix. Goodbye, comrade.")
            break

        case _:
            print("Invalid input. The geological entity judges you silently.")
            time.sleep(1)
