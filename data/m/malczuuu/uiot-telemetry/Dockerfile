# Stage 1: build application  
FROM openjdk:8-jdk as builder  
  
RUN mkdir /app  
ADD . /app  
  
RUN cd /app/ && ./gradlew -Dorg.gradle.daemon=false clean build  
  
# Stage 2: setup docker image  
FROM openjdk:8-jre-alpine  
  
ENV UIOT_RMQ_HOST=localhost  
ENV UIOT_RMQ_PORT=5672  
ENV UIOT_RMQ_USER=rabbitmq  
ENV UIOT_RMQ_PASS=rabbitmq  
ENV UIOT_MONGODB_HOST=localhost  
ENV UIOT_MONGODB_PORT=27017  
ENV UIOT_MONGODB_DATABASE=uiot  
  
COPY \--from=builder /app/build/libs/*.jar app.jar  
  
ENV JAVA_OPTS=""  
EXPOSE 8080  
CMD java \  
-Djava.security.egd=file:/dev/./urandom \  
-Duser.timezone=UTC \  
-Dserver.address=0.0.0.0 \  
-Dserver.port=8080 \  
-Dspring.rabbitmq.host=${UIOT_RMQ_HOST} \  
-Dspring.rabbitmq.port=${UIOT_RMQ_PORT} \  
-Dspring.rabbitmq.username=${UIOT_RMQ_USER} \  
-Dspring.rabbitmq.password=${UIOT_RMQ_PASS} \  
-Dspring.data.mongodb.host=${UIOT_MONGODB_HOST} \  
-Dspring.data.mongodb.port=${UIOT_MONGODB_PORT} \  
-Dspring.data.mongodb.database=${UIOT_MONGODB_DATABASE} \  
-jar app.jar

