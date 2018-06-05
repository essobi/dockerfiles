FROM maven:3-jdk-8-alpine  
  
RUN apk add \--no-cache git && \  
git clone https://github.com/aerospike/delete-set.git && \  
cd delete-set && \  
mvn clean package  
  
WORKDIR delete-set/target  
ENTRYPOINT ["java", "-jar", "delete-set-1.0.0-jar-with-dependencies.jar"]  
  
CMD ["--usage"]

