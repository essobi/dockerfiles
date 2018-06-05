FROM anapsix/alpine-java:8u102b14_server-jre  
MAINTAINER Adrian Haasler García <dev@adrianhaasler.com>  
  
# Configuration  
ENV JIRA_HOME /data/jira  
  
# Install dependencies  
RUN apk upgrade --update \  
&& apk add --update curl tar \  
&& apk add xmlstarlet --update --repository
http://dl-6.alpinelinux.org/alpine/edge/testing  
  
# Create the user that will run the jira instance and his home directory (also
make sure that the parent directory exists)  
RUN mkdir -p $(dirname $JIRA_HOME) \  
&& adduser -h $JIRA_HOME -s /bin/bash -u 547 -D jira  

