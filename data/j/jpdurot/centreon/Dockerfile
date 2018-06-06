FROM centos:centos6  
MAINTAINER jpdurot <jeanphilippe.durot@gmail.com>  
  
# Update CentOS  
RUN yum -y update  
  
# Install Centreon Repository  
RUN yum -y install
http://yum.centreon.com/standard/3.0/stable/noarch/RPMS/ces-
release-3.0-1.noarch.rpm  
  
# Install ssh  
RUN yum -y install openssh-server openssh-client  
RUN mkdir /var/run/sshd  
RUN echo 'root:centreon' | chpasswd  
RUN sed -i 's/^#PermitRootLogin/PermitRootLogin/g' /etc/ssh/sshd_config  
RUN /etc/init.d/sshd start && /etc/init.d/sshd stop  
  
# Install centreon  
RUN yum -y install centreon centreon-base-config-centreon-engine centreon-
installed centreon-clapi  
  
# Install Widgets  
RUN yum -y install centreon-widget-graph-monitoring centreon-widget-host-
monitoring centreon-widget-service-monitoring centreon-widget-hostgroup-
monitoring centreon-widget-servicegroup-monitoring  
  
# Set rights for setuid  
RUN chown root:centreon-engine /usr/lib/nagios/plugins/check_icmp  
RUN chmod -w /usr/lib/nagios/plugins/check_icmp  
RUN chmod u+s /usr/lib/nagios/plugins/check_icmp  
  
# Install and configure supervisor  
RUN yum -y install python-setuptools  
RUN easy_install supervisor  
  
ADD data/supervisord.conf /etc/supervisord.conf  
ADD data/docker_entrypoint.sh /  
ADD data/central-broker.xml /etc/centreon-broker  
ADD data/central-module.xml /etc/centreon-broker  
ADD data/central-rrd.xml /etc/centreon-broker  
  
# Change PHP.ini timezone  
RUN sed -i '/^;date.timezone/cdate.timezone = "Europe/Paris";' /etc/php.ini  
  
RUN chmod u+x /docker_entrypoint.sh  
  
# Expose port SSH and HTTP for the service  
EXPOSE 22 80  
ENTRYPOINT ["/docker_entrypoint.sh"]  
CMD ["start"]  
  

