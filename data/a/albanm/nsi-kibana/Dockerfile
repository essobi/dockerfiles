# Use phusion/passenger-nodejs as base image (see
https://github.com/phusion/passenger-docker)  
FROM phusion/passenger-nodejs:0.9.11  
MAINTAINER Alban Mouton <alban.mouton@gmail.com>  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Install Java for elasticsearch.  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer  
  
# Install ElasticSearch.  
RUN \  
cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.2.tar.gz
&& \  
tar xvzf elasticsearch-1.3.2.tar.gz && \  
rm -f elasticsearch-1.3.2.tar.gz && \  
mv /tmp/elasticsearch-1.3.2 /elasticsearch  
  
# Define mountable directory for elasticsearch data.  
VOLUME ["/data"]  
  
# Configure elasticsearch to write data in /data  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Expose elasticsearch HTTP and transport ports  
EXPOSE 9200  
EXPOSE 9300  
# Install kibana  
RUN \  
wget https://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz -O
/tmp/kibana.tar.gz && \  
tar zxf /tmp/kibana.tar.gz && mv kibana-3.1.0/* /usr/share/nginx/html  
  
# activate nginx to serve kibana  
RUN rm -f /etc/service/nginx/down  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

