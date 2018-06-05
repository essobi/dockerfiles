FROM bingli/kazoo-base  
MAINTAINER Bing Li <bingli1000@gmail.com>  
  
RUN yum -y --nogpgcheck localinstall http://repo.2600hz.com/Packages/Kazoo-
Kamailio-4.2/CentOS_6/x86_64/4.2.3/kazoo-kamailio-4.2.3-16.el6.x86_64.rpm  
  
RUN sed -i '/children/s/25/10/' /etc/kazoo/kamailio/default.cfg  
  
ADD entrypoint.sh /root/  
  
VOLUME ["/var/log]  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
  

