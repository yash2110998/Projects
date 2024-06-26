# Lib
library(faraway)

# Read Data
vehicle <- read.csv('https://raw.githubusercontent.com/bkrai/R-files-from-YouTube/main/vehicle.csv')
vehicle <- read.csv(file.choose(), header = T)
summary(vehicle)

# Data Review and Data Preparation
vehicle$lh[vehicle$lh==0] <- mean(vehicle$lh)
vehicle$lc[vehicle$lc==0] <- mean(vehicle$lc)

# Data Partition
set.seed(1234)
ind <- sample(2, nrow(vehicle), 
              replace = TRUE, 
              prob = c(0.7, 0.3))
training <- vehicle[ind==1,]
testing <- vehicle[ind==2,]

# Multiple Linear Regression
model <- lm(lc~lh, data=training)
plot(lc~lh, training)
abline(model, col = "blue")

# Model Diagnostics
par(mfrow=c(2,2))
plot(model)

# Prediction
pred <- predict(model, testing)
predict(model, data.frame(lh=10))

# Variance Inflation Factor (VIF)
newmodel <- lm(lc~lh+Mileage+mc+fm, data = training)
vif(newmodel)
