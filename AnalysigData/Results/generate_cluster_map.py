import matplotlib.pyplot as plt

def generate_cluster_plot(scaled_data, clusters, cluster_centers):
    plt.figure(figsize=(10, 5))
    plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=clusters, cmap='viridis')
    if cluster_centers is not None:
        plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=300, c='red', label='Centroids')
    plt.xlabel('Remaining mass (scaled)')
    plt.ylabel('Energy produced (scaled)')
    plt.legend()
    plt.savefig(f'/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/cluster_map.png')