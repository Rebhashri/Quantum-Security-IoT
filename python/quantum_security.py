import serial
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2


# ===== CONNECT TO ESP32 =====
ser = serial.Serial("COM7", 115200)
print("Listening to ESP32...\n")


# ===== QUANTUM RANDOM NUMBER GENERATOR =====
def generate_qrng_key():
    service = QiskitRuntimeService()
    backend = service.least_busy(simulator=False)

    # Create a 4-qubit quantum circuit
    qc = QuantumCircuit(4, 4)

    # Put all qubits into superposition
    for i in range(4):
        qc.h(i)

    # Measure the qubits
    qc.measure(range(4), range(4))

    # Transpile circuit for the selected IBM Quantum backend
    tqc = transpile(qc, backend)

    # Run the quantum circuit
    sampler = SamplerV2(backend)
    job = sampler.run([tqc], shots=1)

    # Get result
    result = job.result()

    # Extract the measured 4-bit quantum random key
    counts = result[0].data.c.get_counts()
    qrng_key = list(counts.keys())[0]

    return qrng_key


# ===== XOR ENCRYPTION AND DECRYPTION =====
def encrypt_decrypt(data, key):

    # Convert input data into binary
    binary_data = "".join(format(ord(c), "08b") for c in data)

    # Repeat the quantum key to match the length of the data
    extended_key = (
        key * ((len(binary_data) // len(key)) + 1)
    )[:len(binary_data)]

    # XOR encryption
    encrypted = "".join(
        str(int(binary_data[i]) ^ int(extended_key[i]))
        for i in range(len(binary_data))
    )

    # XOR decryption
    decrypted_binary = "".join(
        str(int(encrypted[i]) ^ int(extended_key[i]))
        for i in range(len(encrypted))
    )

    # Convert decrypted binary back to text
    decrypted_text = "".join(
        chr(int(decrypted_binary[i:i + 8], 2))
        for i in range(0, len(decrypted_binary), 8)
    )

    return encrypted, decrypted_text


# ===== MAIN PROGRAM =====
while True:

    try:
        # Read data sent by ESP32
        data = ser.readline().decode(errors="ignore").strip()

        if data:
            print("ESP32:", data)

            # Check whether a PIN has been entered
            if "Entered PIN:" in data:

                # Extract PIN from serial message
                pin = data.split(":", 1)[1].strip()

                print("\nPIN Received:", pin)

                # Generate quantum random key
                quantum_key = generate_qrng_key()

                print("Quantum Key:", quantum_key)

                # Encrypt and decrypt PIN
                encrypted, decrypted = encrypt_decrypt(
                    pin, quantum_key
                )

                print("Encrypted PIN:", encrypted)
                print("Decrypted PIN:", decrypted)

                print("\n=============================\n")

                # Save demonstration results
                with open("output.txt", "w") as f:
                    f.write("Encrypted PIN: " + encrypted + "\n")
                    f.write("Decrypted PIN: " + decrypted + "\n")

    except KeyboardInterrupt:
        print("\nStopped by user")
        break

    except Exception as e:
        print("Error:", e)
