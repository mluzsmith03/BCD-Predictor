
from import_data import generate_data, import_data


# Test the generator to make sure it works correctly.
print("Testing generator...")

generator = generate_data("wdbc.data")

first_tumor = next(generator)
# Test the import function to make sure it works correctly.
print("\nTesting import_data...")

print("First tumor:", first_tumor)


data = import_data("wdbc.data")
# Looping through all of the data and printing it out to make sure it was imported correctly.
for tumor_id, tumor_data in data.items():
    print(f"Tumor ID: {tumor_id}, Data: {tumor_data}")


# Check that the data was imported correctly
if len(data) == 569:
    print("\nThe dataset was imported successfully!")

else:
    print("\nError something may be wrong with the dataset/Incorrect dataset.")
