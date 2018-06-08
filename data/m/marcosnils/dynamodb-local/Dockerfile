FROM jeanblanchard/busybox-java:7  
MAINTAINER Marcos Lilljedahl, marcosnils@gmail.com  
  
RUN wget -O- http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest | gunzip | tar x  
  
ENTRYPOINT ["/opt/jdk/bin/java", "-Djava.library.path=./DynamoDBLocal_lib",
"-jar", "DynamoDBLocal.jar"]  
  
CMD ["-help"]  

