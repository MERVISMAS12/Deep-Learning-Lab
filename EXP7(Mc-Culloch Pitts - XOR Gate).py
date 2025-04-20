def gate_func(inputs, weights, threshold):
    ws = sum(i * w for i, w in zip(inputs, weights))
    return 1 if ws >= threshold else 0, weights, threshold

def and_func(x1, x2):
    return gate_func(inputs=[x1, x2], weights=[1, 1], threshold=2)
def or_func(x1, x2):
    return gate_func(inputs=[x1, x2], weights=[1, 1], threshold=1)

def xor_func(x1, x2):
    and_output, and_weights, and_threshold = and_func(x1, x2)
    or_output, or_weights, or_threshold = or_func(x1, x2)
    
    xor_output, xor_weights, xor_threshold = gate_func(
        inputs=[or_output, and_output], weights=[1, -1], threshold=1)
    
    return xor_output, xor_weights, xor_threshold

def generate_gate_table(gate_function, gate_name, inputs):
    print(f"{gate_name} Gate:")
    print(" x1 \t x2 \t O/P")
    for x1, x2 in inputs:
        xor_output, xor_weights, xor_threshold = gate_function(x1, x2)
        xor_weights_str = " , ".join(map(str, xor_weights))
        print(f" {x1} \t {x2} \t {xor_output}")
    print(f"Expected Weights: {xor_weights_str} \nExpected Threshold: {xor_threshold}")


input_comb = [(0,0),(0,1),(1,0),(1,1)]
generate_gate_table(xor_func, "XOR", input_comb)
    
    

