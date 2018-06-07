FROM khipu/base-alpine-s6  
MAINTAINER developers@khipu.com  
  
RUN apk -U add pgbouncer postgresql-client zabbix-agent \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /etc/pgbouncer /etc/zabbix/zabbix_agentd.conf.d  
  
COPY confd /etc/confd  
  
COPY s6/pgbouncer.sh /etc/services.d/pgbouncer/run  
COPY s6/confd.sh /etc/services.d/confd/run  
COPY s6/zabbix_agentd.sh /etc/services.d/zabbix_agentd/run  
COPY docker-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  

