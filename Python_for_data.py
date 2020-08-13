import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
print("done")

file_name='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/coursera/project/kc_house_data_NaN.csv'
df=pd.read_csv(file_name)
df.drop(["id", "Unnamed: 0"], axis=1, inplace=True)
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)
mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

print("R^2 for linear model")
RigeModel=Ridge(alpha=0.1)
RigeModel.fit(x_train, y_train)
print(RigeModel.score(x_test, y_test))

print("R^2 for deg 2 polynomial")
pr=PolynomialFeatures(degree=2)

#transform x
x_train_pr=pr.fit_transform(x_train)
x_test_pr=pr.fit_transform(x_test)

RigeModel2 = Ridge(alpha=0.1)
RigeModel2.fit(x_train_pr, y_train)
print(RigeModel2.score(x_test_pr, y_test))





