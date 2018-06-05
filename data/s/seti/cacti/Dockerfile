FROM phusion/baseimage:0.9.16  
MAINTAINER Seti <seti@setadesign.net>  
  
ENV HOME=/root \  
DEBIAN_FRONTEND=noninteractive \  
LC_ALL=C.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
  
COPY assets/snmpd.sh /etc/service/snmpd/run  
COPY assets/apache2.sh /etc/service/apache2/run  
COPY assets/init.sh /etc/my_init.d/init.sh  
  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends &&
\  
echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends && \  
apt-get update && \  
apt-get install -y mysql-client snmpd gdebi-core wget && \  
wget https://github.com/setiseta/docker-
cacti/releases/download/v0.8.8c-test/cacti-spine_0.8.8c-0ubuntu1_amd64.deb &&
\  
wget https://github.com/setiseta/docker-
cacti/releases/download/v0.8.8c-test/cacti_0.8.8c-0ubuntu1_all.deb && \  
gdebi --non-interactive cacti_0.8.8c-0ubuntu1_all.deb && \  
gdebi --non-interactive cacti-spine_0.8.8c-0ubuntu1_amd64.deb && \  
apt-get remove -y wget gdebi-core && \  
rm -f cacti-spine_0.8.8c-0ubuntu1_amd64.deb cacti_0.8.8c-0ubuntu1_all.deb && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /data/logs /data/rra /data/config && \  
echo www-data > /etc/container_environment/APACHE_RUN_USER && \  
echo www-data > /etc/container_environment/APACHE_RUN_GROUP && \  
echo /var/log/apache2 > /etc/container_environment/APACHE_LOG_DIR && \  
echo /var/lock/apache2 > /etc/container_environment/APACHE_LOCK_DIR && \  
echo /var/run/apache2.pid > /etc/container_environment/APACHE_PID_FILE && \  
echo /var/run/apache2 > /etc/container_environment/APACHE_RUN_DIR && \  
ln -s /usr/sbin/spine /usr/bin/spine && \  
chmod +x /etc/service/snmpd/run \  
/etc/service/apache2/run \  
/etc/my_init.d/init.sh  
  
COPY assets/config/snmpd.conf /etc/snmp/snmpd.conf  
COPY assets/config/vhost.conf /etc/apache2/conf-available/cacti.conf  
  
EXPOSE 80 161  
  
CMD ["/sbin/my_init"]

