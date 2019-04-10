import re
def parser(file_name):
    input ={}
    array_of_questions = []
    
    f = open(file_name, "r")
    number_of_questions = int(f.readline())
    input["TotalQuestions"] = number_of_questions
    i = 0
    while (i < number_of_questions):
        line = f.readline().rstrip().split(',')
        question = {}
        question["id"] = line[0]
        question["difficulty"] = line[1]
        question["marks"] = line[2]
        array_of_questions.append(question)
        i = i+1
    input["questions"] = array_of_questions
    furtherdetails = f.readline().rstrip()
    get_numbers = re.findall(r'\d+', furtherdetails)
    input["total_marks"] = get_numbers[0]
    input["easy_percentage"] = get_numbers[1]
    input["medium_percentage"] = get_numbers[2]
    input["hard_percentage"] = get_numbers[3]
    return input
    f.close()
