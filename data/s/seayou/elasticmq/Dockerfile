FROM openjdk:8-jre-alpine  
MAINTAINER Domonkos Czinke <domonkos.czinke@gmail.com>  
EXPOSE 9324  
ENV ELASTICMQ_VERSION 0.12.0  
COPY custom.conf /elasticmq/custom.conf  
ADD https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-${ELASTICMQ_VERSION}.jar /elasticmq/server.jar  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
tini \  
&& apk add --no-cache --virtual .build-deps \  
py-pip \  
&& pip install awscli \  
&& chmod 544 /elasticmq/server.jar \  
&& apk del .build-deps  
  
ENTRYPOINT ["tini", "--"]  
USER nobody  
CMD java -jar -Dconfig.file=/elasticmq/custom.conf /elasticmq/server.jar  

