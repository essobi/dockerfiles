FROM debian:unstable  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apt-get -q -y update  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge install git prometheus etcd  
RUN rm -fr /etc/prometheus/*  
COPY run-prometheus.sh /usr/local/bin/run-prometheus.sh  
  
VOLUME ["/secrets", "/etc/prometheus"]  
USER prometheus  
ENTRYPOINT ["/bin/sh", "/usr/local/bin/run-prometheus.sh"]  

