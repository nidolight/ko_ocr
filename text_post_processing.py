#딕셔너리 내의 단어들중 가장일치하는 단어를 반환

from jamo import h2j, j2hcj
from hangul_utils import join_jamos
from difflib import SequenceMatcher

def find_word(text):
    word = j2hcj(h2j(text))
    # word_dic = []  # dic 불러오기
    # f = open("word_dic.txt", 'r', encoding='utf-8')
    # lines = f.readlines()
    # for line in lines:
    #     word_dic.append(line)
    # f.close()
    word_dic = [["ㅁㅐㅇㅣㄹㅇㅜㅇㅠ"], [
        "ㄷㅗㄴㅇㅠㄱㄷㅡㅇㅅㅣㅁㄷㅓㅅㅅㅏㄹ"], ["ㅅㅡㅍㅡㄹㅏㅇㅣㅌㅡ"], ["ㄷㅗㄴㅇㅠㄱㅎㅏㅇㅈㅓㅇㅅㅏㄹ"], ["ㄷㅗㄴㅇㅠㄱㅁㅗㄱㅅㅣㅁ"]
        ["ㄲㅐㅅㅇㅣㅍ"], ["ㅍㅗㅋㅏㅊㅣㅂ"]]

    tmp = 0
    ans = "null"
    for dic in word_dic:
        similarity = similar(word, str(dic))
        if similarity > 0.35 and similarity > tmp:
            tmp = similarity
            ans = dic
    ans = join_jamos(str(ans))
        
    return ans


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


if __name__ == "__main__":
    print(find_word("포카칩"))
