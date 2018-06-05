## ActiveMQ standalone  
## VERSION 5.13.3  
## Based on @pires jre docker image  
FROM quay.io/pires/docker-jre:8u92  
MAINTAINER Tiago Pires, tandrepires@gmail.com  
  
ENV AMQ_VERSION 5.13.3  
ENV AMQ_HOME /opt/apache-activemq  
  
# Install ActiveMQ  
RUN apk add --update curl ca-certificates && \  
( curl -Lkjs http://mirror.sdunix.com/apache/activemq/$AMQ_VERSION/apache-
activemq-$AMQ_VERSION-bin.tar.gz | \  
gunzip -c - | tar xf - ) && \  
mv /apache-activemq-$AMQ_VERSION /opt/ && \  
ln -s /opt/apache-activemq-$AMQ_VERSION $AMQ_HOME && \  
apk del curl ca-certificates && \  
rm /var/cache/apk/*  
  
# expose below ports  
EXPOSE 1883 5672 8161 61613 61614 61616  
CMD ["/opt/apache-activemq/bin/activemq", "console"]  

