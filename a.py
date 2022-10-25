#! python3
"""
 Giả sử bạn là một giáo viên địa lý với 35 sinh viên trong lớp của mình và bạn muốn đưa ra một câu đố vui về các thủ phủ của tiểu bang Hoa Kỳ. Chao ôi, lớp của bạn có một vài quả trứng xấu trong đó, và bạn không thể tin tưởng học sinh không gian lận. Bạn muốn ngẫu nhiên hóathứ tự câu hỏi sao cho mỗi câu hỏi là duy nhất, khiến cho bất kỳ ai cũng không thể bỏ qua câu trả lời của bất kỳ ai khác. Tất nhiên, làm điều này bằng tay sẽ là một việc dài và nhàm chán. May mắn thay, bạn biết một số Python.

Đây là những gì chương trình thực hiện:

Tạo 35 bài kiểm tra cho 35 thí sinh
Tạo 50 câu hỏi trắc nghiệm cho mỗi bài kiểm tra, theo thứ tự ngẫu nhiên
Cung cấp câu trả lời đúng và ba câu trả lời sai ngẫu nhiên cho mỗi câu hỏi, theo thứ tự ngẫu nhiên
Viết các câu đố thành 35 tệp văn bản
Ghi các phím trả lời vào 35 tệp văn bản
Điều này có nghĩa là mã sẽ cần thực hiện những việc sau:

Lưu trữ các tiểu bang và thủ đô của chúng trong từ điển
Gọi open () , write () và close () cho các tệp văn bản chính của bài kiểm tra và câu trả lời
Sử dụng random.shuffle () để sắp xếp thứ tự của các câu hỏi và các tùy chọn trắc nghiệm một cách ngẫu nhiên
"""
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
capital = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


import random, os, time
#tạo 35 file lưu 35 mã đề khác nhau
for i in range(1,36):
    questionfile = open(f"question{i}", "w", encoding="utf-8")
    answerfile = open(f"answer{i}", "w", encoding="utf-8")
    questionfile.write("Họ và tên:\nLớp:\nNgày:\nTrường:\n")
    questionfile.write("Bạn có 15 phút để hoàn thành bài thi của mình.")
    questionfile.write('\n\n')
    question = list(capital.keys())
    random.shuffle(question)
# Tạo 4 lựa chọn cho mỗi câu hỏi.
    for x in range(50):

        #answer = list(capital.values())
        #correctanswer = capital[question[x]]
        #del answer[answer.index(correctanswer)]

        correctanswer= capital[question[i]]
        #lấy danh sách toàn bộ đáp án.
        answer = list(capital.values())
        # xóa câu trả lời đúng để tránh xuaasrt hiện 2 đáp án giống nhau.
        del answer[answer.index(correctanswer)]
        wronganswer =random.sample(answer, 3)
        optionsanswer = wronganswer + [correctanswer]
        random.shuffle(optionsanswer)
        questionfile.write(f"Câu hỏi {x+1}. Thủ đô của {question[x]} là gì?\n")
        for y in range(4):
            questionfile.write(f"\t{'ABCD'[y]}.{optionsanswer[y]}\n")
            answerfile.write(f'Đáp án câu {x} là: {optionsanswer[optionsanswer.index(correctanswer)]}\n')
    questionfile.write("Nộp bài để kết thúc phần thi!")
    questionfile{i}.close()
    answerfile{i}.close()