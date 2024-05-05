from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from numpy import pi

qreg_q = QuantumRegister(24, 'q')
creg_c = ClassicalRegister(8, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])

circuit.x(qreg_q[1])
circuit.h(qreg_q[2])

circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.cswap(qreg_q[0], qreg_q[1], qreg_q[3])
circuit.cswap(qreg_q[0], qreg_q[2], qreg_q[2])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])

circuit.h(qreg[4])

