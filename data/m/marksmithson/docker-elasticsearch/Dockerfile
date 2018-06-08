FROM java:openjdk-8-jdk  
MAINTAINER Mark Smithson mark@digital-morphosis.com  
RUN apt-get update  
RUN apt-get upgrade -y  
ENV REFRESHED_AT 2015-02-25  
# Install Elastic Search  
RUN wget -O /tmp/elasticsearch.tar.gz
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.4.tar.gz  
RUN tar -C /opt/ -xvf /tmp/elasticsearch.tar.gz  
RUN rm -f /tmp/elasticsearch.tar.gz  
  
RUN ln -s /opt/elasticsearch-1.4.4 /opt/elasticsearch  
  
# Install Plugins  
RUN /opt/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-cloud-
aws/2.4.1  
RUN /opt/elasticsearch/bin/plugin -install elasticsearch/marvel/latest  
RUN /opt/elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic  
  
ADD config/elasticsearch.yml /opt/elasticsearch/config/elasticsearch.yml  
ADD sysctl.d/60-elasticsearch /etc/sysctl.d/60-elasticsearch  
VOLUME ["/data"]  
  
WORKDIR /data  
  
EXPOSE 9200  
EXPOSE 9300  
ENTRYPOINT ["/opt/elasticsearch/bin/elasticsearch"]  

