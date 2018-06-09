#  
# Dockerfile for DynamoDB Local  
#  
#
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html  
#  
FROM openjdk:8-jre-alpine  
MAINTAINER Teemu Pohja <teemu.pohja@gmail.com>  
EXPOSE 8000  
WORKDIR /dynamodb  
  
ENV DYNAMODB_LOCAL_VERSION=2016-05-17 \  
DYNAMODB_LOCAL_SHA256=832d474316c9d092de8c24885e69c9be9e22b9807e7383e0de6f247e44601a90  
  
# Download and install the binaries to WORKDIR  
RUN wget -q -O dynamodb_local.tar.gz http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_${DYNAMODB_LOCAL_VERSION}.tar.gz && \  
echo "${DYNAMODB_LOCAL_SHA256} dynamodb_local.tar.gz" | sha256sum -c - && \  
tar xzf dynamodb_local.tar.gz && \  
rm dynamodb_local.tar.gz  
  
RUN mkdir -p /dynamodb_data && chown nobody:nobody /dynamodb_data && chmod
0750 /dynamodb_data  
USER nobody  
# VOLUME to allow persistence / access of raw database files  
VOLUME /dynamodb_data  
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=./DynamoDBLocal_lib",
"-jar", "DynamoDBLocal.jar"]  
CMD ["-dbPath","/dynamodb_data"]  

