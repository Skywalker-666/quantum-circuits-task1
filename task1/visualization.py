import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=5)

@qml.qnode(dev)
def circuit_task1():
    for i in range(5):
        qml.Hadamard(wires=i)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 3])
    qml.CNOT(wires=[3, 4])
    qml.SWAP(wires=[0, 4])
    qml.RX(np.pi/2, wires=2)
    return qml.state()

if __name__ == "__main__":
    state = circuit_task1()
    probs = np.abs(state) ** 2
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(probs)), probs)
    plt.title("State Probabilities (Task 1)")
    plt.xlabel("Basis State")
    plt.ylabel("Probability")
    plt.savefig("task1_probabilities.png", dpi=300, bbox_inches="tight")
    plt.show()
