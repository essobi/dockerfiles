FROM openjdk:8-alpine  
  
LABEL maintainer="developers@graze.com" \  
license="MIT" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vendor="graze" \  
org.label-schema.name="sqs-local" \  
org.label-schema.description="Docker image with an SQS-compatible queue
implementation for local development" \  
org.label-schema.vcs-url="https://github.com/graze/docker-sqs-local"  
  
ENV ELASTIC_MQ_VERSION 0.13.8  
  
ADD https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-${ELASTIC_MQ_VERSION}.jar /elasticmq-server.jar  
COPY elasticmq.conf /elasticmq.conf  
  
ENTRYPOINT ["/usr/bin/java", "-Dconfig.file=elasticmq.conf", "-jar",
"/elasticmq-server.jar"]  
  
EXPOSE 9324  
  
CMD ["-help"]  

