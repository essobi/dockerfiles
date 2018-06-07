FROM centos:centos6  
MAINTAINER loki <loki@lokis-chaos.de>  
  
RUN yum install -y wget perl && wget -q -O -
http://linux.dell.com/repo/hardware/latest/bootstrap.cgi | bash && yum install
-y srvadmin-base srvadmin-storage-cli srvadmin-idrac srvadmin-omcommon tar
dell_ft_install && yum clean all  
ADD ipmi /etc/rc.d/init.d/ipmi  
ADD launch.sh /usr/local/bin/launch.sh  
ENV PATH
"/sbin:/bin:/usr/sbin:/usr/bin:/opt/dell/srvadmin/sbin:/opt/dell/srvadmin/bin"  
ENTRYPOINT [ "/usr/local/bin/launch.sh" ]  

