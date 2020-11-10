# python3

from collections import namedtuple

# below named tuple is used to put both the character and position on the stack
Bracket = namedtuple("Bracket", ["char", "position"])


# below method checks for matching left & right character and return True if matching
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


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


def main():
    text = input("give input text: \n")
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
