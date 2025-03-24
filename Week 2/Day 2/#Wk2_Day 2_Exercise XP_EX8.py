#Exercise XP
#Week 2_Ex8

data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def take_quiz(data):
    correct_count = 0
    wrong_count = 0
    wrong_answers = []

    for item in data:
        user_answer = input(f"{item['question']}").strip()
        
        if user_answer.lower() == item['answer'].lower():
            correct_count += 1
        else:
            wrong_count += 1
            wrong_answers.append({
                "question": item['question'],
                "user_answer": user_answer,
                "correct_answer": item['answer']
            })
    return correct_count, wrong_count, wrong_answers

def show_results(correct_count, wrong_count, wrong_answers):
    print("\nQuiz Results:")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {wrong_count}")

    if wrong_answers:
        print("\nYou got the following questions wrong:")
        for item in wrong_answers:
            print(f"- Question: {item['question']}")
            print(f"  Your answer: {item['user_answer']}")
            print(f"  Correct answer: {item['correct_answer']}")
    
    if wrong_count > 3:
        print("\nYou got more than 3 questions wrong. Consider playing again to improve your score!")

def main():
    print("Welcome to the Star Wars Quiz!")
    correct_count, wrong_count, wrong_answers = take_quiz(data)
    show_results(correct_count, wrong_count, wrong_answers)

main()
