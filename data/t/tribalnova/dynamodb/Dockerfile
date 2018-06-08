FROM openjdk:7  
RUN mkdir /lib/dynamodb  
WORKDIR /lib/dynamodb  
  
RUN curl -sSL http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest|tar xz  
  
VOLUME ["/opt/dynamodb"]  
EXPOSE 8000  
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar",
"DynamoDBLocal.jar", "-dbPath", "/opt/dynamodb", "-port", "8000"]  
CMD ["-sharedDb", "-delayTransientStatuses"]

