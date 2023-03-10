from qiskit import QuantumCircuit, Aer, assemble
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc_ha = QuantumCircuit(4,2)
# encode inputs in qubits 0 and 1
qc_ha.x(0) # For a=0, remove the this line. For a=1, leave it.
qc_ha.x(1) # For b=0, remove the this line. For b=1, leave it.
qc_ha.barrier()
# use cnots to write the XOR of the inputs on qubit 2
qc_ha.cx(0,2)
qc_ha.cx(1,2)
# use ccx to write the AND of the inputs on qubit 3
qc_ha.ccx(0,1,3)
qc_ha.barrier()
# extract outputs
qc_ha.measure(2,0) # extract XOR value
qc_ha.measure(3,1) # extract AND value

qc_ha.draw()


qobj = assemble(qc_ha)
sim = Aer.get_backend('aer_simulator')
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts)
plt.savefig('./pics/o_O.png', bbox_inches='tight', pad_inches=1)

