FROM centos:centos7  
MAINTAINER matthieu-robin  
  
# Update CentOS  
RUN yum -y update  
RUN yum -y install wget git  
  
# Install Centreon Repository  
RUN wget http://yum.centreon.com/standard/3.4/el7/stable/centreon-stable.repo
-O /etc/yum.repos.d/centreon-stable.repo  
  
# Install Maria-DB  
RUN yum --nogpg -y install MariaDB-server  
RUN /etc/init.d/mysql start  
  
# Install Centreon  
RUN yum --nogpg -y install centreon-base-config-centreon-engine centreon
centreon-widget* centreon-pp-manager  
  
# Install base plugin  
RUN yum --nogpg -y install centreon-plugin-Operatingsystems-Linux-Snmp
centreon-plugin-Applications-Monitoring-Centreon-Central centreon-plugin-
Applications-Monitoring-Centreon-Database centreon-plugin-Applications-
Databases-Mysql  
  
# Install SNMP  
RUN yum -y install net-snmp*  
  
# clean YUM  
RUN yum clean all  
  
# Start services  
ADD scripts/script.sh /tmp/script.sh  
RUN mkdir -p /etc/systemd/system/mariadb.service.d/  
ADD scripts/limits.conf /etc/systemd/system/mariadb.service.d/limits.conf  
RUN chmod +x /tmp/script.sh  
CMD ["/tmp/script.sh"]  
  
# Exposed ports  
EXPOSE 22 80  

