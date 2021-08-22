#딕셔너리 내의 단어들중 가장일치하는 단어로 변환
from jamo import h2j, j2hcj


def find_word(text):
    print(j2hcj(h2j(text)))
    #제일 유사한 단어 선택 후 출력

    ans = text
    return ans


if __name__ == "__main__":
    find_word("동해물과백두산")
