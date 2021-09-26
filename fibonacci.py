# Amar Nagim
# F1.5.01.L4 - Fibonacci reeksFuncties
# a+b/a=1.618034


def guldenSnede():
    sequence = [1,1]
    for n in range(100):
        sequence.append(sequence[-1]+sequence[-2])
    print(sequence[-1]/sequence[-2])


guldenSnede()
       





