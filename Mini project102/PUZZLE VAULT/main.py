print("="*45)
print("      🐍 PYTHON CODE BREAKER 🐍")
print("="*45)

print()
print("Welcome to Python Code Breaker")
print("Solve the Puzzles using python code. ")


print()
print("You have 8 puzzlse to solve. ")
print("Good luck!")

print()
print("="*45)

score = 0

#Puzzle 1: The Hidden Message
print()
print("=" * 45)
print("🔐 PUZZLE 1 — THE HIDDEN MESSAGE")
print("=" * 45)

text = "I LOVE PYTHON"

print()
print("The secret word is :", text)
print()
print("Extract the word : 'LOVE' ")
print("Write Python code to extract it")

answer = input(">>> ")
print ("Your answer : ")
print(answer)


correct_answer = 'text[2:6]'

if answer.strip() == correct_answer:
    print("✅ Correct!")
    score += 100
else:
    print("❌ Wrong!")


#Puzzle 2: The Corrupted Message
print()
print("=" * 45)
print("🔐 PUZZLE 2 — THE CORRUPTED MESSAGE")
print("=" * 45)

text1 ="      Artificial#Intelligence is the field --- of the future@"

print()
print("The corrupted message is:")
print(text1)


print()
print("Clean the message")
print("Expected result: Artificial Intelligence is the field of the future.")
print("Write python code to clean it.")

answer = input(">>> ")
print ("Your answer : ")
print(answer)


correct_answer = 'text1.strip().replace("#", " ").replace("--- ", "").replace("@", ".")'

if answer.strip() == correct_answer:
    print("✅ Correct!")
    score += 100
else:
    print("❌ Wrong!")


#Puzzle 3: The Secret Word
print()
print("=" * 45)
print("🔐 PUZZLE 3 — THE SECRET WORD")
print("=" * 45)

words = ["cloud", "python", "oracle", "agent", "database"]

print()
print("The available word are : ")
print(words)

print()
print("Find the word that contains 'ora' ")
print("Find the word that contains the clue.")
print("Then write Python code to find its position. ")

answer = input(">>> ")
print ("Your answer : ")
print(answer)

correct_answer = 'words[2].find("ora")'

if answer.strip() == correct_answer:
    print("✅ Correct!")
    score += 100
else:
    print("❌ Wrong!")


#Puzzle 4: The Number Laboratory
print()
print("=" * 45)
print("🔐 PUZZLE 4 — THE NUMBER LABORATORY")
print("=" * 45)

numbers = [12 , 54 , 60 , 7 , 33]

print()
print("The numbers are : ")
print(numbers)

print()
print("Find the smallest number , largest number , and total.")
print("Write python code to find them")

answer = input(">>> ")
print ("Your answer : ")
print(answer)

correct_answer = "[min(numbers), max(numbers), sum(numbers)]"

if answer.strip() == correct_answer:
    print("✅ Correct!")
    score += 100
else:
    print("❌ Wrong!")


#Puzzle 5: The Password Matrix
print()
print("=" * 45)
print("🔐 PUZZLE 5 — The Password Matrix")
print("=" * 45)

grid = [
    ["X","X","7","X"],
    ["X","3","X","X"],
    ["9","X","X","X"],
    ["X","X","X","5"],

]


print()
print("A four-digit password is hidden in the matrix.")
print("Find the four digits and build the password.")
print("⚠️ The digits are stored in password order.")
print("Write ONE Python expression that returns the password.")

answer = input(">>> ")
print ("Your answer : ")
print(answer)


correct_answer = '"".join([grid[1][1], grid[3][3], grid[0][2], grid[2][0]])'

if answer.strip() == correct_answer:
    print("✅ Correct!")
    score += 100
else:
    print("❌ Wrong!")


#Puzzle 6: The Function Lock
print()
print("=" * 45)
print("🔐 PUZZLE 6 — THE FUNCTION LOCK")
print("=" * 45)

def create_code(name,year="2026") :
    return name + "-" + year


print()
print("Enter your name : ")
name = input(">>> ")

print()
print("Enter the year : ")
year = input(">>> ")

print()
print("Now use the function to create your code.")
print("⚠️ Use Keyword Arguments.")

answer = input(">>> ")
print()
print("Your answer:")
print(answer)

result = create_code(name=name , year=year)

if answer.strip() == "create_code(name=name, year=year)":
    print("✅ Correct!")
    print("Your access code:", result)
    score += 100
else:
    print("❌ Wrong!")


#Puzzle 7 : The Key Ring


print()
print("=" * 45)
print("🔑 PUZZLE 7 — THE KEY RING")
print("=" * 45)

def unlock(*keys):
    print("Keys received:")
    print(keys)

keys = ("RED", "BLUE", "GOLD")

print()
print("The vault has three keys:")
print(keys)

print()
print("Send all three keys to the function.")
print("⚠️ Use Argument Unpacking , Function name: `keys`")

answer = input(">>> ")
print()
print("Your answer:")
print(answer)

correct_answer = "unlock(*keys)"

if answer.strip() == correct_answer:
    print("✅ Correct!")
    unlock(*keys)
    score += 100
else:
    print("❌ Wrong!")


# Puzzle 8: The Master Key

print()
print("=" * 45)
print("🗝️ PUZZLE 8 — THE MASTER KEY")
print("=" * 45)

def open_vault(section, level, key):
    return section + "-" + level + "-" + key

vault = {
    "section": "OMEGA",
    "level": "7",
    "key": "GOLD"
}

print()
print("The vault data is:")
print(vault)

print()
print("Use Dictionary Unpacking to open the vault .")
print("⚠️ Write Python code that generates the master key  , Function name: `open_vault`.")

answer = input(">>> ")
print()
print("Your answer:")
print(answer)

result = open_vault(**vault)

if answer.strip() == "open_vault(**vault)":
    print("✅ Correct!")
    print("🔓 Master key:", result)
    score += 100
else:
    print("❌ Wrong!")



#Final Score

print()
print("=" * 45)
print("🏆 CONGRATULATIONS!")
print("=" * 45)

print()
print("You completed all the puzzles!")
print("Your final score is:", score, "/ 800")

if score == 800:
    print("🔥 Perfect score! You broke every code!")
elif score >= 500:
    print("👏 Great job! You're becoming a Python Code Breaker!")
else:
    print("💪 Good effort! Keep practicing Python!")

print()
print("=" * 45)