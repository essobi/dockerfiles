FROM ubuntu:utopic  
MAINTAINER Karsten Lettow "kasitmp@gmail.com"  
# Get dependencies  
RUN apt-get update -y  
RUN apt-get install -y wget  
RUN apt-get install -y openjdk-7-jre-headless  
  
# Download and install dynamoDB local  
RUN mkdir /var/dynamo_db_local  
RUN wget -O /var/dynamo_db_local/dynamo_db.tar.gz http://dynamodb-
local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz  
RUN tar xvfz /var/dynamo_db_local/dynamo_db.tar.gz -C /var/dynamo_db_local  
RUN rm /var/dynamo_db_local/dynamo_db.tar.gz  
  
EXPOSE 8000  
CMD ["java", "-Djava.library.path=/var/dynamo_db_local/DynamoDBLocal_lib",
"-jar", "/var/dynamo_db_local/DynamoDBLocal.jar", "-dbPath",
"/var/dynamo_db_local"]  
  

