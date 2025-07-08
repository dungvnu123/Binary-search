def step(x):
    return 1 if x >= 0 else 0

def perceptron_step(x1, x2):
    w1, w2 = 1, 1
    b = -1.5
    output = x1*w1 + x2*w2 + b
    return step(output)

for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} AND {x2} = {perceptron_step(x1, x2)}")
