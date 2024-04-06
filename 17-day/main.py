

# class User:
#     def __init__(self,user_id,user_name):
#         self.id = user_id
#         self.user_name = user_name
#         self.followers = 0
#         self.following = 0
#         print("new user is being created")
        
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1

        

# user_1 = User('001','navjot')
# user_2 = User('002','amanjot')
# print(user_1.user_name)

# user_1.follow(user=user_2)


# print(user_1.followers)


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    
    new_question = Question(question_text,question_answer )
    question_bank.append(new_question)
    
    
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

quiz.next_question()