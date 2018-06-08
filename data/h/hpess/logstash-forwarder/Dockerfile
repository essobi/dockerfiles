FROM hpess/base:master  
MAINTAINER Karl Stoney <karl.stoney@hp.com>  
  
# Install the forwarder and the openssl stuff to generate certificates  
RUN yum -y install https://download.elasticsearch.org/logstash-
forwarder/binaries/logstash-forwarder-0.4.0-1.x86_64.rpm && \  
yum -y -q install openssl && \  
yum -y -q clean all  
  
COPY tmp/* /tmp/  
COPY preboot/* /preboot/  
COPY services/* /etc/supervisord.d/  
  
WORKDIR /opt/logstash-forwarder  
ENV HPESS_ENV logstash-forwarder  
  
VOLUME ["/logs"]  

