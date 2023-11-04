from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def linear_regression(x, y):
    model = LinearRegression()
    model.fit(x, y)
    return model.coef_, model.intercept_

def arima_model(series):
    model = ARIMA(series, order=(5,1,0))
    print(series)
    model_fit = model.fit()
    return model_fit

def arima_forecast(series):
    X = series
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(5,1,0))
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
    root_mean_squared_error = sqrt(mean_squared_error(test, predictions))
    return predictions,root_mean_squared_error,test

def correlation_analysis(data):
    correlation_matrix = data.corr()
    return correlation_matrix

def ideal_cluster_number(scaled_data):
    shape_scores = []
    for i in range(2, 12):
        kmeans = KMeans(n_clusters=i, random_state=0)
        clusters = kmeans.fit_predict(scaled_data)
        shape_avg = silhouette_score(scaled_data, clusters)
        shape_scores.append(shape_avg)
        return shape_scores
    
def apply_kmeans(scaled_data, ideal_number_of_clusters):
    kmeans = KMeans(n_clusters=ideal_number_of_clusters, random_state=0)
    clusters = kmeans.fit_predict(scaled_data)
    cluster_centers = kmeans.cluster_centers_
    return clusters, cluster_centers