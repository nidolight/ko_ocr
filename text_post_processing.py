#딕셔너리 내의 단어들중 가장일치하는 단어를 반환

from jamo import h2j, j2hcj
from hangul_utils import join_jamos
from difflib import SequenceMatcher
import pickle

def find_word(text):
    word = j2hcj(h2j(text))
    with open('dict.pkl', 'rb') as f:
        mydict = pickle.load(f)

    tmp = 0
    ans = "null"
    for key, val in mydict.items():
        similarity = similar(word, key)
        if similarity > 0.35 and similarity > tmp:
            tmp = similarity
            ans = key
    print("similairity : " + str(tmp))
    print("ans : " + str(ans))
    ans = join_jamos(str(ans))
        
    return ans

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == "__main__":
    print(find_word("동육앙정살"))
