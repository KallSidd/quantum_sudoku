from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from numpy import pi

qreg_q = QuantumRegister(24, 'q')
creg_c = ClassicalRegister(8, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

#Verifies a 4x4 board. If no input is specified uses a default valid board and 500 shots.
def verify(board=[[1, 2, 3, 4],[2, 3, 4, 1],[3, 4, 2, 1],[4, 3, 2, 1]], numShots=500):
    #initializing swap test bits
    circuit.h(qreg_q[0])
    circuit.h(qreg_q[5])
    circuit.h(qreg_q[10])
    circuit.h(qreg_q[15])
    
    #initializing rows and columns
    getCell(circuit, qreg_q, 1, board[0][0])
    getCell(circuit, qreg_q, 2, board[1][0])
    getCell(circuit, qreg_q, 3, board[2][0])
    getCell(circuit, qreg_q, 4, board[3][0])
    getCell(circuit, qreg_q, 6, board[0][1])
    getCell(circuit, qreg_q, 7, board[1][1])
    getCell(circuit, qreg_q, 8, board[2][1])
    getCell(circuit, qreg_q, 9, board[3][1])
    getCell(circuit, qreg_q, 11, board[0][2])
    getCell(circuit, qreg_q, 12, board[1][2])
    getCell(circuit, qreg_q, 13, board[2][2])
    getCell(circuit, qreg_q, 14, board[3][2])
    getCell(circuit, qreg_q, 16, board[0][3])
    getCell(circuit, qreg_q, 17, board[1][3])
    getCell(circuit, qreg_q, 18, board[2][3])
    getCell(circuit, qreg_q, 19, board[3][3])

    #conducting swap tests on all the rows
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[4])
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[3])
    circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[3])
    circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[4])
    circuit.cswap(qreg_q[0], qreg_q[3], qreg_q[4])
    circuit.h(qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])

    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[7])
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[8])
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[9])
    circuit.cswap(qreg_q[5], qreg_q[7], qreg_q[8])
    circuit.cswap(qreg_q[5], qreg_q[7], qreg_q[9])
    circuit.cswap(qreg_q[5], qreg_q[8], qreg_q[9])
    circuit.h(qreg_q[5])
    circuit.measure(qreg_q[5], creg_c[1])

    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[12])
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[13])
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[14])
    circuit.cswap(qreg_q[10], qreg_q[12], qreg_q[13])
    circuit.cswap(qreg_q[10], qreg_q[12], qreg_q[14])
    circuit.cswap(qreg_q[10], qreg_q[13], qreg_q[14])
    circuit.h(qreg_q[10])
    circuit.measure(qreg_q[10], creg_c[2])

    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[17])
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[18])
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[19])
    circuit.cswap(qreg_q[15], qreg_q[17], qreg_q[18])
    circuit.cswap(qreg_q[15], qreg_q[17], qreg_q[19])
    circuit.cswap(qreg_q[15], qreg_q[18], qreg_q[19])
    circuit.h(qreg_q[15])
    circuit.measure(qreg_q[15], creg_c[3])
    circuit.barrier()

    #column 1
    circuit.h(qreg_q[20])
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[6]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[11]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[16]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[6], qreg_q[11]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[6], qreg_q[16]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[11], qreg_q[16]).c_if(creg_c, 15)
    circuit.h(qreg_q[20])
    circuit.measure(qreg_q[20], creg_c[4])

    #column 2
    circuit.h(qreg_q[21])
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[7]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[12]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[17]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[7], qreg_q[12]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[7], qreg_q[17]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[12], qreg_q[17]).c_if(creg_c, 31)
    circuit.h(qreg_q[21])
    circuit.measure(qreg_q[21], creg_c[5])

    #column 3
    circuit.h(qreg_q[22])
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[8]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[13]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[18]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[8], qreg_q[13]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[8], qreg_q[18]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[13], qreg_q[18]).c_if(creg_c, 63)
    circuit.h(qreg_q[22])
    circuit.measure(qreg_q[22], creg_c[6])

    #column 4
    circuit.h(qreg_q[23])
    circuit.cswap(qreg_q[23], qreg_q[4], qreg_q[9]).c_if(creg_c, 127)
    circuit.cswap(qreg_q[23], qreg_q[4], qreg_q[14]).c_if(creg_c, 127)
    circuit.cswap(qreg_q[23], qreg_q[4], qreg_q[19]).c_if(creg_c, 127)
    circuit.cswap(qreg_q[23], qreg_q[9], qreg_q[14]).c_if(creg_c, 127)
    circuit.cswap(qreg_q[23], qreg_q[9], qreg_q[19]).c_if(creg_c, 127)
    circuit.cswap(qreg_q[23], qreg_q[14], qreg_q[19]).c_if(creg_c, 127)
    circuit.h(qreg_q[23])
    circuit.measure(qreg_q[23], creg_c[7])

    backend = Aer.get_backend('qasm_simulator') # the device to run on
    result = backend.run(circuit, shots=numShots).result()
    counts  = result.get_counts(circuit)
    print(counts)
    plot_histogram(counts, sort='desc', filename="validOutput")

    circuit.draw(output='mpl', filename="validCircuit")

    if('11111111' in counts):
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
    elif(num == 4):
        circuit.x(qreg[qubit])
        circuit.h(qreg[qubit])