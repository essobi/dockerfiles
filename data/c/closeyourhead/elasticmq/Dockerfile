FROM alpine:3.3  
MAINTAINER closeyourhead  
  
ENV ELASTICMQ_VERSION 0.9.3  
ENV ELASTICMQ_JAR https://s3-eu-west-1.amazonaws.com/softwaremill-
public/elasticmq-server-${ELASTICMQ_VERSION}.jar  
  
RUN apk --update --no-cache add openjdk7-jre-base  
  
ADD $ELASTICMQ_JAR /elasticmq/server.jar  
  
COPY custom.conf /elasticmq/custom.conf  
  
EXPOSE 9324  
CMD ["java", "-jar", "-Dconfig.file=/elasticmq/custom.conf",
"/elasticmq/server.jar"]  

