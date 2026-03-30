import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=5)

@qml.qnode(dev)
def swap_test():
    ancilla = 0
    q1, q2, q3, q4 = 1, 2, 3, 4
    qml.Hadamard(wires=q1)
    qml.RX(np.pi/3, wires=q2)
    qml.Hadamard(wires=q3)
    qml.Hadamard(wires=q4)
    qml.Hadamard(wires=ancilla)
    qml.CSWAP(wires=[ancilla, q1, q3])
    qml.CSWAP(wires=[ancilla, q2, q4])
    qml.Hadamard(wires=ancilla)
    return qml.probs(wires=ancilla)

if __name__ == "__main__":
    result = swap_test()
    fig, ax = qml.draw_mpl(swap_test)()
    fig.savefig("task2_circuit.png", dpi=300, bbox_inches="tight")
    plt.show()
    print(result)
    plt.figure()
    plt.bar([0, 1], result)
    plt.xticks([0, 1])
    plt.xlabel("Measurement Outcome")
    plt.ylabel("Probability")
    plt.title("Swap Test Result")
    plt.savefig("task2_result.png", dpi=300, bbox_inches="tight")
    plt.show()
