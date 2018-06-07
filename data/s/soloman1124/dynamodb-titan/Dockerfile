FROM maven:3.3.3-jdk-8  
MAINTAINER Soloman Weng "soloman1124@gmail.com"  
ENV REFRESHED_AT 2016-05-11  
ENV GREMLIN_PORT 8182  
ENV DYNAMODB_ENDPOINT http://dynamodb:8000  
ENV DYNAMODB_PREFIX v100  
ENV AWS_ACCESS_KEY_ID access  
ENV AWS_SECRET_ACCESS_KEY secret  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update  
RUN apt-get install git zip gettext -y  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone https://github.com/awslabs/dynamodb-titan-storage-backend.git
/usr/src/app  
  
RUN mvn install  
RUN /usr/src/app/src/test/resources/install-gremlin-server.sh \  
&& rm /usr/src/app/server/dynamodb-titan100-storage-backend-1.0.0-hadoop1.zip  
  
COPY *.template ./  
COPY run ./  
  
WORKDIR /usr/src/app/server/dynamodb-titan100-storage-backend-1.0.0-hadoop1  
  
EXPOSE $GREMLIN_PORT  
  
ENTRYPOINT ["/usr/src/app/run"]  

