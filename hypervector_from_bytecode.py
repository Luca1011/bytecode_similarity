#!/usr/bin/python3
import sys

# Filled with made up dummy data!
opcodes = {"ac5bf2":"PUSH", "7d42":"MSTORE", "26de1b":"SSTORE"}

def remove_swarm(bytecode):
    #TODO
    bytecode_trimmed = bytecode[0:len(bytecode)-1]
    return bytecode_trimmed

def remove_PUSH_op(opcode_array):
    #TODO
    return opcode_array

def disassemble(bytecode_trimmed):
    #TODO: Compare to opcodes
    opcode_array = {"SSTORE", "MSTORE"}
    #TODO: Fill opcode_array
    opcode_array = remove_PUSH_op(opcode_array)
    return opcode_array;

def extract_n_gram(n, opcode_array):
    #TODO
    n_gram = "SSTORE, PUSH, MSTORE, SSTORE, PUSH"
    return n_gram

def compute_hypervector(n_gram):
    #TODO
    hypervector = [1,2,3,4,5]
    return str(hypervector)

def bytecode_to_hypervector(filename):
    
    #Currently expecting bytecode as string, not as bytes
    with open(filename, 'r') as bytecode_file:
        bytecode = bytecode_file.read().replace("\n", '')
        bytecode_trimmed = remove_swarm(bytecode)
        opcode_array = disassemble(bytecode_trimmed)
        n_gram = extract_n_gram(5, opcode_array)
        hypervector = compute_hypervector(n_gram)

        with open("hypervector.csv",'w') as output_file:
            output_file.write(hypervector[1:len(hypervector)-1])

    return 


if __name__ == "__main__":
    
    if sys.argv[1] != None:
        bytecode_to_hypervector(sys.argv[1])
