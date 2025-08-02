### pipeline to train a model data scince lifecycle
# 1. Data Collection
# 2. Data Preprocessing
# 3. Data Exploration
# 4. Data Visualization
# 5. Model Training
# 6. Model Evaluation
# 7. Model Deployment
# 8. Model Monitoring
# 9. Model Maintenance
# 10. Model Retraining
# 11. Model Versioning
# 12. Model Explainability
# 13. Model Interpretability
# 14. Model Debugging
# 15. Model Optimization
# 16. Model Tuning
# 17. Model Scaling
# 18. Model Serving
# 19. Model Integration
# 20. Model Management
# 21. Model Governance
# 22. Model Security
# 23. Model Compliance
# 24. Model Auditing
# 25. Model Documentation
# 26. Model Collaboration
# 27. Model Reproducibility
# 28. Model Experimentation
# 29. Model Tracking


# inspect dataset
# data cleaning
# EDA such as correlation, distribution, hypothesis testing, etc.
# univariate and multivariate analysis
# feature engineering such as scaling, encoding, etc. feature selection, etc.
# feature extraction, etc. feature generation, etc.
import numpy as np
import pandas as pd

# missing values
def handle_missing_values(df):
    # Fill missing values with the mean of the column
    return df.fillna(df.mean())

# delete rows with missing values if necessary missing values < 1%
def drop_missing_values(df):
    return df.dropna()

# implute missing values with a specific value
def impute_missing_values(df, value):
    return df.fillna(value)

# impute missing values that depend on other columns
def impute_dependent_missing_values(df, column, dependent_column):
    df[column] = df[column].fillna(df[dependent_column].mean())
    return df

# impute missing values that depend in some cells in other columns
def impute_conditional_missing_values(df, condition_column, value_column):
    df[value_column] = np.where(df[condition_column].isnull(), df[value_column].mean(), df[value_column])
    return df

# if the data is sequential, we can use forward fill or backward fill
def forward_fill_missing_values(df):
    return df.ffill()

def backward_fill_missing_values(df):
    return df.bfill()

# central tendency imputation
def central_tendency_imputation(df, column):
    mean_value = df[column].mean()
    median_value = df[column].median()
    mode_value = df[column].mode()[0]  # mode returns a Series
    df[column] = df[column].fillna(mean_value)  # or median_value or mode_value
    return df

# if the missing data is from 5 to 20% of the dataset, we can use interpolation
def interpolate_missing_values(df):
    return df.interpolate()

# iterative imputation #
def iterative_imputation(df):
    pass



# Example usage
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})
df = handle_missing_values(df)

print(df.head())








