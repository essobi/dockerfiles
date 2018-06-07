FROM openjdk:8-jdk  
  
ADD sketchws-1.0-SNAPSHOT.jar /data/sketchws-1.0-SNAPSHOT.jar  
ADD config.yml /data/config.yml  
RUN cat /data/config.yml  
CMD java -jar /data/sketchws-1.0-SNAPSHOT.jar server /data/config.yml  
  
EXPOSE 8080  
  

