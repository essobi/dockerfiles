# Generated automatically by update.sh  
# Do no edit this file  
FROM openjdk:7-jre  
  
RUN mkdir /dynamodb  
WORKDIR /dynamodb  
  
RUN wget -O- https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_latest.tar.gz \  
| tar -xzf - -C /dynamodb  
  
VOLUME ["/data/db"]  
  
EXPOSE 8000  
ENTRYPOINT ["java",
"-Djava.library.path=/opt/dynamodb_local/DynamoDBLocal_lib", "-jar",
"DynamoDBLocal.jar"]  
CMD ["-sharedDb", "-dbPath", "/data/db"]  

