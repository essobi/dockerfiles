# BuzzleEureka Service  
#  
# This dockerfile downloads the BuzzleEureka Service,  
# downloads Maven Tools, compiles BuzzleEureka and starts it.  
# Clone BuzzleEureka Service  
FROM alpine/git AS clone  
WORKDIR /app  
RUN git clone https://github.com/BuzzlePlatform/BuzzleEureka.git && cd
BuzzleEureka  
  
# Install Maven Tools  
FROM maven:3.5-jdk-8-alpine as build  
WORKDIR /app  
COPY \--from=clone /app/BuzzleEureka /app  
RUN mvn install  
  
# Install Java 8  
FROM openjdk:8-jre-alpine as start  
WORKDIR /app  
COPY \--from=build /app/target/BuzzleEureka.jar /app  
EXPOSE 8761  
CMD exec java -jar BuzzleEureka.jar  

