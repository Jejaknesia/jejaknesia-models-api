import h5py
model_path = 'converted_model.tflite'

with h5py.File(model_path, 'r') as file:
    print('Groups:', list(file.keys()))
    
    for group_name, group in file.items():
        print('Group:', group_name)
        print('Datasets:', list(group.keys()))
        print('---')
