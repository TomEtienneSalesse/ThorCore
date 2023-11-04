from DataProcessing import data_import
from DataProcessing import data_processing
from DataAnalysis import statistical_analysis
from Results import generate_plots_regression
from Results import generate_plots_arima
from Results import generate_heatmap
from Results import generate_cluster_map
from DataAnalysis import data_analysis
from Results import create_pdf

# Data path
file_path = 'C:/Users/Utilisateur/Desktop/Travail/Python/ThorCore/data.xlsx'

# Import data
data = data_import.import_data(file_path)

# Get statistics
stats=statistical_analysis.statistics_data(data)

# Process data
processed_data = data_processing.preprocess_data(data)

# Classification
grouped_data = data_processing.classify_tests(processed_data)
test_number = len(grouped_data)
"""
#Correlation
correl_matrix = data_analysis.correlation_analysis(data)
generate_heatmap.plot_correlation_heatmap(correl_matrix)

# Graphs for each test with linear regression
for group_name, group_data in grouped_data:
    coef_NN, intercept_NN = data_analysis.linear_regression(group_data.iloc[:, 3].values.reshape(-1, 1), group_data.iloc[:, 4].values)
    coef_mass, intercept_mass = data_analysis.linear_regression(group_data.iloc[:, 3].values.reshape(-1, 1), group_data.iloc[:, 5].values)
    coef_energy, intercept_energy = data_analysis.linear_regression(group_data.iloc[:, 3].values.reshape(-1, 1), group_data.iloc[:, 6].values)
    generate_plots_regression.generate_plots(group_data, group_name, coef_NN, intercept_NN, coef_mass, intercept_mass, coef_energy, intercept_energy)

#Graphs for each test with linear regression with Arima model
for group_name, group_data in grouped_data:
    if len(group_data)>2:
        ARIMA_model_NN,rmse_NN,test_NN=data_analysis.arima_forecast(group_data.iloc[:, 4].values)
        ARIMA_model_mass,rmse_mass,test_mass=data_analysis.arima_forecast(group_data.iloc[:, 5].values)
        ARIMA_model_energy,rmse_energy,test_energy=data_analysis.arima_forecast(group_data.iloc[:, 6].values)
        coef_NN, intercept_NN = data_analysis.linear_regression(group_data.iloc[:, 3].values.reshape(-1, 1), group_data.iloc[:, 4].values)
        coef_mass, intercept_mass = data_analysis.linear_regression(group_data.iloc[:, 3].values.reshape(-1, 1), group_data.iloc[:, 5].values)
        coef_energy, intercept_energy = data_analysis.linear_regression(group_data.iloc[:, 3].values.reshape(-1, 1), group_data.iloc[:, 6].values)
        generate_plots_arima.generate_plots(group_data, group_name, coef_NN, intercept_NN, coef_mass, intercept_mass, coef_energy, intercept_energy,ARIMA_model_NN,rmse_NN,ARIMA_model_mass,rmse_mass,ARIMA_model_energy,rmse_energy,test_NN,test_mass,test_energy)

#data procecing for cluster analysis
scaled_data = data_processing.process_cluster(data)
shape = data_analysis.ideal_cluster_number(scaled_data)
number_of_tests = data_processing.get_number_of_tests(data)
#ideal_number_of_clusters = shape.index(max(shape)) + 2
clusters, clusters_centers =  data_analysis.apply_kmeans(scaled_data, number_of_tests)
generate_cluster_map.generate_cluster_plot(scaled_data, clusters, clusters_centers)"""

create_pdf.generate_report(stats, test_number)
create_pdf.images(test_number)