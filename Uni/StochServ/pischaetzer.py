import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


if __name__ == "__main__":
    # Parametern für die Simulation
    N = 100
    L = 1_000

    # Zufallsngenerator
    rng = np.random.default_rng()

    # Array für die Ergebnisse
    M = np.zeros(L)

    # Simulation
    for k in range(0, L):
        # Zufällige Punkte in [-1,1] x [-1,1]
        X = rng.uniform(low=-1.0, high=1.0, size=(N, 2))
        # Punkte im Einheitskreis
        Z = np.linalg.norm(X, axis=1) <= 1
        # Monte-Carlo-Schätzer
        M[k] = Z.mean()

    # Ausgabe
    print(f"π ≈ {M.mean()*4}")

    sns.set_theme()

    # Visualisierung
    fig, ax = plt.subplots()
    plot = plt.plot(X[:, 0], X[:, 1], "o")
    circle = Circle((0, 0), 1, fill=False, color="b")
    ax.add_patch(circle)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    # Histogramm
    sns.histplot(M, bins=np.linspace(0, 1, N), stat="probability", kde=True)
    plt.show()

