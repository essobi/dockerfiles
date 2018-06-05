FROM centos:6.6  
RUN yum install -y \  
wget \  
perl \  
dmidecode  
  
RUN wget -q -O - http://linux.dell.com/repo/hardware/latest/bootstrap.cgi |
bash \  
&& yum -y install srvadmin-idrac  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

