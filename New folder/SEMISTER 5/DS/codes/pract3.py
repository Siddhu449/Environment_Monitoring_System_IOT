import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data = {
     'Product': ['Apple_Juice', 'Banana_Smoothie', 'Orange_Jam', 'Grape_Jelly', 'Kiwi_Parfait',
                 'Mango_Chutney', 'Pineapple_Sorbet', 'Strawberry_Yogurt', 'Blueberry_Pie', 'Cherry_Salsa'],
    'Category': ['Apple', 'Banana', 'Orange', 'Grape', 'Kiwi',
                 'Mango', 'Pineapple', 'Strawberry', 'Blueberry', 'Cherry'],
    'Sales': [1200, 1700, 2200, 1400, 2000, 1000, 1500, 1800, 1300, 1600],
    'Cost': [600, 850, 1100, 700, 1000, 500, 750, 900, 650, 800],
    'Profit': [600, 850, 1100, 700, 1000, 500, 750, 900, 650, 800]
}

df = pd.DataFrame(data)

print("="*20, "Original Dataset:", "="*20)
print(df)

numeric_columns = ['Sales', 'Cost', 'Profit']

scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(scaler_standard.fit_transform(df[numeric_columns]), columns=[f"{col}_std" for col in numeric_columns])

scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(scaler_minmax.fit_transform(df[numeric_columns]), columns=[f"{col}_norm" for col in numeric_columns])

df_scaled_combined = pd.concat([df_standardized, df_normalized, df[['Product', 'Category']]], axis=1)

print("\n", "="*20, "Dataset after Standardization and Normalization:", "="*20)
print(df_scaled_combined)

categorical_columns = ['Product', 'Category']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first'), categorical_columns)  
    ],
    remainder='passthrough'
)

df_dummified = pd.DataFrame(preprocessor.fit_transform(df_scaled_combined))

print("\n", "="*20, "Final Dataset after Feature Dummification:", "="*20)
print(df_dummified)
