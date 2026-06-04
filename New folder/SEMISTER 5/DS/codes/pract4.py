import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelBinarizer 
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
# Define the data
data = {
     'Product': ['Apple_Juice', 'Banana_Smoothie', 'Apple_Juice', 'Banana_Smoothie', 'Kiwi_Parfait', 'Mango_Chutney', 'Pineapple_Sorbet', 'Strawberry_Yogurt', 'Blueberry_Pie', 'Cherry_Salsa'],
    'Category': ['Apple', 'Banana', 'Orange', 'Grape', 'Kiwi', 'Mango', 'Pineapple', 'Strawberry', 'Blueberry', 'Cherry'],
    'Sales': [1200, 1700, 2200, 1400, 2000, 1000, 1500, 1800, 1300, 1600],
    'Cost': [600, 850, 1100, 700, 1000, 500, 750, 900, 650, 800],
    'Profit': [600, 850, 1100, 700, 1000, 500, 750, 900, 650, 800]
}
# Create a DataFrame
df = pd.DataFrame(data)
# Display the original dataset
print("Original Dataset:")
print(df)

# Step 2: Feature Dummification
# creating a copy of the 
# original data frame 
df1 = df.copy() 
  
# creating an object  
# of the LabelBinarizer 
label_binarizer = LabelBinarizer() 
  
# fitting the column  
# Product to LabelBinarizer 
label_binarizer_output = label_binarizer.fit_transform( df1['Product']) 
  
# creating a data frame from the object 
result_df = pd.DataFrame(label_binarizer_output, 
                         columns = label_binarizer.classes_)
print("\nDataset after Feature Dummification:") 
print(result_df) 
