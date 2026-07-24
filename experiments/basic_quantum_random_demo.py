from qiskit import QuantumCircuit
import random

# Number of random bits to generate
num_bits = 8

# Create quantum circuit
qc = QuantumCircuit(num_bits, num_bits)

# Apply Hadamard gate to each qubit
for i in range(num_bits):
    qc.h(i)

# Measure all qubits
for i in range(num_bits):
    qc.measure(i, i)

# Simulate random results
random_bits = [random.choice([0, 1]) for _ in range(num_bits)]

print("Quantum Random Bits:", random_bits)

# Display quantum circuit
print(qc.draw())
