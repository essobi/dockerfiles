FROM alpine  
LABEL maintainer "wise2c"  
  
RUN mkdir -p /etc/prom-conf/  
  
ADD prometheus.yml /etc/prom-conf/prometheus.yml  
  
VOLUME /etc/prom-conf  
  
CMD ["/bin/sh"]  

