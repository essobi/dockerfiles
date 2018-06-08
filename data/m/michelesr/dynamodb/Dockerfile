FROM java:8  
MAINTAINER Michele Sorcinelli "michelesr@autistici.org"  
EXPOSE 8000  
RUN mkdir /opt/dynamodb/ && \  
wget 'http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz' && \  
tar xf dynamodb_local_latest.tar.gz -C /opt/dynamodb/ && \  
rm -rf dynamodb_local_latest.tar.gz  
  
CMD ["java", "-Djava.library.path=/opt/dynamodb/DynamoDBLocal_lib", "-jar",
"/opt/dynamodb/DynamoDBLocal.jar", "-sharedDb"]  

