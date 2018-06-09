FROM baselibrary/java:8  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Version  
ENV LOGSTASH_MAJOR 1.4  
ENV LOGSTASH_VERSION 1.4.5-1-a2bacae  
  
## Repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D88E42B4 &&\  
echo "deb http://packages.elastic.co/logstash/1.4/debian stable main" >
/etc/apt/sources.list.d/logstash.list  
  
## Packages  
RUN \  
apt-get update &&\  
apt-get install -y logstash=$LOGSTASH_VERSION &&\  
rm -rf /var/lib/apt/lists/*  
  
## Environments  
ENV PATH /opt/logstash/bin:$PATH  
  
EXPOSE 9200 9300  
VOLUME ["/var/lib/logstash"]  
  
CMD ["logstash", "agent"]  
  

