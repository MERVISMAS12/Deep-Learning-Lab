def gate_func(inputs, weigths, threshold):
    ws = sum(i * w for i, w in zip(inputs, weigths))
    return 1 if ws >= threshold else 0, weigths, threshold

def and_func(x1, x2):
    return gate_func(inputs=[x1,x2], weigths=[1,1], threshold=2)

def generate_gate_table(gate_func, gate_name, inputs):
    print(f"{gate_name} Gate: ")
    print(f" x1 \t x2 \t O/P")
    for x1, x2 in inputs:
        output, weigths, threshold = gate_func(x1, x2)
        weights_str = " , ".join(map(str, weigths))
        print(f" {x1} \t {x2} \t {output}")
    print(f"Expected Weights: {weights_str} \nExpected Threshold: {threshold}")
    
input_comb = [(0,0),(0,1),(1,0),(1,1)]
generate_gate_table(and_func, "AND", input_comb)