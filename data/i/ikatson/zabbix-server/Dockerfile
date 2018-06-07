FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install --no-install-recommends -y zabbix-
server-pgsql postgresql-client zabbix-agent python  
  
RUN install -o zabbix -g zabbix -d /var/run/zabbix/  
  
EXPOSE 10051  
ADD start.sh /start.sh  
  
ENTRYPOINT ["/start.sh"]  

