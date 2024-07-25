# %%
print("Time series and ML")

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import StandardScaler
from scipy import stats

# %%
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

# %% [markdown]
# The code below uses linregress function from stats module. The linregress function returns 5 values slope, intercept, r, the p-value an std_error.
# 
# myfunc that takes a single value x and returns x*slope + intercept
# 
# map function applies myfunc to each element of x dataset. resulting list is stored in mymodel variable.
# mymodel contains predicted values of y bases on linear regression model not original y values

# %%
slope, intercept, r, p, std_error = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()

# %%
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

# %% [markdown]
# r value is -0.75 which is close to -1 so it indicates a good negative relationship between x and y

# %%
speed = myfunc(10)
print(speed)

# %% [markdown]
# in above code we predicted the speed of a 10 year old car using myfunc and linear regression model. above model is a good fit. If r value is far from 1 or -1 then it indicates model is a bad fit.

# %% [markdown]
# Now let us take  alook at polynmial regression which comes to play when our dataset will not fit a linear regression i.e a staraight line through all data points.

# %%
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x, y)
plt.show()

# %% [markdown]
# x represents hours of the day and y represnets speed pf car.
# The graph above shows the speed of a car at different times of the day.

# %%
mymodel = np.poly1d(np.polyfit(x,y,3))
print(mymodel)
myline = np.linspace(1,22,100)

plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()

# %% [markdown]
# above is example of polynomial regression: (-0.03x^3 + 1.34x^2 - 15.54x +113.8)
# numpy.polyfit(x, y, 3) performs the polynomial regression analysis and returns the coefficients of a degree 3 polynomial.
# numpy.linspace(1, 22, 100) generates a range of 100 evenly spaced values from 1 to 22.
# 

# %%
from sklearn.metrics import r2_score
print(r2_score(y,mymodel(x)))

# %% [markdown]
# In case of linear regression we used r (correlation) to test how good or bad model fits . But in case of polynomial regression we check this through R-squared i.e coeff of determination.
# a result of 0.94 shows that there is good relationship and model is  a goodfit. if there is no relationship among variables then its not possible to predict fucture values.

# %%
df = pd.read_csv(r"C:\Users\Thinkpad\Downloads\data.csv")
df.head(10)

# %%
df.Volume.mean()
df.Volume.median()
df.Volume.quantile(0.25)
df.Volume.quantile(0.75)
df.Volume.max()
df.Volume.min()

# %%
X = df[['Weight', 'Volume']]
y = df['CO2']

# %%
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X,y)


# %% [markdown]
# fit() that takes the independent and dependent values as parameters and fills the regression object with data that describes the relationship

# %%
regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

# %% [markdown]
# Now lets start with trainig and testing models

# %%
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

# %% [markdown]
# x is an array of 100 random numbers with a mean of 3 and a standard deviation of 1.
# y is an array of 100 random numbers with a mean of 150 and a standard deviation of 40, divided by x. This creates a non-linear relationship between x and y.

# %%
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# %% [markdown]
# To measure if the model is good enough, we can use a method called Train/Test.
# we train the model using training set and we test the model using testing set.
# 
# train means craeting the model while test means tsting the accuracy of model

# %%
plt.scatter(train_x, train_y)
plt.show()

# %%
plt.scatter(test_x, test_y)
plt.show()

# %%
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

myline = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# %%
r2 = r2_score(train_y, mymodel(train_x))

print(r2)

# %%
r2 = r2_score(test_y, mymodel(test_x))

print(r2)

# %%
print("Lets see what is a Confusion Matrix and logistic regression is")

# %%



