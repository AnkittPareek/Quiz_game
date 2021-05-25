class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def start_quiz(self):
        self.question_number += 0
        right = 0
        wrong = 0
        while self.question_number < len(self.question_list):
            answer = input(f'Q.{self.question_number + 1}: {self.question_list[self.question_number].text}'
                           f' (True/False)? : ').lower()
            if answer == self.question_list[self.question_number].answer.lower():
                print("Well Done")
                right += 1
            else:
                print("Sorry! this is Wrong.")
                wrong += 1
            self.question_number += 1
        print(f"\n\nThanks for taking the quiz, You guessed {right} Right and {wrong} Wrong answers.")
