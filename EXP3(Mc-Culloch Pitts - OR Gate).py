def gate_func(inputs, weights, threshold):
    ws = sum(i*w for i, w in zip(inputs, weights))
    return 1 if ws >= threshold else 0, weights, threshold

def or_func(x1, x2):
    return gate_func(inputs = [x1,x2], weights = [1,1], threshold= 1)

def generate_gate_table(gate_function, gate_name, inputs):
    print(f"{gate_name} Gate:")
    print(" x1 \t x2 \t O/P")
    for x1, x2 in inputs:
        outputs, weights, threshold = gate_function(x1, x2)
        weight_str = " , ".join(map(str, weights))
        print(f" {x1} \t {x2} \t {outputs}")
    print(f"Expected Weights: {weight_str} \nExpected Threshold: {threshold}")

input_comb = [(0,0),(0,1),(1,0),(1,1)]
generate_gate_table(or_func, "OR", input_comb)