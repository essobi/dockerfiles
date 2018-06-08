FROM centos:7  
ENTRYPOINT ["/opt/dell/srvadmin/bin/idracadm"]  
  
RUN yum install -y wget perl openssl-devel && \  
wget -q -O - http://linux.dell.com/repo/hardware/latest/bootstrap.cgi | bash
&& \  
yum install -y srvadmin-idracadm  

