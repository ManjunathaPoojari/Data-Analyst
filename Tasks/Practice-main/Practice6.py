def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    lines = []

    for i in range(size):
        left = '-'.join(alpha[size-1:i:-1])  
        right = '-'.join(alpha[i:size])      
        line = (left + '-' + right) if left else right
        line = line.center(4*size - 3, '-')
        lines.append(line)

    for line in lines[::-1][1:]:
        lines.append(line)

    for line in lines:
        print(line)

n = int(input())
print_rangoli(n)
