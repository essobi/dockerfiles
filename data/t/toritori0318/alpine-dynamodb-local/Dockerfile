FROM anapsix/alpine-java:latest  
  
MAINTAINER TSUYOSHI TORII toritori0318  
  
# dynamodb-local  
RUN wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest -O dynamo.tar.gz  
RUN mkdir dynamodb_local  
RUN tar xvzf dynamo.tar.gz -C ./dynamodb_local && rm -f dynamo.tar.gz  
  
EXPOSE 8000  
CMD ["java", "-Djava.library.path=./dynamodb_local/DynamoDBLocal_lib", "-jar",
"./dynamodb_local/DynamoDBLocal.jar"]  

