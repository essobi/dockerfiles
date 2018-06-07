FROM java:jdk-alpine  
MAINTAINER Gianluca Tomasino <gianluca.tomasino@gmail.com>  
  
RUN apk add --update bash libstdc++ && rm /var/cache/apk/*  
  
ENV JDBC_DATABASE_URL
'jdbc:mysql://database/learningbox?user=learningbox&password=learningbox'  
ENV LEARNINGBOX_VERSION 0.1.1  
EXPOSE 8080  
ADD
https://github.com/gianlucatomasino/learningbox/releases/download/$LEARNINGBOX_VERSION/learningbox.jar
/app/  
WORKDIR /app  
  
ENTRYPOINT ["java", "-jar", "learningbox.jar"]

