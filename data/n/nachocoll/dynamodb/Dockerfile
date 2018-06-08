# DynamoDB Local Docker!  
#
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html  
FROM openjdk:7  
VOLUME /data  
RUN mkdir -p opt/dynamodb  
WORKDIR /opt/dynamodb  
RUN wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz -q -O - | tar -xz  
EXPOSE 8000  
CMD ["java", "-jar", "DynamoDBLocal.jar", "-dbPath",
"/data","-port","8000","-sharedDb"]  

