FROM java:7  
RUN mkdir /dynamodb_local/  
RUN curl -fs http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_2016-05-17.tar.gz | tar xzv -C
/dynamodb_local/  
  
ENTRYPOINT ["java", "-Djava.library.path=/dynamodb_local/DynamoDBLocal_lib",
"-jar", "/dynamodb_local/DynamoDBLocal.jar"]  
EXPOSE 8000  

