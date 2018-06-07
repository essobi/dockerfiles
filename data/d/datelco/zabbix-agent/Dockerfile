FROM phusion/baseimage  
MAINTAINER gdubina@dataart.com  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y wget  
  
RUN \  
wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-
release/zabbix-release_3.0-1+trusty_all.deb; \  
dpkg -i zabbix-release_3.0-1+trusty_all.deb; \  
apt-get update; apt-get install zabbix-agent; \  
rm zabbix-release_3.0-1+trusty_all.deb  
  
RUN mkdir -p /etc/my_init.d  
RUN mkdir -p /var/run/zabbix && chmod 777 /var/run/zabbix  
  
ADD files/start_agent.sh /etc/my_init.d/0start_agent.sh  
  

