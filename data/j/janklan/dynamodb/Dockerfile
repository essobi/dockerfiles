FROM openjdk:7  
LABEL Maintainer="Jan Klan <jan@klan.com.au>" \  
Description="Docker image allowing local DynamoDB development."  
  
RUN mkdir -p opt/dynamodb  
WORKDIR /opt/dynamodb  
  
RUN wget https://s3-ap-southeast-1.amazonaws.com/dynamodb-local-
singapore/dynamodb_local_latest.tar.gz -q -O - | tar -xz  
  
# The entrypoint is the dynamodb jar. Default port is 8000.  
EXPOSE 8000  
ENTRYPOINT ["java", "-jar", "DynamoDBLocal.jar"]  
  

