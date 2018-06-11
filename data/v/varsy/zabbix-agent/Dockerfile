FROM ubuntu:14.04  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com & Stanislav Osipov,
stanislav.osipov@jetbrains.com  
  
ENV TERM=xterm  
RUN apt-get -y update && \  
apt-get install -y wget && \  
wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-
release/zabbix-release_3.0-1+trusty_all.deb && \  
dpkg -i zabbix-release_3.0-1+trusty_all.deb && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y zabbix-agent sysstat  
  
ADD plugins/ /etc/zabbix/plugins/  
RUN find /etc/zabbix/plugins/ -type f -name "*.sh" -exec chmod +x {} \; && \  
find /etc/zabbix/plugins/ -type f -name "*.conf" -exec mv -t
/etc/zabbix/zabbix_agentd.conf.d/ {} \;  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh  
  
CMD /run-services.sh  

