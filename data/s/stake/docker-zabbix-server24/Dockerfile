FROM centos:centos6  
  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN localedef -f UTF-8 -i ja_JP ja_JP  
  
# Update base images.  
RUN yum distribution-synchronization -y  
  
# setup zabbix  
RUN yum install -y http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y http://repo.zabbix.com/zabbix/2.4/rhel/6/x86_64/zabbix-
release-2.4-1.el6.noarch.rpm  
  
RUN yum install -y net-snmp-devel net-snmp-libs net-snmp net-snmp-perl net-
snmp-python net-snmp-utils  
RUN yum install -y httpd mysql mysql-server php php-mysql java-1.7.0-openjdk
passwd perl-JSON  
RUN sed -i '/tsflags=nodocs/d' /etc/yum.conf  
RUN yum install -y zabbix-agent zabbix-get zabbix-java-gateway zabbix-sender
zabbix-server zabbix-web-japanese zabbix-web-mysql  
  
# setup supervisor  
RUN yum install -y python-setuptools  
RUN easy_install supervisor  
  
# Cleaining up.  
RUN yum clean all  
  
# configuration MySQL  
ADD ./mysql/my.cnf /etc/my.cnf  
  
# configuration Zabbix  
ADD ./zabbix/zabbix.ini /etc/php.d/zabbix.ini  
ADD ./zabbix/httpd_zabbix.conf /etc/httpd/conf.d/zabbix.conf  
ADD ./zabbix/zabbix.conf.php /etc/zabbix/web/zabbix.conf.php  
ADD ./zabbix/zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf  
ADD ./zabbix/zabbix_java_gateway.conf /etc/zabbix/zabbix_java_gateway.conf  
ADD ./zabbix/zabbix_server.conf /etc/zabbix/zabbix_server.conf  
ADD ./scripts/zabbix-server.sh /usr/local/sbin/zabbix-server.sh  
ADD ./scripts/zabbix-agentd.sh /usr/local/sbin/zabbix-agentd.sh  
  
RUN sed -i 's/^\;date\\.timezone \=/date.timezone\=Asia\/Tokyo/' /etc/php.ini  
RUN chmod 640 /etc/zabbix/zabbix_server.conf  
RUN chown root:zabbix /etc/zabbix/zabbix_server.conf  
RUN chmod 755 /usr/local/sbin/zabbix-server.sh /usr/local/sbin/zabbix-
agentd.sh  
  
# Add the script that will start the repo.  
ADD ./supervisord/supervisord.conf /etc/supervisord.conf  
ADD ./run.sh /run.sh  
RUN chmod 755 /run.sh  
  
# Expose the Ports used by  
# * Zabbix services  
# * Apache with Zabbix UI  
EXPOSE 10051 10052 80  
CMD ["/bin/bash", "/run.sh"]

