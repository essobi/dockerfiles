FROM java:8-jdk  
MAINTAINER Tim Redding  
ADD gradlew .  
ADD gradle gradle/  
RUN ./gradlew  
RUN rm -rf gradlew; rm -rf gradle  

