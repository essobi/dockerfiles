FROM bingli/kazoo-base  
MAINTAINER Bing Li <bingli1000@gmail.com>  
  
RUN yum install -y sudo  
RUN yum -y --nogpgcheck localinstall
http://repo.2600hz.com/Stable/CentOS_6/x86_64/R15B/Kazoo-FreeSWITCH/kazoo-
freeswitch-R15B-1.4.15-3.el6.x86_64.rpm  
  
ADD entrypoint.sh /root/  
  
VOLUME ["/var/log"]  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
  

