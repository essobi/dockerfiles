FROM centos:7  
RUN yum update -y && yum install -y wget perl openssl-devel  
RUN wget -q -O - http://linux.dell.com/repo/hardware/latest/bootstrap.cgi |
bash  
  
RUN yum install -y srvadmin-idracadm  
  
ENTRYPOINT ["/opt/dell/srvadmin/bin/idracadm"]  

