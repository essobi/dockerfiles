FROM phusion/baseimage  
MAINTAINER Daniel Covello  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y wget nodejs npm  
RUN ln -s `which nodejs` /usr/bin/node  
WORKDIR /app  
  
ENV BANNANA_VERSION 1.6.0  
RUN mkdir -p /app/banana && \  
wget https://github.com/lucidworks/banana/archive/v$BANNANA_VERSION.tar.gz -O
/app/banana.tar.gz && \  
tar -C /app/banana -xvf /app/banana.tar.gz --strip-components=1 &&\  
cd /app/banana && \  
npm install  
  
RUN mkdir -p /etc/service/banana  
COPY start-banana.sh /etc/service/banana/run  
RUN chmod +x /etc/service/banana/run  
  
ENV SOLR_HOST solr  
ENV SOLR_PORT 8983  
ENV SOLR_DOMAIN solr/  
  
EXPOSE 8000  

