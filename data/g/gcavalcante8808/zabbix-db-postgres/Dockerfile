FROM postgres:latest  
  
RUN apt-get update && apt-get -y install wget tar && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get clean  
  
ARG ZBX_VERSION=3.4.9  
WORKDIR /tmp  
RUN wget
http://ufpr.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/${ZBX_VERSION}/zabbix-${ZBX_VERSION}.tar.gz
&& \  
tar xzvf zabbix-$ZBX_VERSION.tar.gz && \  
mv zabbix-$ZBX_VERSION/database/postgresql /tmp/ && \  
rm -rf /usr/src/zabbix-$ZBX_VERSION  
COPY zabbix-db-entrypoint.sh /docker-entrypoint-initdb.d/  
  
EXPOSE 5432  

