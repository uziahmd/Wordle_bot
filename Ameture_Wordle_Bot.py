import csv

class Wordle:
    def __init__(self, word, score, variety):
        self.word = word
        self.score = score
        self.variety = variety

def get_result(guess, answer):
  result = ""
  for pos, ch_guess, ch_answer in zip(range(5), guess, answer):
    if ch_guess == ch_answer:
      result += "."
    elif ch_guess not in answer:
      result += "_"
    else:
      result += "?"
  return result
  
def adjust(words, guess, response):
  return [word for word in words if get_result(guess, word) == response]

def scoring(words):
    pool = []

    alpha = [0]*26
    
    for w in words:
        for x in range(5):
            alpha[ord(w[x])-97]+=1

    for w in words:
        score = alpha[ord(w[0]) -97] + alpha[ord(w[1])-97] + alpha[ord(w[2]) -97] + alpha[ord(w[3])-97] + alpha[ord(w[4])-97]
        variety = len(set(w))
        temp = Wordle(w, score, variety)
        pool.append(temp)
    pool.sort(key=lambda x: (x.score), reverse= True)

    return pool

def main():
    words = []
    with open("words.csv") as file:
        reader = csv.reader(file, delimiter=',')
        for word in reader:
            words.append(word[0])

    pool = scoring(words)
    
    turn = 1
    win = False
    
    while (turn <= 6 and win == False):
        print("This is our guess")
        num = 0
        
        if turn <= 3 and pool[num].variety != 5:
            while pool[num].variety != 5:
                num += 1 
        print(pool[num].word)
        print("Enter the response (_/./?) ")
        response = input()
        if response == ".....":
            print("Victory")
            win = True
        else:
            words = adjust(words, pool[num].word, response)
            pool = scoring(words)
            turn += 1
    
if __name__=="__main__":
    main()