def arithmetic_arranger(problems, my_bool = False):
    # Constraint 1.
    count = len(problems)
    if count > 5:
        return "Error: Too many problems."
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    for i in range(count):
        first = problems[i].split()

        length_1 = len(first[0])
        length_2 = len(first[2])

        # Constraint 2.
        if length_1 > 4 or length_2 > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Constraint 3.
        if first[1] != "+" and first[1] != "-":
            return "Error: Operator must be '+' or '-'." 

        # Constraint 4.
        if not (first[0].isdigit() and first[2].isdigit()):
            return "Error: Numbers must only contain digits."

        max_length = max(len(first[0]), len(first[2]))

        space_1 = " "*(max_length - length_1 + 2)
        space_2 = " "*(max_length - length_2 + 1)
        dash = "-"*(max_length + 2)
        
        # Creating each line with specified spacing.
        line_1 = f"{line_1}{space_1}{first[0]}    "
        line_2 = f"{line_2}{first[1]}{space_2}{first[2]}    "
        line_3 = f"{line_3}{dash}    "

        # 4th optional line for answer.
        ans = eval(problems[i])
        length_ans = len(str(ans))
        space_4 = " "*(max_length + 2 - length_ans)
        line_4 = f"{line_4}{space_4}{ans}    "
    
    # Return formatted lines. Answer line included if my_bool parameter set to True.
    if my_bool:
        final_ans = f"{line_1.rstrip()}\n{line_2.rstrip()}\n{line_3.rstrip()}\n{line_4.rstrip()}"
        return final_ans
    else:
        final_ans = f"{line_1.rstrip()}\n{line_2.rstrip()}\n{line_3.rstrip()}"
        return final_ans

# Test cases:
# print(arithmetic_arranger(["32 + 8", "1 - 0", "99 + 9999", "53 - 49", "3 + 49", ], True))
