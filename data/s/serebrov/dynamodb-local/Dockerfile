FROM java:7  
MAINTAINER Boris Serebrov  
  
# files dir  
RUN mkdir /opt/dynamodb_local  
# data dir  
RUN mkdir /opt/dynamodb_local_data  
WORKDIR /opt/dynamodb_local  
  
RUN wget -q http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz && \  
tar zxvf dynamodb_local_latest.tar.gz && rm dynamodb_local_latest.tar.gz  
  
EXPOSE 8000  
ENTRYPOINT ["java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar",
"-port", "8000"]  
CMD ["-dbPath","/opt/dynamodb_local_data","--sharedDb"]  

