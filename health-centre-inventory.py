patients = {
    "P001": {
        "name": "Patient A",
        "age": 24,
        "condition": "Malaria"
    },
    "P002": {
        "name": "Patient B",
        "age": 45,
        "condition": "Hypertension"
    }
}

print(patients)
patient_id = input("Enter Patient ID: \n").strip().upper()

if patient_id in patients:
    print(patients[patient_id])
else:
    print("Patient not found!")

inventory = {
    "Paracetamol": 50,
    "Amoxicillin": 8,
    "Artemether": 25
}

print("\n--- MEDICINE INVENTORY ---")
for medicine, stock in inventory.items():
    if stock < 10:
        print(medicine, ":", stock, "- LOW STOCK WARNING!")
    else:
        print(medicine, ":", stock, "- Sufficient")
