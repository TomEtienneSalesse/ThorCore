from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    return data

def classify_tests(data):
    grouped_data = data.groupby(0)
    return grouped_data

def process_cluster(data):
    data = data.drop(columns=[0,1,2,3,4])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

def get_number_of_tests(data):
    number_of_tests = max(data[0])
    return number_of_tests