import numpy as np
import matplotlib.pyplot as plt

def plot_correlation_heatmap(correl_matrix):
    plt.figure(figsize=(10, 5))
    correl_matrix = np.array(correl_matrix)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.matshow(np.round(correl_matrix, 2), cmap='viridis')

    for i in range(correl_matrix.shape[0]):
        for j in range(correl_matrix.shape[1]):
            ax.text(j, i, str(round(correl_matrix[i, j],4)), va='center', ha='center', color='black', fontsize=10)

    attributes = ['Test Number', 'Neutron Flux', 'Initial Mass', 'Time', 'Number of Nuclei', 'Mass', 'Energy']
    ax.set_xticks(np.arange(len(attributes)))
    ax.set_yticks(np.arange(len(attributes)))
    ax.set_xticklabels(attributes)
    ax.set_yticklabels(attributes)
    plt.xticks(rotation=45)
    plt.savefig(f'/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/correlation_matrix.png')