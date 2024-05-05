from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from numpy import pi

qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.x(qreg_q[2])
circuit.x(qreg_q[3])

circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])

circuit.h(qreg_q[4])
circuit.cswap(qreg_q[4], qreg_q[1], qreg_q[3])
circuit.h(qreg_q[4])
circuit.measure(qreg_q[4], creg_c[1])

circuit.h(qreg_q[5])
circuit.cswap(qreg_q[5], qreg_q[2], qreg_q[3])
circuit.h(qreg_q[5])
circuit.measure(qreg_q[5], creg_c[2])

backend = Aer.get_backend('qasm_simulator') # the device to run on
result = backend.run(circuit, shots=500).result()
counts  = result.get_counts(circuit)
print(counts)
plot_histogram(counts, sort='desc')

print(counts['111'] / sum(counts.values()))