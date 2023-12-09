import pandas as pd
import numpy as np
df1 = pd.read_csv("dataset-1.csv")
df1

df2 = pd.read_csv("dataset-2.csv")
df2

#python task1 - 1
def generate_car_matrix(dataset):
    # Write your logic here
    car_matrix = df1.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    return car_matrix

dataset_path = 'dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)



#python task1 - 2
def get_type_count(dataset):     
    # Write your logic here
    conditions = [
        (df1['car'] <= 15),
        (df1['car'] > 15) & (df1['car'] <= 25),
        (df1['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df1['car_type'] = np.select(conditions, choices)
    type_count = df1['car_type'].value_counts().to_dict()
    type_count = {k: type_count[k] for k in sorted(type_count)}

    return type_count

dataset_path = 'dataset-1.csv'
result_type_count = get_type_count(dataset_path)
print(result_type_count)



#python task1 - 3
def get_bus_indexes(dataset):    
    # Write your logic here
    mean_bus_value = df1['bus'].mean()
    bus_indexes = df1[df1['bus'] > 2 * mean_bus_value].index.tolist()
    bus_indexes.sort()

    return bus_indexes

dataset_path = 'dataset-1.csv'
result_bus_indexes = get_bus_indexes(dataset_path)
print(result_bus_indexes)



#python task1 - 4
def filter_routes(dataset):
    # Write your logic here
    route_avg_truck = df1.groupby('route')['truck'].mean()
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    selected_routes.sort()

    return selected_routes

dataset_path = 'dataset-1.csv'
result_routes = filter_routes(dataset_path)
print(result_routes)



#python task1 - 5
def multiply_matrix(input_matrix):   
    # Write your logic here
    modified_matrix = input_matrix.copy()
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

result_matrix = generate_car_matrix('dataset-1.csv')
modified_result = multiply_matrix(result_matrix)
print(modified_result)



#python task1 - 6
def time_check(dataset):
    # Write your logic here
    df2['start_datetime'] = pd.to_datetime(df2['startDay'] + ' ' + df2['startTime'], errors='coerce')
    df2['end_datetime'] = pd.to_datetime(df2['endDay'] + ' ' + df2['endTime'], errors='coerce')
    time_completeness = df2.groupby(['id', 'id_2']).apply(lambda x: check_timestamps(x)).reset_index(drop=True)

    return time_completeness

def check_timestamps(group):
    min_datetime = group['start_datetime'].min()
    max_datetime = group['end_datetime'].max()

    if pd.notna(min_datetime) and pd.notna(max_datetime):
        correct_range = (min_datetime.time() == pd.Timestamp('00:00:00').time()) and \
                        (max_datetime.time() == pd.Timestamp('23:59:59').time()) and \
                        (min_datetime.day_name() == 'Monday') and \
                        (max_datetime.day_name() == 'Sunday')
    else:
        correct_range = False

    return not correct_range

dataset_path = 'dataset-2.csv'
result_completeness = time_check(dataset_path)
print(result_completeness)


