FROM java:8-jre  
  
RUN curl -fsSL https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_latest.tar.gz -o /tmp/dynamodb_local_latest.tar.gz && \  
gunzip /tmp/dynamodb_local_latest.tar.gz && \  
mkdir /tmp/dynamodb && \  
tar -C /tmp/dynamodb -xf /tmp/dynamodb_local_latest.tar && \  
mkdir -p /opt/dynamodb && \  
mv /tmp/dynamodb /opt && \  
rm -rf /tmp/*  
  
EXPOSE 8000  
WORKDIR /opt/dynamodb  
  
ENV JAVA_OPTS "-Xms800M -Xmx800M"  
CMD ["sh", "-c", "java $JAVA_OPTS -Djava.library.path=./DynamoDBLocal_lib -jar
DynamoDBLocal.jar -sharedDb -port 8000"]  

