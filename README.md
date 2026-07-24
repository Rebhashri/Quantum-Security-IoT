# Quantum Security in IoT

A proof-of-concept IoT security system that combines an ESP32-based keypad with Qiskit and IBM Quantum services to demonstrate the use of quantum-generated random keys for PIN data encryption.

## Overview

The project demonstrates a quantum-assisted security approach for protecting sensitive data entered through an IoT device.

A user enters a PIN using a 4×3 matrix keypad connected to an ESP32. The ESP32 sends the entered PIN to a Python application through serial communication. The Python application generates a 4-bit quantum random key using Qiskit and an IBM Quantum backend.

The generated key is then used in an XOR-based encryption and decryption process to demonstrate the protection of the PIN data.

## System Workflow

```text
User enters PIN
        ↓
4×3 Matrix Keypad
        ↓
ESP32
        ↓
Serial Communication
        ↓
Python Application
        ↓
Qiskit + IBM Quantum
        ↓
Quantum Random Key
        ↓
XOR Encryption
        ↓
Encrypted PIN
        ↓
XOR Decryption
        ↓
Original PIN
```

## Features

- ESP32-based IoT data input
- 4×3 matrix keypad interface
- Serial communication between ESP32 and Python
- Quantum circuit-based random key generation
- Integration with IBM Quantum services
- XOR-based encryption demonstration
- XOR-based decryption demonstration
- Python-based implementation

## Hardware Requirements

- ESP32 development board
- 4×3 matrix keypad
- USB cable
- Computer

## Software Requirements

- Arduino IDE
- Python 3.x
- Qiskit
- Qiskit IBM Runtime
- PySerial
- IBM Quantum account

## Technologies Used

- ESP32
- Arduino
- Python
- Qiskit
- IBM Quantum
- Quantum Computing
- Serial Communication
- XOR Encryption

## Project Structure

```text
Quantum-Security-IoT/
│
├── arduino/
│   └── esp32_keypad.ino
│
├── python/
│   └── quantum_security.py
│
├── experiments/
│   └── basic_quantum_random_demo.py
│
├── results/
│
├── docs/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Navigate to the project directory:

```bash
cd Quantum-Security-IoT
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## IBM Quantum Configuration

The Python application uses Qiskit IBM Runtime to access an IBM Quantum backend.

Before running the application, configure your IBM Quantum account credentials according to the Qiskit IBM Runtime documentation.

Do not include API tokens, passwords, or other credentials directly in the source code or commit them to GitHub.

## Running the Project

### 1. Upload the Arduino Code

Open the following file in Arduino IDE:

```text
arduino/esp32_keypad.ino
```

Connect the ESP32 to the computer and upload the Arduino code.

### 2. Connect the ESP32

Connect the ESP32 to the computer using a USB cable.

The Python application communicates with the ESP32 through serial communication.

The serial port used in the Python program is currently:

```python
ser = serial.Serial("COM7", 115200)
```

If your ESP32 is assigned a different COM port, update the port number accordingly.

### 3. Run the Python Application

Navigate to the Python directory:

```bash
cd python
```

Run the main Python application:

```bash
python quantum_security.py
```

### 4. Enter a PIN

Enter a PIN using the 4×3 keypad connected to the ESP32.

Press `#` to submit the PIN.

The Python application receives the PIN and performs the following operations:

1. Receives the PIN from the ESP32.
2. Generates a quantum random key using Qiskit and IBM Quantum.
3. Converts the PIN into binary data.
4. Encrypts the binary data using XOR.
5. Decrypts the encrypted data using the same key.
6. Converts the decrypted binary data back into text.
7. Displays the encryption and decryption results.

## Example Output

```text
Listening to ESP32...

ESP32: Entered PIN: 1234

PIN Received: 1234
Quantum Key: 1010
Encrypted PIN: <binary encrypted data>
Decrypted PIN: 1234

=============================
```

The quantum key and encrypted output may vary between executions.

## Project Status

This project is currently a proof-of-concept demonstration of quantum-assisted security for IoT applications.

The implementation demonstrates the integration of:

- IoT hardware
- ESP32
- Keypad-based user input
- Serial communication
- Quantum random number generation
- Classical XOR encryption
- Data encryption and decryption

## Limitations

The current implementation uses a 4-bit quantum key that is repeated to match the length of the input data.

The XOR encryption used in this project is intended for educational and proof-of-concept purposes and should not be considered a production-grade encryption system.

The project demonstrates the concept of using quantum-generated randomness in an IoT security workflow rather than providing a complete cryptographic security solution.

## Future Enhancements

- Generate longer quantum random keys
- Implement stronger cryptographic algorithms
- Improve secure key management
- Add encrypted communication between the ESP32 and Python application
- Integrate secure authentication mechanisms
- Store encrypted data securely
- Improve real-time quantum hardware integration
- Extend the system for other IoT security applications
- Develop a standalone IoT security application

## Security Note

This project is developed for educational and research purposes.

The current implementation demonstrates the concept of integrating quantum-generated randomness into an IoT security workflow. The XOR encryption method used here is not intended to replace established cryptographic standards for real-world security applications.

Sensitive information such as IBM Quantum API tokens, passwords, personal credentials, and real PINs should never be committed to the GitHub repository.

## Author

**RubyRe**

Engineering Student

Interests:
- IoT
- Embedded Systems
- Quantum Computing
- Cybersecurity
- Python