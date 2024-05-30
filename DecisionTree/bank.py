import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import pickle

# Load dataset
data = pd.read_csv('data_kredit.csv')

# Handle missing values
data['Constrain'].fillna('No', inplace=True)

# Preprocess data
le_character = LabelEncoder()
le_condition = LabelEncoder()
le_constrain = LabelEncoder()

data['Character'] = le_character.fit_transform(data['Character'])
data['Condition_of_Economic'] = le_condition.fit_transform(data['Condition_of_Economic'])
data['Constrain'] = le_constrain.fit_transform(data['Constrain'])

# Debug: Print unique values to ensure proper encoding
print("Character unique values:", le_character.classes_)
print("Condition_of_Economic unique values:", le_condition.classes_)
print("Constrain unique values:", le_constrain.classes_)

# Convert 'Capacity' column to numeric
capacity_mapping = {'High': 1, 'Medium': 2, 'Low': 3}
data['Capacity'] = data['Capacity'].map(capacity_mapping)

# Convert 'Approved' column to binary
data['Approved'] = data['Approved'].apply(lambda x: 1 if x == 'Yes' else 0)

# Check if all columns are numeric now
print(data.dtypes)

X = data.drop('Approved', axis=1)
y = data['Approved']

# Check class distribution
print("Class distribution in y:", y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Train model with CART
model = DecisionTreeClassifier(criterion='gini')  # or 'entropy'
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=1))

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Function for making predictions
def predict_credit(character, capacity, capital, collateral, condition_of_economic, constrain):
    # Check if inputs are valid
    if character not in le_character.classes_:
        return f"Error: Unknown character value '{character}'"
    if condition_of_economic not in le_condition.classes_:
        return f"Error: Unknown condition_of_economic value '{condition_of_economic}'"
    if constrain not in le_constrain.classes_:
        return f"Error: Unknown constrain value '{constrain}'"
    if capacity not in capacity_mapping:
        return f"Error: Unknown capacity value '{capacity}'"
    
    # Encode inputs
    character = le_character.transform([character])[0]
    condition_of_economic = le_condition.transform([condition_of_economic])[0]
    constrain = le_constrain.transform([constrain])[0]
    
    # Map capacity
    capacity = capacity_mapping[capacity]
    
    # Create a DataFrame for the inputs
    input_data = pd.DataFrame([[character, capacity, capital, collateral, condition_of_economic, constrain]], 
                              columns=['Character', 'Capacity', 'Capital', 'Collateral', 'Condition_of_Economic', 'Constrain'])
    
    # Load the model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # Make prediction
    prediction = model.predict(input_data)
    result = 'Approved' if prediction[0] == 1 else 'Not Approved'
    return result

# Example usage
character = 'Good'
capacity = 'Low'
capital = 60000
collateral = 150000
condition_of_economic = 'Unstable'
constrain = 'No'  # Changed 'None' to 'No' to match the dataset

# Debug: Print inputs to ensure correctness
print(f"Inputs: Character={character}, Capacity={capacity}, Capital={capital}, Collateral={collateral}, Condition_of_Economic={condition_of_economic}, Constrain={constrain}")

print("Prediction Result:", predict_credit(character, capacity, capital, collateral, condition_of_economic, constrain))
