#Prometheus Config Store Dockerfile  
FROM alpine  
LABEL maintainer "Pavithra K C"  
  
RUN mkdir -p /etc/prom-conf/  
  
ADD prometheus.yml /etc/prom-conf/prometheus.yml  
  
RUN chmod 766 /etc/prom-conf/prometheus.yml  
  
ADD alert.rules /etc/prom-conf/alert.rules  
  
RUN chmod 766 /etc/prom-conf/alert.rules  
  
CMD ["/bin/sh"]  

