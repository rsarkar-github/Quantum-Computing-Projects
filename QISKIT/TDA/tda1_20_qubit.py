# The simplicial complex is as follows:
# Vertices: 0, 1, 2
# Simplicial complex: {{0}, {1}, {2}, {0, 1}}

# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, register
import Qconfig_20_qubit as Qconfig

# Set your API Token.
QX_TOKEN = Qconfig.APItoken
QX_URL = Qconfig.config["url"]
QX_HUB = Qconfig.config["hub"]
QX_GROUP = Qconfig.config["group"]
QX_PROJECT = Qconfig.config["project"]

# Authenticate with the IBM Q API in order to use online devices.
register(QX_TOKEN, QX_URL, hub=QX_HUB, group=QX_GROUP, project=QX_PROJECT)

# Create a Quantum Circuit with 5 qubits
q = QuantumRegister(5)
c = ClassicalRegister(5)
qc = QuantumCircuit(q, c)

# Build the circuit
qc.x(q[2])
qc.x(q[1])
qc.cx(q[1], q[0])
qc.measure(q[3], c[3])
# qc.cx(q[2], q[4])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])
qc.measure(q[4], c[4])

# Compile and run the Quantum circuit
shots = 1024
backend_options = ["local_qasm_simulator", "ibmq_20_tokyo"]
use_backend = backend_options[1]
job_sim = execute(qc, use_backend, shots=shots)
sim_result = job_sim.result()

# Analyze the results
counts = sim_result.get_counts(qc)
print("simulation: ", sim_result)
print("counts: ", counts)
keys = counts.keys()
cnt = 0
for item in keys:
    if item[0] == "0":
        cnt += counts[item]

prob = cnt / shots
print("Probability of getting eigenvalue 0 = ", prob)

# Calculation of Betti numbers
