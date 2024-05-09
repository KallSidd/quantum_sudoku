from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from numpy import pi

qreg_q = QuantumRegister(15, 'q')
creg_c = ClassicalRegister(6, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

#Verifies a 3x3 board. If no input is specified uses a default valid board and 500 shots.
def verify(board=[[1, 2, 3],[2, 3, 1],[3, 2, 1],], numShots=500):
    #initializing swap test bits
    circuit.h(qreg_q[0])
    circuit.h(qreg_q[4])
    circuit.h(qreg_q[8])
    
    #initializing rows and columns
    getCell(circuit, qreg_q, 1, board[0][0])
    getCell(circuit, qreg_q, 2, board[1][0])
    getCell(circuit, qreg_q, 3, board[2][0])
    getCell(circuit, qreg_q, 5, board[0][1])
    getCell(circuit, qreg_q, 6, board[1][1])
    getCell(circuit, qreg_q, 7, board[2][1])
    getCell(circuit, qreg_q, 9, board[0][2])
    getCell(circuit, qreg_q, 10, board[1][2])
    getCell(circuit, qreg_q, 11, board[2][2])

    #conducting swap tests on all the rows
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[3])
    circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[3])
    circuit.h(qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])

    circuit.cswap(qreg_q[4], qreg_q[5], qreg_q[6])
    circuit.cswap(qreg_q[4], qreg_q[5], qreg_q[7])
    circuit.cswap(qreg_q[4], qreg_q[6], qreg_q[7])
    circuit.h(qreg_q[4])
    circuit.measure(qreg_q[4], creg_c[1])

    circuit.cswap(qreg_q[8], qreg_q[9], qreg_q[10])
    circuit.cswap(qreg_q[8], qreg_q[9], qreg_q[11])
    circuit.cswap(qreg_q[8], qreg_q[10], qreg_q[11])
    circuit.h(qreg_q[8])
    circuit.measure(qreg_q[8], creg_c[2])
    circuit.barrier()

    #column 1
    circuit.h(qreg_q[12])
    circuit.cswap(qreg_q[12], qreg_q[1], qreg_q[5])
    circuit.cswap(qreg_q[12], qreg_q[1], qreg_q[9])
    circuit.cswap(qreg_q[12], qreg_q[5], qreg_q[9])
    circuit.h(qreg_q[12])
    circuit.measure(qreg_q[12], creg_c[3])

    #column 2
    circuit.h(qreg_q[13])
    circuit.cswap(qreg_q[13], qreg_q[2], qreg_q[6])
    circuit.cswap(qreg_q[13], qreg_q[2], qreg_q[10])
    circuit.cswap(qreg_q[13], qreg_q[6], qreg_q[10])
    circuit.h(qreg_q[13])
    circuit.measure(qreg_q[13], creg_c[4])

    #column 3
    circuit.h(qreg_q[14])
    circuit.cswap(qreg_q[14], qreg_q[3], qreg_q[7])
    circuit.cswap(qreg_q[14], qreg_q[3], qreg_q[11])
    circuit.cswap(qreg_q[14], qreg_q[7], qreg_q[11])
    circuit.h(qreg_q[14])
    circuit.measure(qreg_q[14], creg_c[5])

    backend = Aer.get_backend('qasm_simulator') # the device to run on
    result = backend.run(circuit, shots=numShots).result()
    counts  = result.get_counts(circuit)
    print(counts)
    plot_histogram(counts, sort='desc', filename="3x3Output")

    circuit.draw(output='mpl', filename="3x3validCircuit")

    if('111111' in counts):
        print("valid")
    else:
        print("invalid")

#helper to initialize qubits
def getCell(circuit, qreg, qubit, num):
    if(num == 1):
        pass
    elif(num == 2):
        circuit.x(qreg[qubit])
    elif(num == 3):
        circuit.h(qreg[qubit])
verify()