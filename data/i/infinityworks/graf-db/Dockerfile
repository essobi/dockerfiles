#Grafana SQLLITE pre-configured Dockerfile  
FROM alpine  
MAINTAINER Ed Marshall (ed.marshall@infinityworks.com)  
  
RUN mkdir -p /var/lib/_grafana  
COPY grafana.db /var/lib/_grafana  
COPY entrypoint.sh /usr/sbin/entrypoint.sh  
RUN chmod +x /usr/sbin/entrypoint.sh  
  
ENTRYPOINT /usr/sbin/entrypoint.sh  

