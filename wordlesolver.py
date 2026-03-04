import json
import math
from tqdm import tqdm


with open('targets_5_letter.json','r') as file:
    answers = json.load(file)

with open('dictionary_5_letter.json','r') as file2:
    guesses = json.load(file2)

def identify_color(G,A,i):
    
    if(G[i]==A[i]):
        A[i]='0'
        G[i]=''
        return 'g'
    else:
        for char in range(len(G)):
            if(char==i):
                continue
            elif(G[i]==A[char]):
                A[char]='0'
                G[i]=''
                return 'y'
    
    return 'r'



def feedback(g,a):
    G=list(g)
    A=list(a)

    fdbck=""
    for char in range(len(G)):
        fdbck+=identify_color(G,A,char)

    return fdbck
    

def score_guess(guess, possible_answers):
    patterns = {}                                 
    for answer in possible_answers:
        pat = feedback(guess, answer)
        patterns[pat] = patterns.get(pat, 0) + 1

    total = len(possible_answers)
    entropy = 0
    for count in patterns.values():
        p = count / total
        entropy -= p * math.log2(p)

    return entropy

gss = list(guesses)
s = list(answers)
for turn in range(1, 7):  # max 6 turns
    
    if len(s) == 1:
        print(f"Solved on turn {turn}")
        print(f"The solution is {s[0]}")
        break
    else:
        print(f"\n===== Turn {turn} =====")
        print("Remaining possible answers:", len(s))


    ### the case if no possible answer remains len(s) == 0 ERROR HE GAVE US WRONG INFO

        if (len(s)==0):

            print("Error ! You Entered Wrong information\n")
            break

        if(turn != 1):
            scores = {}
            for g in tqdm(gss, desc="Thinking..."):
                scores[g] = score_guess(g, s)

            scored_guesses = sorted(
                gss,
                key=lambda g: scores[g],
                reverse=True
            )
        else:
            scored_guesses = gss ### Already sorted before..

        # --- Show Top Suggestions ---
        print("----------- Top Suggestions -----------")
        for i in range(min(10, len(scored_guesses))): ### top ten or less...
            print(f"{i+1} - {scored_guesses[i]}  Entropy:{round(score_guess(scored_guesses[i],s),2)}")

        ###  User Input store in guess and the pattern store in pattern
        guess = input("Enter your guess:").lower()
        if (guess not in guesses):
            ErrorG=1
            while(ErrorG):
                guess = input("ERROR!!... Try Again !! \nEnter a valid guess:").lower()
                if(guess in guesses):
                    ErrorG=0


        pattern = input("Enter the given pattern:").lower()
        for char in pattern:
            if (char not in ["g","r","y"]):
                pattern_valid=0
                break
            pattern_valid=1

        
        if (len(pattern)!=5 or not pattern_valid ):
            ErrorP=1
            while(ErrorP):
                pattern = input("ERROR!!... Try Again !! \nEnter a valid pattern:").lower()
                for char in pattern:
                    if (char  not in ["g","r","y"]):
                        pattern_valid=0
                        break
                    pattern_valid=1

                if(len(pattern)==5 and pattern_valid):
                    ErrorP=0


        # handle the case of ggggg before filtering
        if(pattern =="ggggg"):
            print(f"Great!!! You Reached The Correct Answer:{guess}\n")
            break


        # --- FILTER POSSIBLE ANSWERS ---
        s = [word for word in s if feedback(guess, word) == pattern]
