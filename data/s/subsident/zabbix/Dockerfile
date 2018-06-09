FROM centos:centos6  
MAINTAINER SHS  
  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY* ; \  
rpm --import http://repo.zabbix.com/RPM-GPG-KEY-ZABBIX ; \  
rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6  
  
#RUN yum history new  
RUN yum -y distribution-synchronization  
  
RUN yum -y install http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y install http://repo.zabbix.com/zabbix/2.2/rhel/6/x86_64/zabbix-
release-2.2-1.el6.noarch.rpm  
  
RUN yum makecache  
  
RUN yum -y update  
  
RUN yum -y install net-snmp-devel net-snmp-libs net-snmp net-snmp-perl net-
snmp-python net-snmp-utils mysql httpd php php-mysql php-snmp php-ldap install
perl-JSON pwgen zabbix-agent zabbix-get zabbix-sender zabbix-server zabbix-
server-mysql zabbix-web zabbix-web-mysql zabbix22-dbfiles-mysql mc lsof htop
wget freetds unixODBC unixODBC-devel traceroute  
  
RUN yum clean all  
  
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python \  
&& easy_install supervisor  
  
RUN sed -i 's/^DocumentRoot "\/var\/www\/html"$/DocumentRoot
"\/usr\/share\/zabbix"/' /etc/httpd/conf/httpd.conf  
  
ADD run.sh /  
#RUN chmod 755 /run.sh  
EXPOSE 80 10001 10051  
EXPOSE 162/udp  
  
CMD ["/run.sh"]  

