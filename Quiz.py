def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def quiz(questions):
    score = 0
    total_questions = len(questions)

    for question, options, correct_answer in questions:
        display_question(question, options)
        user_answer = input("Enter your answer (1-4): ")

        try:
            user_answer_index = int(user_answer) - 1
            if user_answer_index < 0 or user_answer_index >= len(options):
                print("Invalid answer. Please enter a number between 1 and", len(options))
                continue

            if options[user_answer_index] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is:", correct_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
    if score <= 5:
        comment = "Get Good"
    elif score >= 6 and <= 10:
        comment = "Almost trash"
    elif score >= 11 and <= 15:
        comment = "Much better"
    elif score >= 16 and <= 20:
        comment = "Goat Status"

    print("\nQuiz completed!")
    print("Your score:", score, "out of", total_questions)
    print(comment)
    
    

if __name__ == "__main__":
    questions = [
        ("In which anime series does the character 'Naruto Uzumaki' appear?", ["One Piece", "Naruto", "Dragon Ball Z", "Bleach"], "Naruto"),
        ("Who is the protagonist of the anime 'Attack on Titan'?", ["Eren Yeager", "Goku", "Luffy", "Ichigo Kurosaki"], "Eren Yeager"),
        ("Which video game franchise features a character named 'Link'?", ["Final Fantasy", "The Legend of Zelda", "Assassin's Creed", "Super Mario"], "The Legend of Zelda"),
        ("What is the main objective in the game 'Minecraft'?", ["Survive", "Collect coins", "Defeat the final boss", "Build and explore"], "Build and explore"),
        ("Which of the following is NOT a starter Pokémon?", ["Charmander", "Squirtle", "Pikachu", "Bulbasaur"], "Pikachu"),
        ("What is the name of the main character in the video game 'Final Fantasy VII'?", ["Cloud Strife", "Sonic the Hedgehog", "Mario", "Master Chief"], "Cloud Strife"),
        ("What is the name of the Japanese dish consisting of thinly sliced raw fish?", ["Sushi", "Ramen", "Tempura", "Sashimi"], "Sashimi"),
        ("Which fruit is the main ingredient in guacamole?", ["Mango", "Banana", "Avocado", "Pineapple"], "Avocado"),
        ("What is the traditional Italian dessert made of ladyfingers, espresso, and mascarpone cheese?", ["Tiramisu", "Cannoli", "Gelato", "Panna cotta"], "Tiramisu"),
        ("Which type of pasta resembles small rice grains?", ["Fusilli", "Orzo", "Farfalle", "Rigatoni"], "Orzo"),
        ("What is the name of the popular Japanese dish made of thinly sliced beef and vegetables cooked in broth?", ["Yakitori", "Teriyaki", "Udon", "Sukiyaki"], "Sukiyaki"),
        ("In the anime 'One Piece', what is the name of Luffy's signature attack?", ["Gomu Gomu no Pistol", "Kamehameha", "Rasengan", "Bankai"], "Gomu Gomu no Pistol"),
        ("Which video game series features the character 'Mario'?", ["Call of Duty", "Halo", "Super Mario", "The Legend of Zelda"], "Super Mario"),
        ("What is the name of the food made by wrapping rice and seaweed around raw fish?", ["Sushi", "Ramen", "Tempura", "Sashimi"], "Sushi"),
        ("Which vegetable is the main ingredient in a traditional Greek moussaka?", ["Potato", "Eggplant", "Tomato", "Zucchini"], "Eggplant"),
        ("What is the name of the dish made of seasoned ground meat grilled on skewers?", ["Sushi", "Ramen", "Kebab", "Sashimi"], "Kebab"),
        ("In the anime 'Dragon Ball Z', who is Goku's best friend?", ["Vegeta", "Krillin", "Piccolo", "Bulma"], "Krillin"),
        ("Which video game franchise features characters named 'Scorpion' and 'Sub-Zero'?", ["Street Fighter", "Tekken", "Mortal Kombat", "Super Smash Bros"], "Mortal Kombat"),
        ("What is the name of the Italian dish consisting of thin sheets of pasta layered with sauce and cheese?", ["Lasagna", "Spaghetti", "Fettuccine Alfredo", "Carbonara"], "Lasagna"),
        ("Which of the following is NOT a character in the video game 'Overwatch'?", ["Tracer", "Widowmaker", "Zenyatta", "Scorpion"], "Scorpion"),
    ]

    quiz(questions)