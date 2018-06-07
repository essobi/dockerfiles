FROM java:7  
MAINTAINER maverick@factual.com  
  
RUN apt-get -qqy update && apt-get -qqy install wget procps curl cron  
  
WORKDIR /usr/local/  
RUN wget -qO nexus-2.8.1-01-bundle.tar.gz
http://download.sonatype.com/nexus/oss/nexus-2.8.1-01-bundle.tar.gz  
RUN tar xzf nexus-2.8.1-01-bundle.tar.gz  
RUN rm nexus-2.8.1-01-bundle.tar.gz  
  
# Running nexus server  
ENV RUN_AS_USER root  
WORKDIR /usr/local/nexus-2.8.1-01  
  
RUN mkdir -p /share/maven  
COPY start.sh .  
  
CMD ["./start.sh"]  

