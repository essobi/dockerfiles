FROM java:8-alpine  
MAINTAINER Orbweb Inc. <devs@orbweb.com>  
  
ENV VERSION 1.0  
WORKDIR /opt/dynamodb  
RUN apk --no-cache add --virtual .builddeps curl && \  
curl -v -L http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz | tar -xz && \  
apk del .builddeps  
EXPOSE 8000/tcp  
VOLUME ["/var/data/dynamodb"]  
CMD ["java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar",
"DynamoDBLocal.jar", "-sharedDb", "-dbPath", "/var/data/dynamodb", "-port",
"8000"]  

