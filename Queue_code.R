library(pracma)
library(ggplot2)
library(queueing)

# Loading Data
df <- read.csv("C:\\Users\\ME\\Desktop\\Phase 3\\Data.csv")
str(df)

# Preparing Data
df[3:23]<-exp(df[3:23])
df1 <- subset(df,X>=2241)
str(df1)

df1$new_x <- df1$X-2241
df1$new_x <- mod(df1$new_x,16)
df1$new_x

#============== For Morning Sessions =========================#

morning_9_10 <- subset(df1,df1$new_x==2)
morning_9_10 <- morning_9_10[-c(1,2,24)]
mor_sums_9_10 <- rowSums(morning_9_10)

morning_10_11 <- subset(df1,df1$new_x==3)
morning_10_11 <- morning_10_11[-c(1,2,24)]
mor_sums_10_11 <- rowSums(morning_10_11)
           
mor_sums <- mor_sums_9_10+mor_sums_10_11

head(mor_sums)
jk <-data.frame(c(1:length(mor_sums)),mor_sums)
ggplot(jk)+geom_point(aes(c.1.length.mor_sums..,mor_sums))
length(mor_sums)
j<-boxplot(mor_sums)$out

x <- mor_sums
x<- x[-which(mor_sums %in% j)]
jk1<-data.frame(Index = c(1:length(x)),traffic_volume =x)
ggplot(jk1)+geom_point(aes(Index,traffic_volume))
length(x)


# Average arrival rate per 2 hour
lambda <- mean(x) 

# Service Rate per 2 hour
mu <- 16000
# Utilization rate
rho <- lambda/mu
rho

# Average arrival rate per 6 Mins
lambda1 <- mean(x)/20 

# Service Rate per 6 Mins
mu1 <- 800 
rho1 <- lambda1/mu1
rho1


avg_cust <- rho+((rho^2)/(2*(1-rho)))
avg_cust

# Average Waiting Time in Queue
avg_time <- rho/(2*mu*(1-rho))


#============== For Evening =========================#

evening_4_5 <- subset(df1,df1$new_x==9)
evening_4_5 <- evening_4_5[-c(1,2,24)]
eve_sums_4_5 <- rowSums(evening_4_5)

evening_5_6 <- subset(df1,df1$new_x==10)
evening_5_6 <- evening_5_6[-c(1,2,24)]
eve_sums_5_6 <- rowSums(evening_5_6)

eve_sums <- eve_sums_4_5+eve_sums_5_6

head(eve_sums)
jk2 <-data.frame(Index = c(1:length(eve_sums)),traffic_volume=eve_sums)
ggplot(jk2)+geom_point(aes(Index,traffic_volume))
length(eve_sums)
j1<-boxplot(eve_sums)$out

x1 <- eve_sums
x1<- x1[-which(eve_sums %in% j1)]
jk3<-data.frame(Index = c(1:length(x1)),traffic_volume=x1)
ggplot(jk3)+geom_point(aes(Index,traffic_volume))
length(x1)


# Average arrival rate per 2 hour
lambda2 <- mean(x1) 

# Service Rate per 2 hour
mu2 <- 16000

# Utilization rate
rho2 <- lambda2/mu2
rho2

# Average arrival rate per 6 Mins
lambda3 <- mean(x1)/20 

# Service Rate per 6 Mins
mu3 <- 800 
rho3 <- lambda3/mu3
rho3
