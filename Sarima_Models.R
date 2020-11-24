---
  title: "Time Series Modelling"
author: "Ashbin Jaison"
date: "March 3, 2020"
output: html_document
---
  
  # Loading required packages.
  
library(tseries)
library(dplyr)
library(tidyr)
library(forecast)
library(astsa)
library(ggplot2)



# Loading required Data.

df <- read.csv("C:\\Users\\ME\\Desktop\\Phase 3\\Data.csv")

# Loading train and test data for Aluva,Edapally, Maharajas, Mg Road and Tykoodam Stations
aluva <- ts(df$Aluva[1:3312],frequency = 16)
edapa <- ts(df$Edapally[1:3312],frequency = 16)
mahce <- ts(df$Maharajas.College[1:3324],frequency = 16)
mgrod <- ts(df$MG.road[1:3312],frequency = 16)
tykdm <- ts(df$Thykoodam[2017:3312],frequency = 16)
aluva_test <- ts(df$Aluva[3313:3328],frequency = 16)
edapa_test <- ts(df$Edapally[3313:3328],frequency = 16)
mahce_test <- ts(df$Maharajas.College[3313:3328],frequency = 16)
mgrod_test <- ts(df$MG.road[3313:3328],frequency = 16)
tykdm_test <- ts(df$Thykoodam[3313:3328],frequency = 16)



# Initial data plots

theme_set(theme_minimal())
aluva1 = data.frame(date = c(1:320),aldat = aluva[1601:1920])
edapa1 = data.frame(date = c(1:320),eddat=edapa[1601:1920])
mahce1 = data.frame(date = c(1:320),madat=mahce[1601:1920])
mgrod1 = data.frame(date = c(1:320),mgdat=mgrod[1601:1920])
tykdm1 = data.frame(date = c(1:120),tydat=tykdm[601:720])

ggplot(aluva1, aes(x = date, y = aldat)) + geom_line(color = "#E7B800", size = 1)+xlab('Date Index') + ylab('Traffic Aluva')
ggplot(mgrod1, aes(x = date, y = mgdat)) + geom_line(color = "#00AFBB", size = 1)+xlab('Date Index') + ylab('Traffic MG Road')
ggplot(mahce1, aes(x = date, y = madat)) + geom_line(color = "#E7B800", size = 1)+xlab('Date Index') + ylab('Traffic Maharajas College')
ggplot(edapa1, aes(x = date, y = eddat)) + geom_line(color = "#00AFBB", size = 1)+xlab('Date Index') + ylab('Traffic Edapally')
ggplot(tykdm1, aes(x = date, y = tydat)) + geom_line(color = "#00AFBB", size = 1)+xlab('Date Index') + ylab('Traffic Thykoodam')




# Testing for stationarity of time series

kpss.test(aluva)
kpss.test(edapa)
kpss.test(mahce)
kpss.test(mgrod)
kpss.test(tykdm)


# Plotting acf and pacf of different time series

acf(aluva,lag=100)
pacf(aluva,lag=100)
acf(edapa,lag = 100)
pacf(edapa,lag = 100)
acf(mahce,lag=100)
pacf(mahce,lag=100)
acf(mgrod,lag=100)
pacf(mgrod,lag=100)
acf(tykdm,lag=100)
pacf(tykdm,lag=100)


# Identifing parameters of sarima model for ALUVA and predicting traffic.

# AIC Matrices for getting Model for ALUVA

alAIC = matrix(NA,nrow=4,ncol=4)
for (i in 1:4){
  for (j in 1:4){
    alAIC[i,j]=arima(aluva,order=c(i-1,1,j-1),method = "ML")$aic
  }
}
alAIC

almodel = arima(aluva,order = c(2,1,2))
summary(almodel)
alres = residuals(almodel)
Box.test(alres)
acf(alres)

