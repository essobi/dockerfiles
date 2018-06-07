FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y curl openjdk-7-jre-headless python python-pip  
  
# elasticsearch  
RUN curl -fL
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.2.tar.gz
| tar xzf - -C /opt && \  
mv /opt/elasticsearch-1.7.2 /opt/elasticsearch  
  
# elasticsearch-curator  
RUN pip install elasticsearch-curator  
  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/elasticsearch/bin  
  
CMD ["elasticsearch"]  
  
VOLUME ["/opt/elasticsearch/data", "/opt/elasticsearch/logs"]  

