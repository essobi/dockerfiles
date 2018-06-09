FROM openjdk:8-jdk-alpine  
ADD https://github.com/NickFenzan/athena-
keyserver/releases/download/0.0.1/athena-keyserver-0.0.1.jar app.jar  
ENV JAVA_OPTS=""  
ENTRYPOINT exec java $JAVA_OPTS -jar /app.jar  

