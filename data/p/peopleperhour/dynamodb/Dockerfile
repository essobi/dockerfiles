FROM openjdk:8-jre  
  
RUN mkdir /var/dynamodb_wd  
RUN mkdir /var/dynamodb_local  
WORKDIR /var/dynamodb_wd  
  
RUN \  
wget -O /tmp/dynamodb_local_latest https://s3-us-
west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz && \  
tar xfz /tmp/dynamodb_local_latest && \  
rm -f /tmp/dynamodb_local_latest  
  
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar",
"DynamoDBLocal.jar", "-dbPath", "/var/dynamodb_local"]  
CMD ["-port", "8000"]  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/var/dynamodb_local", "/var/dynamodb_wd"]  

