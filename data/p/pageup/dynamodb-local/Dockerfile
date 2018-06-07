FROM openjdk:8-jre  
MAINTAINER Colin Scott  
  
RUN mkdir /var/dynamodb  
WORKDIR /var/dynamodb  
  
EXPOSE 8000  
RUN wget -O /var/dynamodb/dynamodb_local_latest http://dynamodb-
local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz  
RUN tar xfz /var/dynamodb/dynamodb_local_latest  
  
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=./DynamoDBLocal_lib",
"-jar", "DynamoDBLocal.jar"]  
CMD ["-port", "8000", "-sharedDb"]  

