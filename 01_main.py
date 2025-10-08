import random

def get_int(prompt, min_val = 1, default = None):
    while True:
        s = input(prompt).strip()
        if s == "" and default is not None:
            return default
        try:
            n = int(s)
            if n < min_val:
                print(f"Please enter an integer >= {min_val}.")
                continue
            return n
        except ValueError:
            print("Please enter a valid integer.")

def roll_die(sides):
    return random.randint(1, sides)

def roll_dice(num, sides):
    return [roll_die(sides) for _ in range(num)]

def main():
    print("=== Dice Roller Simulator ===")
    while True:
        sides = get_int("Number of sides per die (default 6): ", min_val = 2, default = 6)
        num = get_int("How man dice to roll (default 1): ", min_val = 1, default = 1)
        results = roll_dice(num, sides)
        print("\nRolls:", ", ".join(str(r) for r in results))
        if num > 1:
            print("Total: ", sum(results))
            counts = {}
            for r in results:
                counts[r] = counts.get(r, 0) + 1
            print("Counts:", ", ".join(f"{face} X {count}" for face, count in sorted(counts.items())))
        again = input("\nRolls again ? (Y/n): ").strip().lower()
        if again == 'n':
            print("GoodBye!")
            break

if __name__ ==  "__main__":
    main()