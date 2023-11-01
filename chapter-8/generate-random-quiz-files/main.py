import random
import os
from dict import capitals

def generate_random_quiz_files():
    # Create a directory to store quiz and answer key files
    if not os.path.exists('quizzes'):
        os.mkdir('quizzes/')
    if not os.path.exists('quizzes/questions'):
        os.makedirs('quizzes/questions')
    if not os.path.exists('quizzes/answers'):
        os.makedirs('quizzes/answers')
        
    # Generate 35 quiz files.
    for quizNum in range(35):
        # Create the quiz and answer key files.
        question_filename = os.path.join('quizzes', 'questions', f'quiz_{quizNum + 1}.txt')
        answer_filename = os.path.join('quizzes', 'answers', f'quiz_{quizNum + 1}_answer.txt')
        # print(question_file)
        # print(answer_file)
        
        with open(question_filename, 'w', encoding='utf-8') as question_file, \
            open(answer_filename, 'w', encoding='utf-8') as answer_file:
                # write out the header for the quiz
                question_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
                question_file.write(f'{" " * 20}State Capitals Quiz - Student {quizNum + 1}\n\n')
                answer_file.write(f'US State Capitals Answers - Student {quizNum + 1}\n\n')
                
                # Shuffle the order of the states
                states = list(capitals.keys())
                # print(states)
                random.shuffle(states)  # it does not return a new list instead it changes d original list
                # print(states)

                # Loop through all 50 states, making a question for each
                for question_num in range(50):  # it generates 1750 questions
                    state = states[question_num]  # get questions 1-50 from the list
                    correct_answer = capitals[state]  # get the capital of the state from the capitals dictionary
                    # print(state)
                    # print(correct_answer)
                    
                    # Create a list of answer options
                    answer_options = list(capitals.values())
                    del answer_options[answer_options.index(correct_answer)]  # delete the correct answer from d anaswer options
                    wrong_answers = random.sample(answer_options, 3)
                    answer_options = wrong_answers + [correct_answer]  # conactenate list with list
                    # print(answer_options)
                    random.shuffle(answer_options)
                    # print(answer_options)
                    
                    # Write the question and answer options to the quiz file
                    question_file.write(f'{question_num + 1}. What is the capital of {state}?\n')
                    for index, option in enumerate(answer_options):
                        question_file.write(f'{"ABCD"[index]}. {option}\n')
                    question_file.write('\n')
                    
                    # Write the correct answer to the answer key file
                    answer_file.write(f'{question_num + 1}. {"ABCD"[answer_options.index(correct_answer)]}\n')

if __name__ == '__main__':
    generate_random_quiz_files()
    
# TODO: Implement using json
    
