import os

# Change this to the full path where your DL1 folder is located
base_dir = "C:/Users/ACT-AIDS-T3-23/Desktop/DL1/Dataset"

train_parasite_dir = os.path.join(base_dir, "Train/Parasite")
train_uninfected_dir = os.path.join(base_dir, "Train/Uninfected")
test_parasite_dir = os.path.join(base_dir, "Test/Parasite")
test_uninfected_dir = os.path.join(base_dir, "Test/Uninfected")

def count_images(folder):
    return len(os.listdir(folder))

print("Train Parasite images:", count_images(train_parasite_dir))
print("Train Uninfected images:", count_images(train_uninfected_dir))
print("Test Parasite images:", count_images(test_parasite_dir))
print("Test Uninfected images:", count_images(test_uninfected_dir))
