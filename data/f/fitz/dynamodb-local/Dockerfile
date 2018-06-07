FROM jeanblanchard/java:8  
MAINTAINER Ryan Fitzgerald, ryan.fitz1@gmail.com  
  
WORKDIR /data  
  
RUN wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz  
RUN tar xzf dynamodb_local_latest.tar.gz  
RUN rm dynamodb_local_latest.tar.gz  
  
ENTRYPOINT ["java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar",
"DynamoDBLocal.jar"]  
  
CMD ["-help"]  
  
EXPOSE 8000

