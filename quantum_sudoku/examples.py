#from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from numpy import pi

qreg_q = QuantumRegister(24, 'q')
creg_c = ClassicalRegister(8, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

def valid():
    print("Example using the following board:\n[1|2|3|4]\n[2|3|4|1]\n[3|2|1|4]\n[4|1|2|3]")
    #column 1
    #initialize the first column
    circuit.h(qreg_q[0])

    circuit.x(qreg_q[2])
    circuit.h(qreg_q[3])
    circuit.x(qreg_q[4])
    circuit.h(qreg_q[4])

    #conduct the swap test
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[4])
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[3])
    circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[3])
    circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[4])
    circuit.cswap(qreg_q[0], qreg_q[3], qreg_q[4])
    circuit.h(qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])

    #column 2
    #initialize the second column
    circuit.h(qreg_q[5])

    circuit.x(qreg_q[6])
    circuit.h(qreg_q[7])
    circuit.x(qreg_q[8])
    circuit.h(qreg_q[8])

    #conduct the swap test
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[7])
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[8])
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[9])
    circuit.cswap(qreg_q[5], qreg_q[7], qreg_q[8])
    circuit.cswap(qreg_q[5], qreg_q[7], qreg_q[9])
    circuit.cswap(qreg_q[5], qreg_q[8], qreg_q[9])
    circuit.h(qreg_q[5])
    circuit.measure(qreg_q[5], creg_c[1])

    #column 3
    #initialize the third column
    circuit.h(qreg_q[10])

    circuit.h(qreg_q[11])
    circuit.x(qreg_q[12])
    circuit.x(qreg_q[14])
    circuit.h(qreg_q[14])

    #conduct the swap test
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[12])
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[13])
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[14])
    circuit.cswap(qreg_q[10], qreg_q[12], qreg_q[13])
    circuit.cswap(qreg_q[10], qreg_q[12], qreg_q[14])
    circuit.cswap(qreg_q[10], qreg_q[13], qreg_q[14])
    circuit.h(qreg_q[10])
    circuit.measure(qreg_q[10], creg_c[2])

    #column 4
    #initialize the fourth column
    circuit.h(qreg_q[15])

    circuit.x(qreg_q[16])
    circuit.h(qreg_q[16])
    circuit.x(qreg_q[18])
    circuit.h(qreg_q[19])

    #conduct the swap test
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[17])
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[18])
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[19])
    circuit.cswap(qreg_q[15], qreg_q[17], qreg_q[18])
    circuit.cswap(qreg_q[15], qreg_q[17], qreg_q[19])
    circuit.cswap(qreg_q[15], qreg_q[18], qreg_q[19])
    circuit.h(qreg_q[15])
    circuit.measure(qreg_q[15], creg_c[3])

    circuit.barrier()
    #row 1
    circuit.h(qreg_q[20])
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[6]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[11]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[16]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[6], qreg_q[11]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[6], qreg_q[16]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[11], qreg_q[16]).c_if(creg_c, 15)
    circuit.h(qreg_q[20])
    circuit.measure(qreg_q[20], creg_c[4])

    #row 2
    circuit.h(qreg_q[21])
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[7]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[12]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[17]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[7], qreg_q[12]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[7], qreg_q[17]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[12], qreg_q[17]).c_if(creg_c, 31)
    circuit.h(qreg_q[21])
    circuit.measure(qreg_q[21], creg_c[5])

    #row 3
    circuit.h(qreg_q[22])
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[8]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[13]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[18]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[8], qreg_q[13]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[8], qreg_q[18]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[13], qreg_q[18]).c_if(creg_c, 63)
    circuit.h(qreg_q[22])
    circuit.measure(qreg_q[22], creg_c[6])

    #row 4
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
    result = backend.run(circuit, shots=500).result()
    counts  = result.get_counts(circuit)
    print(counts)
    plot_histogram(counts, sort='desc', filename="validOutput")

    circuit.draw(output='mpl', filename="validCircuit")

    if('11111111' in counts):
        print("valid")
    else:
        print("invalid")

