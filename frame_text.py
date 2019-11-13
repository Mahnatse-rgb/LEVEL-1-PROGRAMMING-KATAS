def print_in_a_frame(*words):
    size = max(len(word) for word in words)
    print('*' * (size + 4))
    
    for word in words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))

print_in_a_frame("Write", "good", "code", "every", "day")