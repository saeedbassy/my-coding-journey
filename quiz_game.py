keep_playing = "yes"
while keep_playing == "yes":
    score = 0
    def ask_question(question, correct_answer):
        user_answer = input(question)
        if user_answer == correct_answer:
            return True
        else:
            return False
    quiz = {"What is the capital of France? ": "Paris", "What is 5 + 3? ": "8", "What color do you get mixing blue and yellow? ": "green"}
    for question in quiz:
        result = input(question)
        if result == quiz[question]:
            score = score + 1
    print("You scored " + str(score) + " out of 3.")
    keep_playing = input("Play again? (yes/no): ")