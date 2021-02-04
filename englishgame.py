# import sys
# print(sys.version)
# print(sys.path)



import re
import random
import numpy as np


source = 'englishwords.txt'

def create_words_dict(source):
    with open(source) as f: 
        data = f.read()
    print(data)

    englishwords = re.findall('[a-z]+', data)

    # print(englishwords)

    ja = re.findall('\s.*\n', data)

    meanings = []
    for word in ja:
        # print(word)
        m = re.sub('\t|\n', '', word)
        meanings.append(m)

    words_dict = dict(zip(englishwords, meanings))
    return englishwords, meanings, word_dict
for key, value in words_dict.items():
    print(key, value)

n_tests = 50
n_questions = 50
if  __name__ == '__main__':

    englishwords, meanings, words_dict = create_words_dict(source)

    for test_num in range(n_tests):
        with open('英単語テスト_{:02d}.txt'.format(test_num + 1), 'w') as f:
            f.write('出席番号:\n'
                    '名前:\n\n'
                    '第{}回英単語テスト\n\n'.format(test_num + 1))
        
            random_index = np.random.randint(low=0, high=len(englishwords), size=n_questions)
            for question_num in range(n_questions):
                question_word = englishwords[random_index[question_num]]
                correct_answer = words_dict[question_word]
            

                meanings_copy = meanings.copy()
                meanings_copy.remove(correct_answer)
                wrong_answers = random.sample(meanings_copy, 3)

                answer_options = [correct_answer] + wrong_answers

                random.shuffle(answer_options)

                f.write('問{}. {}\n\n'.format(question_num + 1, question_word))

                for i in range(4):
                    f.write('{}. {}\n'.format(i + 1, answer_options[i]))
                f.write('\n\n')    

print("git hello")