alAIC1 = matrix(NA,nrow = 4,ncol = 4)
for (i in 1:4){
  for (j in 1:4){
    alAIC1[i,j]=arima(alres,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
alAIC1

almodel2 = arima(alres,order = c(1,1,2))
summary(almodel2)
alres2 = residuals(almodel2)
acf(alres2)
Box.test(alres2)

# Fitting the SARIMA Model
aluvmod = sarima(aluva,2,1,2,1,1,2,16)
Box.test(resid(aluvmod$fit))

# Predicting traffic using the fitted Model 
alprediction = sarima.for(aluva,2,1,2,1,1,2,16,n.ahead = 16)
data.frame(predicted=(alprediction$pred),actual=(aluva_test))

# Converting back to original Scale
data.frame(predicted=exp(alprediction$pred),actual=exp(aluva_test))



# Identifing parameters of sarima model for Maharajas and predicting traffic.

# AIC Matrix for getting Model for MAHCE
k <- auto.arima(mahce)
k
accuracy(k)
maAIC = matrix(NA,nrow=4,ncol=4)
for (i in 1:4){
  for (j in 1:4){
    maAIC[i,j]=arima(mahce,order=c(i-1,0,j-1),method = "CSS-ML")$aic
  }
}
maAIC
mamodel = arima(mahce,order = c(2,0,2))
summary(mamodel)
mares = residuals(mamodel)
Box.test(mares)
acf(mares)

maAIC1 = matrix(NA,nrow = 4,ncol = 4)
for (i in 1:4){
  for (j in 1:4){
    maAIC1[i,j]=arima(mares,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
maAIC1

mamodel2 = arima(mares,order = c(2,1,3))
summary(mamodel2)
mares2 = residuals(mamodel2)
acf(mares2)
Box.test(mares2)
modmah = Arima(mahce,order = c(2,0,2),seasonal = list(order=c(2,1,2),16))
modmah
accuracy(modmah)
Box.test(modmah$residuals)

# Fitting the SARIMA Model
mahcmod = sarima(mahce,2,0,2,2,1,3,16)
Box.test(resid(mahcmod$fit))

# Predicting traffic using the fitted Model
maprediction = sarima.for(ts(df$Maharajas.College),2,0,2,2,1,3,16,n.ahead = 16)
data.frame(predicted=maprediction$pred,actual=mahce_test)

# Converting back to original Scale
data.frame(predicted=exp(maprediction$pred),actual=exp(mahce_test))


# Identifing parameters of sarima model for MGroad and predicting traffic.

# AIC Matrix for getting Model for MGroad
mgAIC = matrix(NA,nrow=4,ncol=4)
for (i in 1:4){
  for (j in 1:4){
    mgAIC[i,j]=arima(mgrod,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
mgAIC
mgmodel = arima(mgrod,order = c(2,1,3))
summary(mgmodel)
mgres = residuals(mgmodel)
Box.test(mgres)
acf(mgres)

mgAIC1 = matrix(NA,nrow = 4,ncol = 4)
for (i in 1:4){
  for (j in 1:4){
    mgAIC1[i,j]=arima(mgres,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
mgAIC1

mgmodel2 = arima(mgres,order = c(2,1,3))
summary(mgmodel2)
mgres2 = residuals(mgmodel2)
acf(mgres2)
Box.test(mares2)

# Fitting the SARIMA Model
mgrdmod = sarima(mgrod,2,1,3,2,1,3,16)
Box.test(resid(mgrdmod$fit))

# Predicting traffic using the fitted Model
mgprediction = sarima.for(mgrod,2,1,3,2,1,3,16,n.ahead = 16)
data.frame(predicted=mgprediction$pred,actual=mgrod_test)

# Converting back to original Scale
data.frame(predicted=exp(mgprediction$pred),actual=exp(mgrod_test))


# Identifing parameters of sarima model for Edapally and predicting traffic.

# AIC Matrix for getting Model for Edapally
edAIC = matrix(NA,nrow=4,ncol=4)
for (i in 1:4){
  for (j in 1:4){
    edAIC[i,j]=arima(edapa,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
edAIC
edmodel = arima(edapa,order = c(2,1,3))
summary(edmodel)
edres = residuals(edmodel)
Box.test(edres)
acf(edres)

edAIC1 = matrix(NA,nrow = 4,ncol = 4)
for (i in 1:4){
  for (j in 1:4){
    edAIC1[i,j]=arima(edres,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
edAIC1

edmodel2 = arima(edres,order = c(2,1,3))
summary(edmodel2)
edres2 = residuals(edmodel2)
acf(edres2)
Box.test(edres2)

# Fitting the SARIMA Model
edapmod = sarima(edapa,2,1,3,2,1,3,16)
Box.test(resid(edapmod$fit))

# Predicting traffic using the fitted Model
edprediction = sarima.for(edapa,2,1,3,2,1,3,16,n.ahead = 16)
data.frame(predicted=edprediction$pred,actual=edapa_test)

# Converting back to original Scale
data.frame(predicted=exp(edprediction$pred),actual=exp(edapa_test))


# Identifing parameters of sarima model for Thykoodam and predicting traffic.

# AIC Matrix for getting Model for Thykoodam
tyAIC = matrix(NA,nrow=4,ncol=4)
for (i in 1:4){
  for (j in 1:4){
    tyAIC[i,j]=arima(tykdm,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
tyAIC
tymodel = arima(tykdm,order = c(2,1,2))
summary(tymodel)
tyres = residuals(tymodel)
Box.test(tyres)
acf(tyres)

tyAIC1 = matrix(NA,nrow = 4,ncol = 4)
for (i in 1:4){
  for (j in 1:4){
    tyAIC1[i,j]=arima(tyres,order=c(i-1,1,j-1),method = "CSS-ML")$aic
  }
}
tyAIC1

tymodel2 = arima(tyres,order = c(1,1,2))
summary(tymodel2)
tyres2 = residuals(tymodel2)
acf(tyres2)
Box.test(tyres2)

# Fitting the SARIMA Model
tykdmod = sarima(tykdm,2,1,2,1,1,2,16)
Box.test(resid(tykdmod$fit))

# Predicting traffic using the fitted Model
typrediction = sarima.for(tykdm,2,1,2,1,1,2,16,n.ahead = 16)
data.frame(predicted=typrediction$pred,actual=tykdm_test)

# Converting back to original Scale
data.frame(predicted=exp(typrediction$pred),actual=exp(tykdm_test))
