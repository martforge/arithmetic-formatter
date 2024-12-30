def arithmetic_arranger(problems, show_answers=False):
    top_line = []
    bottom_line = []
    dashes_line = []
    results_line = []
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        # Check for invalid characters (alphabetic)
        for char in problem:
            if char.isalpha():
                return 'Error: Numbers must only contain digits.'
        
        num_a = ''
        num_b = ''
        operator = ''
        index = 0

        # num_a
        while index < len(problem) and problem[index].isdigit():
            num_a += problem[index]
            index += 1

        if not num_a.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        # spaces
        while index < len(problem) and problem[index] == ' ':
            index += 1 

        # operator
        if index < len(problem) and problem[index] in ['+', '-']:
            operator += problem[index]
            index += 1
        else:
            return "Error: Operator must be '+' or '-'."  

        # spaces
        while index < len(problem) and problem[index] == ' ':
            index += 1
        
        # num_b
        while index < len(problem) and problem[index].isdigit():
            num_b += problem[index]
            index += 1
        
        if not num_b.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        # not more than 4 digits
        if len(num_a) > 4 or len(num_b) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # calculation
        if show_answers:
            if operator == '+':
                result = str(int(num_a) + int(num_b))
            else:
                result = str(int(num_a) - int(num_b))
            results_line.append(result)

        # width
        width = max(len(num_a), len(num_b)) + 2  # +2 for space and operator
        
        # format
        top_line.append(' ' * (width - len(num_a)) + num_a)
        bottom_line.append(operator + ' ' * (width - len(num_b) - 1) + num_b)
        dashes_line.append('-' * width)
    
    # combine
    arranged_problems = '    '.join(top_line) + '\n' + '    '.join(bottom_line) + '\n' + '    '.join(dashes_line)
    
    # answers
    if show_answers:
        results = []
        for i, result in enumerate(results_line):
            spacing = len(dashes_line[i]) - len(result)
            results.append(' ' * spacing + result)
        arranged_problems += '\n' + '    '.join(results)
    
    return arranged_problems  

# Example usage
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')
