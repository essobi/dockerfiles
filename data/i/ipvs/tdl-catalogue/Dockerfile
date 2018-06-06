FROM ubuntu:latest  
MAINTAINER ipvs.uni-stuttgart.de  
RUN apt-get update; apt-get install -y gradle openjdk-8-jdk  
WORKDIR /  
COPY . /repo  
WORKDIR /repo  
RUN gradle build -x test  
WORKDIR /  
RUN cp /repo/build/libs/topic-catalogue-0.0.1-SNAPSHOT.jar ./app.jar  
EXPOSE 8080  
CMD java -Dmongodb.ip=${MONGODB_IP} -Dmongodb.port:${MONGODB_PORT} -jar
./app.jar  

