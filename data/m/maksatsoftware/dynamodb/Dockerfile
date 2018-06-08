FROM java:8  
MAINTAINER Maksat Annageldyev <maksat.annageldyev@maksat.software>  
  
RUN mkdir -p opt/dynamodb  
WORKDIR /opt/dynamodb  
  
RUN wget https://s3.eu-central-1.amazonaws.com/dynamodb-local-
frankfurt/dynamodb_local_latest.tar.gz -q -O - | tar -xz  
  
EXPOSE 8000  
ENTRYPOINT ["java", "-jar", "DynamoDBLocal.jar"]  

