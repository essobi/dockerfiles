FROM java:8  
MAINTAINER Humblehound <dejtabejz@gmail.com>  
ADD . /source  
WORKDIR /source  
RUN ./gradlew build  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","build/libs/napps-0.1.1.jar"]  
  

