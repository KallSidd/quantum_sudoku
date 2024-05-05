from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from numpy import pi

qreg_q = QuantumRegister(27, 'q')
creg_c = ClassicalRegister(18, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

# 0 1 2
# 3 4 5
# 6 7 8

#example grid
# 1 2 3
# 2 3 1
# 3 1 2
 
#number mapping
# 0 -> 1
# 1 -> 2
# + -> 3

#initialize the qubits
circuit.x(qreg_q[1])
circuit.h(qreg_q[2])

circuit.x(qreg_q[3])
circuit.h(qreg_q[4])

circuit.h(qreg_q[6])
circuit.x(qreg_q[8])

#compare qubits 1 and 2
circuit.cx(qreg_q[0], qreg_q[9])
circuit.cx(qreg_q[1], qreg_q[9])
#compare qubits 1 and 3
circuit.cx(qreg_q[0], qreg_q[10])
circuit.cx(qreg_q[2], qreg_q[10])
#compare qubits 2 and 3
circuit.cx(qreg_q[1], qreg_q[11])
circuit.cx(qreg_q[2], qreg_q[11])

#compare qubits 4 and 5
circuit.cx(qreg_q[3], qreg_q[12])
circuit.cx(qreg_q[4], qreg_q[12])
#compare qubits 4 and 6
circuit.cx(qreg_q[3], qreg_q[13])
circuit.cx(qreg_q[5], qreg_q[13])
#compare qubits 5 and 6
circuit.cx(qreg_q[4], qreg_q[14])
circuit.cx(qreg_q[5], qreg_q[14])

#compare qubits 7 and 8
circuit.cx(qreg_q[6], qreg_q[15])
circuit.cx(qreg_q[7], qreg_q[15])
#compare qubits 7 and 9
circuit.cx(qreg_q[6], qreg_q[16])
circuit.cx(qreg_q[8], qreg_q[16])
#compare qubits 8 and 9
circuit.cx(qreg_q[7], qreg_q[17])
circuit.cx(qreg_q[8], qreg_q[17])

#compare qubits 1 and 4
circuit.cx(qreg_q[0], qreg_q[18])
circuit.cx(qreg_q[3], qreg_q[18])
#compare qubits 1 and 7
circuit.cx(qreg_q[0], qreg_q[19])
circuit.cx(qreg_q[6], qreg_q[19])
#compare qubits 4 and 7
circuit.cx(qreg_q[3], qreg_q[20])
circuit.cx(qreg_q[6], qreg_q[20])

#compare qubits 2 and 5
circuit.cx(qreg_q[0], qreg_q[21])
circuit.cx(qreg_q[1], qreg_q[21])
#compare qubits 2 and 8
circuit.cx(qreg_q[0], qreg_q[22])
circuit.cx(qreg_q[2], qreg_q[22])
#compare qubits 5 and 8
circuit.cx(qreg_q[1], qreg_q[23])
circuit.cx(qreg_q[2], qreg_q[23])

#compare qubits 3 and 6
circuit.cx(qreg_q[2], qreg_q[24])
circuit.cx(qreg_q[5], qreg_q[24])
#compare qubits 3 and 9
circuit.cx(qreg_q[2], qreg_q[25])
circuit.cx(qreg_q[8], qreg_q[25])
#compare qubits 6 and 9
circuit.cx(qreg_q[5], qreg_q[26])
circuit.cx(qreg_q[8], qreg_q[26])

circuit.measure(qreg_q[9], creg_c[0])
circuit.measure(qreg_q[10], creg_c[1])
circuit.measure(qreg_q[11], creg_c[2])
circuit.measure(qreg_q[12], creg_c[3])
circuit.measure(qreg_q[13], creg_c[4])
circuit.measure(qreg_q[14], creg_c[5])
circuit.measure(qreg_q[15], creg_c[6])
circuit.measure(qreg_q[16], creg_c[7])
circuit.measure(qreg_q[17], creg_c[8])
circuit.measure(qreg_q[18], creg_c[9])
circuit.measure(qreg_q[19], creg_c[10])
circuit.measure(qreg_q[20], creg_c[11])
circuit.measure(qreg_q[21], creg_c[12])
circuit.measure(qreg_q[22], creg_c[13])
circuit.measure(qreg_q[23], creg_c[14])
circuit.measure(qreg_q[24], creg_c[15])
circuit.measure(qreg_q[25], creg_c[16])
circuit.measure(qreg_q[26], creg_c[17])

backend = Aer.get_backend('qasm_simulator') # the device to run on
result = backend.run(circuit, shots=1000).result()
counts  = result.get_counts(circuit)
print(counts)
plot_histogram(counts, sort='desc', filename="3x3Output")
print(len(counts))