FROM ggtools/java8  
MAINTAINER Christophe Labouisse  
  
# Create working space  
RUN mkdir -p /var/dynamodb_wd  
WORKDIR /var/dynamodb_wd  
  
# Default port for DynamoDB Local  
EXPOSE 8000  
# Get the package from Amazon  
RUN wget -O - http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest | \  
tar -xzf -  
  
# Default command for image  
ENTRYPOINT ["java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar",
"-dbPath", "/var/dynamodb_local", "-port", "8000"]  
CMD ["-sharedDb", "-optimizeDbBeforeStartup", "-delayTransientStatuses"]  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/var/dynamodb_local", "/var/dynamodb_wd"]  

