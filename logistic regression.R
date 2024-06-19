#Logistic Regression

mydata <- read.csv(file.choose(), header = T)
str(mydata) #summary of data
mydata$admit <- as.factor(mydata$admit)
mydata$rank   <- as.factor(mydata$rank)

str(mydata)

xtabs(~admit+rank, data = mydata)

#partition data

set.seed(1234)
ind <- sample(2,nrow(mydata), replace= T, prob = c(0.8,0.2))
train <- mydata[ind ==1,]
test <- mydata[ind==2,]

#logistic regression model
mymodel <- glm(admit~ gre+gpa+rank, data=train, family = "binomial")
summary(mymodel)

#for any variable more stars we have more will be that variable significant
#example = for gre we have p_value = 0.18 which is greater than 5 percent level of significance hence not significant
#for gpa its significant as p-value is less than 5% level of significance
#we can drop the insignificant variables from model
mymodel <- glm(admit~ gpa+rank, data=train, family = "binomial")
summary(mymodel) #fropping gre

#prediction

p1 <- predict(mymodel, train, type = "response")
head(p1)
head(train)
#1st applicant is rejcted as he had only 28% chance of getting selected with gre of 380 and gpa of 3,61
y <- -4.7270 + (1.3753*3.61)+(1*-1.1645)
head(train)

#probablity that 3rd applicamt will be selected is 68%
#Probablity that 1st applicant is selected is 28%
head(p1)

