def main():
    # def print_square(square):
    #     for i in range(square):
    #         print("-"*square)
    # print_square(4)
    def questions_answer():
        questions_list = ["What is the sum of 20+15","What is python","What is 2x30"]
        answers_list = [35,"snake",60]
        options_list1= [35,45,68]
        options_list2= ["Bird","Fish","Snake"]
        options_list3= [35,60,68]
        return questions_list, answers_list, options_list1, options_list2, options_list3
    def ask_questions():
        score_no =[]
        questions_list, answers_list, options_list1, options_list2, options_list3 = questions_answer()
        print(f"Q1.,{questions_list[0]}")
        for i in range(len(options_list1)):
            print(f"Options{i+1,{options_list1[i]}}")
            ans1 =int(input("Enter the option"))
            if ans1 == answers_list[0]:
                print("Correct Answer! Score +1 ")
                score_no.append(1)
        print(f"Q2.,{questions_list[1]}")
        for i in range(len(options_list2)):
            print(f"Options{i+1,{options_list2[i]}}")
            ans2 = input("Enter the option")
            if ans2.lower() == answers_list[1]:
                print("Correct Answer! Score +1 ")
                score_no.append(1)
        print(f"Q3,{questions_list[2]}")
        for i in range(len(options_list3)):
            print(f"Options{i+1,{options_list3[i]}}")
            ans3 =int(input("Enter the option"))
            if ans3 == answers_list[2]:
                print("Correct Answer! Score +1 ")
                score_no.append(1)
        print(f"Your score is {sum(score_no)}/3")
    questions_answer()
    ask_questions()
main()