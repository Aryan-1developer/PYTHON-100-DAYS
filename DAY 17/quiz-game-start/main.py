from question_model import Question
from data import question_data
from quiz_brain import QuizBrain 

questions_bank = []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

print(questions_bank[0].text)
quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()