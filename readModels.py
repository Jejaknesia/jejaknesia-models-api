import h5py

# Menentukan path file model .h5
model_path = 'Place_Recommender_1.h5'

# Membuka file model
with h5py.File(model_path, 'r') as file:
    # Memeriksa isi grup dan dataset dalam file
    print('Groups:', list(file.keys()))
    
    for group_name, group in file.items():
        print('Group:', group_name)
        print('Datasets:', list(group.keys()))
        print('---')

    # Melakukan tindakan lain yang sesuai dengan struktur file Anda
    # Misalnya, mendapatkan nilai tertentu dari dataset tertentu
