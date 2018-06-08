FROM java:8-alpine  
MAINTAINER Said Sef <said@saidsef.co.uk>  
  
LABEL "uk.co.saidsef.aws-dynamodb"="Said Sef Associates Ltd"  
LABEL version="1.5"  
  
ARG PORT=""  
ENV PORT ${PORT:-8000}  
ENV HOME /tmp  
  
WORKDIR /opt/dynamodb  
  
RUN apk add --update wget && \  
wget -O /tmp/dynamodb.tar.gz https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_latest.tar.gz && \  
tar xfvz /tmp/dynamodb.tar.gz && \  
rm -fv /tmp/dynamodb.tar.gz && \  
rm -rfv /var/cache/apk/*  
  
EXPOSE $PORT  
CMD ["java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-dbPath",
"/opt/dynamodb/db", "-port", "8000"]  

