import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datasets = pd.read_excel('NVASA.xlsx')
X = datasets.iloc[:, :8].values
Y = datasets.iloc[:, 8].values
datasets.head()

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.3, random_state = 42)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 100, random_state = 42)
regressor.fit(X_Train, Y_Train)

Y_Pred = regressor.predict(X_Test)
print("The predicted values of test_data are:\n", Y_Pred)
print('\n')
print("The accuracy of the model is:")
print(regressor.score(X_Test, Y_Test))

from sklearn.feature_selection import SelectFromModel
ranking = regressor.feature_importances_
features = datasets.columns
features = features[0:8]
feature_ranking = dict(zip(features,ranking))
print("The rankings of different features are: ")
print(feature_ranking)
feat_importances = pd.Series(ranking, index=features)
feat_importances.nlargest(8).plot(kind='barh')

print("Enter the input features:")
print("Select the polymer type(Yes-1, No-0)")
a = input("'PS-b-PEO': ")
b = input("'PS-b-P2VP': ")
c = input("'PS-b-P4VP': ")
d = input("Casting Solvent Type(Toluene-0, THF-1): ")
e = input("'Mol_wt(kDa)': ")
f = input("'Vf(minor)': ")
g = input("'Concentration(mg/ml)': ")
h = input("'Swell_ratio': ")
prediction = regressor.predict([[a, b, c, d, e, f, g, h]])
print("Predicted Value(FWHM):", prediction[0])

plt.figure(figsize=(10,10))
plt.scatter(Y_Test, Y_Pred, c='red')

p1 = max(max(Y_Pred), max(Y_Test))
p2 = min(min(Y_Pred), min(Y_Test))
plt.plot([p1, p2], [p1, p2], 'b-')
plt.xlabel('Measured Values', fontsize=15)
plt.ylabel('Predicted Values', fontsize=15)
plt.axis('equal')
#plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()

from mpl_toolkits import mplot3d

y = datasets['MW (kDa)'].to_numpy()
x = datasets['Swell Ratio'].to_numpy()
z = datasets['FWHM (q)'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(x, y, z, linewidth=0, antialiased=False)

ax.set_xlabel('SR')
ax.set_ylabel('MW')
ax.set_zlabel('FWHM')
#plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()


