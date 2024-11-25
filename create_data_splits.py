import os
import random

# Paths for malware and goodware directories
malware_dir = '/scratch/users/mbenali/download_apk/100k_download/images/malware'
goodware_dir = '/scratch/users/mbenali/download_apk/100k_download/images/goodware'

# Number of experiments
num_experiments = 10

# Split ratios
train_ratio = 0.8
test_ratio = 0.1
valid_ratio = 0.1

# Function to get all file paths from a directory
def get_file_paths(directory, label):
    return [f"{label}/{file}" for file in os.listdir(directory) if file.endswith(".png")]

# Function to split dataset into train, test, and validation sets
def split_dataset(files):
    random.shuffle(files)
    total = len(files)
    train_end = int(total * train_ratio)
    test_end = train_end + int(total * test_ratio)
    
    train_files = files[:train_end]
    test_files = files[train_end:test_end]
    valid_files = files[test_end:]
    
    return train_files, test_files, valid_files

# Get all malware and goodware files
malware_files = get_file_paths(malware_dir, "malware")
goodware_files = get_file_paths(goodware_dir, "goodware")

# Repeat the process for 10 experiments
for experiment in range(1, num_experiments + 1):
    # Combine and split the datasets
    all_files = malware_files + goodware_files
    print(f"There are {len(all_files)} files.")
    train, test, valid = split_dataset(all_files)
    
    # Write the splits to files
    with open(f"data_splits/train{experiment}.txt", "w") as train_file:
        train_file.write("\n".join(train))
    
    with open(f"data_splits/test{experiment}.txt", "w") as test_file:
        test_file.write("\n".join(test))
    
    with open(f"data_splits/valid{experiment}.txt", "w") as valid_file:
        valid_file.write("\n".join(valid))

print("Datasets for 10 experiments have been created.")
