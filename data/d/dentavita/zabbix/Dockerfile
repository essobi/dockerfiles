FROM centos:centos6  
MAINTAINER Alexey Bogdanenko <abogdanenko@dentavita.ru>  
  
# Update base images.  
RUN yum distribution-synchronization -y  
  
# Install EPEL, Zabbix release packages  
RUN yum install -y http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y http://repo.zabbix.com/zabbix/2.2/rhel/6/x86_64/zabbix-
release-2.2-1.el6.noarch.rpm  
  
RUN yum makecache  
# Installing SNMP Utils  
RUN yum -y -q install net-snmp-devel net-snmp-libs net-snmp net-snmp-perl net-
snmp-python net-snmp-utils  
# Install Lamp Stack, including PHP5 SNMP  
RUN yum -y -q install mysql mysql-server  
# Install Apache and PHP5 with ldap support  
RUN yum -y -q install httpd php php-mysql php-snmp php-ldap  
# Additional Tools  
RUN yum -y -q install perl-JSON pwgen  
# Install zabbix server and php frontend  
RUN yum -y -q install zabbix-agent zabbix-get zabbix-sender zabbix-server
zabbix-server-mysql zabbix-web zabbix-web-mysql  
# Install database files  
RUN yum -y -q install zabbix22-dbfiles-mysql  
# install monit  
RUN yum -y -q install monit  
# Cleaining up  
RUN yum clean all  
# MySQL  
ADD my.cnf /etc/  
# Zabbix Conf Files  
ADD zabbix.ini /etc/php.d/  
ADD httpd_zabbix.conf /etc/httpd/conf.d/zabbix.conf  
ADD zabbix.conf.php /etc/zabbix/web/  
ADD zabbix_agentd.conf /etc/zabbix/  
ADD zabbix_server.conf /etc/zabbix/  
  
# Change Apache DocumentRoot to zabbix folder  
RUN sed -i 's/^DocumentRoot "\/var\/www\/html"$/DocumentRoot
"\/usr\/share\/zabbix"/' /etc/httpd/conf/httpd.conf  
  
RUN chmod 640 /etc/zabbix/zabbix_server.conf  
RUN chown root:zabbix /etc/zabbix/zabbix_server.conf  
  
# Monit  
ADD monitrc /etc/  
RUN chmod 600 /etc/monitrc  
  
# https://github.com/dotcloud/docker/issues/1240#issuecomment-21807183  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
  
ADD /run.sh /  
RUN chmod 755 /run.sh  
  
# Expose the Ports used by  
# * Zabbix services  
# * Apache with Zabbix UI  
# * Monit  
EXPOSE 10051 80 2812  
VOLUME ["/var/lib/mysql"]  
CMD ["/run.sh"]  

