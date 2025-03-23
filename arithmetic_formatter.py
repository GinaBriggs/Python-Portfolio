def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    operators = ["+", "-"]
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        part = problem.split()

        
        if len(part) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = part

        
        if operator not in operators:
            return "Error: Operator must be '+' or '-'."

        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        
        width = max(len(num1), len(num2)) + 2

        
        first_line.append(num1.rjust(width))
        second_line.append(operator + " " + num2.rjust(width - 2))
        dash_line.append("-" * width)

        
        if show_answers:
            result = str(int(num1) + int(num2)) if operator == "+" else str(int(num1) - int(num2))
            answer_line.append(result.rjust(width))

    
    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(dash_line),
    ])

    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
