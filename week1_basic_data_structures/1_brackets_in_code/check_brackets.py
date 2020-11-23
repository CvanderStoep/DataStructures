# python3
import os
from collections import namedtuple

# below named tuple is used to put both the character and position on the stack
Bracket = namedtuple("Bracket", ["char", "position"])


# below method checks for matching left & right character and return True if matching
def are_matching(left, right):
    return (left, right) in [("(", ")"), ("[", "]"), ("{", "}")]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_character in enumerate(text):
        br = Bracket(next_character, i)
        # print("bracket is: ", br)
        if next_character in "([{":
            # Process opening bracket
            opening_brackets_stack.append(br)

        if next_character in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1, False
            top_of_stack_char, top_of_stack_pos = opening_brackets_stack.pop()
            if not are_matching(top_of_stack_char, next_character):
                return i + 1, False

    # everything matches and stack is empty
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        # Still characters left on the stack, return the position of the top of the stack.
        top_of_stack_char, top_of_stack_pos = opening_brackets_stack.pop()
        return top_of_stack_pos + 1, False

#TODO output only number iso tuple (i, false)
#TODO convert below into a unit test
def test_files():
    """"This routine runs all the test files in the test directory"""

    os.chdir('./tests')
    for f in os.listdir():
        file_name, f_ext = os.path.splitext(f)
        file = open(f,"r")
        if f_ext != ".a":
            # print(f)
            input_text = file.read().strip()
            mismatch = find_mismatch(input_text)
        else:
            output_text = file.read().strip()
            # print(input_text)
            # print(mismatch)
            # print(output_text)
            if "Success" in output_text and "Success" in mismatch: #both give success
                print(f, "pass")
            elif str(output_text) == str(mismatch[0]): #both give same answer
                print(f, "pass")
            else:
                print(f, 'wrong answer!') #something is wrong

def main():
    test_files()
    text = input("give input text: \n")
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
