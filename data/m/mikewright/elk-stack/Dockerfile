FROM openjdk:8-jre  
  
MAINTAINER "Michael Wright <mkwright@gmail.com>"  
RUN useradd -ms /bin/bash elastic  
  
RUN apt-get update && \  
apt-get install -y supervisor nginx  
  
ENV ELASTIC_VERSION 5.0.0  
ADD
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTIC_VERSION}.tar.gz
/elastic/  
  
RUN cd /elastic && \  
tar --strip-components=1 -xvf elasticsearch-${ELASTIC_VERSION}.tar.gz && \  
chown -R elastic:elastic /elastic && \  
mkdir -p /home/elastic  
  
ENV HOME /home/elastic  
  
EXPOSE 9200  
WORKDIR /elastic  
  
VOLUME /data  
VOLUME /logs  
  
ADD elasticsearch.yml /elastic/config/elasticsearch.yml  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD startup /elastic/startup  
  
CMD ["./startup"]  
  

