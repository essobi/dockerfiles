FROM openjdk:8u121-jre-alpine  
  
ADD . /data  
WORKDIR /data  
CMD ["gradle","oneJar"]  
CMD java -jar build/libs/bonbox-1.0-SNAPSHOT-standalone.jar server bonbox.yaml  
  
EXPOSE 8080  

