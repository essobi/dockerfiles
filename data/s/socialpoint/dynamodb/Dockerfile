FROM openjdk:7-jre  
  
LABEL maintainer "Backend Team <backend@socialpoint.es>"  
  
WORKDIR /var/docker-dynamodb-local  
  
RUN /usr/bin/curl -L https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_latest.tar.gz | /bin/tar xz  
  
RUN mkdir -p /var/dynamodb  
  
EXPOSE 8000  
VOLUME /var/dynamodb  
  
CMD ["/usr/bin/java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar",
"-dbPath", "/var/dynamodb"]

