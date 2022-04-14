import pandas as pd

def data_loader(data_path):
    
    file_name = data_path.split('/')[-1]
    data = pd.read_csv(data_path)
    print(f'READING FILE.. {file_name} \n')
    
    print(f'[shape]: {data.shape} \n')
    print(f'[column]: {data.columns.values} \n')
    print(f'[example]: {data.T.iloc[:, 0:1]} \n')
    
    return data