FROM ubuntu:16.04  
MAINTAINER Ben Jones <ben@fogbutter.com>  
RUN apt-get update && \  
apt-get autoremove -y && \  
apt-get upgrade -y && \  
apt-get install -y wget default-jre && \  
mkdir -p /var/dynamodb /usr/local/dynamodb && \  
cd /usr/local/dynamodb && \  
wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz && \  
tar -xzf dynamodb_local_latest.tar.gz && \  
rm -f dynamodb_local_latest.tar.gz  
EXPOSE 8000  
WORKDIR /var/dynamodb  
ENTRYPOINT ["java",
"-Djava.library.path=/usr/local/dynamodb/DynamoDBLocal_lib", "-jar",
"/usr/local/dynamodb/DynamoDBLocal.jar"]  
CMD ["-inMemory"]  
  

