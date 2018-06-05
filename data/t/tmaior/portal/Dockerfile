#Tomcat  
#tmaior  
#docker run -d --name zabbix -p 80:80 -p 10051:10051 -v
/etc/localtime:/etc/localtime:ro --env="ZS_DBHost=portal.ctpdim9r054w.sa-
east-1.rds.amazonaws.com" --env="ZS_DBUser=portal"
--env="ZS_DBPassword=tmaiorportal" zabbix/zabbix-3.0:latest  
FROM zabbix/zabbix-3.0:latest  
  
COPY bootstrap.sh /config/init/bootstrap.sh  
  
RUN mkdir /usr/local/src/zabbix/frontends/zabbix  
  
RUN cp -r /usr/local/src/zabbix/frontends/php/*
/usr/local/src/zabbix/frontends/zabbix  
  
RUN mv /usr/local/src/zabbix/frontends/zabbix
/usr/local/src/zabbix/frontends/php/

