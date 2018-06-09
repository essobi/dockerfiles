# Dockerfile for logsniffer  
# https://github.com/therek/docker-logsniffer  
FROM openjdk:8-jdk-alpine  
MAINTAINER Cezary Morga <cm@therek.net>  
  
ENV LOGSNIFFER_VERSION=0.5.6  
RUN apk --update add wget bash tini  
RUN mkdir /logsniffer && \  
wget
https://github.com/logsniffer/logsniffer/releases/download/${LOGSNIFFER_VERSION}/logsniffer.war
-O /logsniffer.war  
  
RUN rm -fr /tmp/* /var/cache/apk/*  
  
EXPOSE 8082  
VOLUME [ "/logsniffer" ]  
ENTRYPOINT [ "/sbin/tini", "--" ]  
CMD [ "/usr/bin/java", "-Dlogsniffer.home=/logsniffer", "-jar",
"/logsniffer.war" ]  