def invalid():
    print("Example using the following board:\n[2|1|1|1]\n[4|3|3|3]\n[1|4|4|]\n[3|2|2|2]")
    #column 1
    #initialize the first column
    circuit.h(qreg_q[0])

    circuit.x(qreg_q[1])
    circuit.h(qreg_q[2])
    circuit.x(qreg_q[2])
    circuit.x(qreg_q[3])
    circuit.h(qreg_q[4])

    #conduct the swap test
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[4])
    circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[3])
    circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[3])
    circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[4])
    circuit.cswap(qreg_q[0], qreg_q[3], qreg_q[4])
    circuit.h(qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])

    #column 2
    #initialize the second column
    circuit.h(qreg_q[5])

    circuit.h(qreg_q[7])
    circuit.x(qreg_q[8])
    circuit.h(qreg_q[8])
    circuit.x(qreg_q[9])

    #conduct the swap test
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[7])
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[8])
    circuit.cswap(qreg_q[5], qreg_q[6], qreg_q[9])
    circuit.cswap(qreg_q[5], qreg_q[7], qreg_q[8])
    circuit.cswap(qreg_q[5], qreg_q[7], qreg_q[9])
    circuit.cswap(qreg_q[5], qreg_q[8], qreg_q[9])
    circuit.h(qreg_q[5])
    circuit.measure(qreg_q[5], creg_c[1])

    #column 3
    #initialize the third column
    circuit.h(qreg_q[10])

    circuit.h(qreg_q[12])
    circuit.x(qreg_q[13])
    circuit.h(qreg_q[13])
    circuit.x(qreg_q[14])

    #conduct the swap test
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[12])
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[13])
    circuit.cswap(qreg_q[10], qreg_q[11], qreg_q[14])
    circuit.cswap(qreg_q[10], qreg_q[12], qreg_q[13])
    circuit.cswap(qreg_q[10], qreg_q[12], qreg_q[14])
    circuit.cswap(qreg_q[10], qreg_q[13], qreg_q[14])
    circuit.h(qreg_q[10])
    circuit.measure(qreg_q[10], creg_c[2])

    #column 4
    #initialize the fourth column
    circuit.h(qreg_q[15])

    circuit.h(qreg_q[17])
    circuit.x(qreg_q[18])
    circuit.h(qreg_q[18])
    circuit.x(qreg_q[19])

    #conduct the swap test
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[17])
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[18])
    circuit.cswap(qreg_q[15], qreg_q[16], qreg_q[19])
    circuit.cswap(qreg_q[15], qreg_q[17], qreg_q[18])
    circuit.cswap(qreg_q[15], qreg_q[17], qreg_q[19])
    circuit.cswap(qreg_q[15], qreg_q[18], qreg_q[19])
    circuit.h(qreg_q[15])
    circuit.measure(qreg_q[15], creg_c[3])

    circuit.barrier()
    #row 1
    circuit.h(qreg_q[20])
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[6]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[11]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[1], qreg_q[16]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[6], qreg_q[11]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[6], qreg_q[16]).c_if(creg_c, 15)
    circuit.cswap(qreg_q[20], qreg_q[11], qreg_q[16]).c_if(creg_c, 15)
    circuit.h(qreg_q[20])
    circuit.measure(qreg_q[20], creg_c[4])

    #row 2
    circuit.h(qreg_q[21])
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[7]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[12]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[2], qreg_q[17]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[7], qreg_q[12]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[7], qreg_q[17]).c_if(creg_c, 31)
    circuit.cswap(qreg_q[21], qreg_q[12], qreg_q[17]).c_if(creg_c, 31)
    circuit.h(qreg_q[21])
    circuit.measure(qreg_q[21], creg_c[5])

    #row 3
    circuit.h(qreg_q[22])
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[8]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[13]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[3], qreg_q[18]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[8], qreg_q[13]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[8], qreg_q[18]).c_if(creg_c, 63)
    circuit.cswap(qreg_q[22], qreg_q[13], qreg_q[18]).c_if(creg_c, 63)
    circuit.h(qreg_q[22])
    circuit.measure(qreg_q[22], creg_c[6])

    #row 4
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
    result = backend.run(circuit, shots=500).result()
    counts  = result.get_counts(circuit)
    print(counts)
    plot_histogram(counts, sort='desc', filename="invalidOutput")

    circuit.draw(output='mpl', filename="invalidCircuit")

    if('11111111' in counts):
        print("valid")
    else:
        print("invalid")