# AWS DynamoDB Local  
# docker run -d -p 8000:8000 pottava/aws-dynamodb-local  
FROM pottava/java:7  
RUN apk --no-cache add curl \  
&& mkdir -p /opt/dynamodb /var/dynamodb/db \  
&& cd /opt/dynamodb \  
&& curl --location --silent http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest | tar xzf - \  
&& apk del curl  
  
WORKDIR /opt/dynamodb  
  
ENTRYPOINT ["java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar",
"-dbPath", "/var/dynamodb/db"]  
CMD ["-port", "8000"]  
  
EXPOSE 8000  

