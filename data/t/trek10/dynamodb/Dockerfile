FROM java:openjdk-9-jre  
MAINTAINER Jared Short <jshort@trek10.com>  
  
# Create working space  
RUN mkdir /var/dynamodb  
WORKDIR /var/dynamodb  
  
# Default port for DynamoDB Local  
EXPOSE 8000  
# Get the package from Amazon  
RUN wget -O /var/dynamodb/dynamodb_local_latest https://s3-us-
west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz  
RUN tar xfz /var/dynamodb/dynamodb_local_latest  
  
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar",
"DynamoDBLocal.jar", "-inMemory", "-sharedDb"]  
# CMD ["-port", "8000"]  

