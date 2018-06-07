FROM ubuntu  
EXPOSE 8080  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk unzip wget  
ADD camel-seminar-1.0.0-SNAPSHOT-jar-with-dependencies.jar camel-
seminar-1.0.0-SNAPSHOT.jar  
CMD ["java", "-jar", "camel-seminar-1.0.0-SNAPSHOT.jar"]  

