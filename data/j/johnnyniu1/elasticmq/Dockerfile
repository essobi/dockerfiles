FROM anapsix/alpine-java:8_jdk  
MAINTAINER Johnny Niu (johnnyniu@aconex.com)  
  
RUN apk add --update curl && rm -rf /var/cache/apk/*  
  
ENV ELASTICMQ_VERSION 0.9.3  
EXPOSE 9324  
CMD ["java", "-jar", "-Dconfig.file=/elasticmq/custom.conf",
"/elasticmq/server.jar"]  
COPY custom.conf /elasticmq/custom.conf  
  
ADD https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-${ELASTICMQ_VERSION}.jar /elasticmq/server.jar

