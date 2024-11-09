import random
import difflib

with open('words.txt', 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file.readlines()]
allword: list[str] = [chr(i) for i in range(97, 123)]


def reload():
    return start() if input("是否再来一局:(y/n)").strip().lower() == "y" else exit(0)


def start():
    while True:
        chosen_word: str = random.choice(words)
        num: int = 10
        correct: list[str] = [i for i in chosen_word]
        output: str = ""
        while num:
            inputed: str = input("guess word:").lower()
            if inputed == chosen_word:
                print(f'\033[92myou won,the correct word is "{chosen_word}"\033[0m')
                reload()
            if inputed not in words:
                close_matches = difflib.get_close_matches(inputed, words, 1, 0.6)
                print(f'inputed error(\033[31m"{inputed}"\033[0m)', end="")
                if close_matches:
                    print(f',Did you mean \"{close_matches[0]}\"?')
                else:
                    print()
                continue
            list_inputed: list[str] = [i for i in inputed]
            for i in range(5):
                if list_inputed[i] == correct[i]:
                    output += f"\033[92m{list_inputed[i]}\033[0m "
                elif list_inputed[i] in correct:
                    output += f"\033[93m{list_inputed[i]}\033[0m "
                else:
                    output += f"\033[90m{list_inputed[i]}\033[0m "
                if list_inputed[i] in allword:
                    allword.remove(list_inputed[i])
            print(f"{output}\n还未试过的:", end="")
            for i in allword:
                print(i, end="")
            num -= 1
            output += "\n"
            print(f"        还剩{num}次机会")
        print(f'\033[31myou lose,the correct word is "{chosen_word}"\033[0m')
        reload()


if __name__ == "__main__":
    start()
