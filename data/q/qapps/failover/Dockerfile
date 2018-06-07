# Keepalived  
FROM fedora:21  
MAINTAINER Yury Kavaliou <Yury_Kavaliou@epam.com>  
  
RUN yum install -y keepalived  
  
RUN echo "net.ipv4.ip_nonlocal_bind = 1" >> /etc/sysctl.conf  
  
COPY ./files/start_failover.sh /usr/local/sbin/start_failover.sh  
RUN chmod u+x /usr/local/sbin/start_failover.sh  
  
ENTRYPOINT [ "/bin/bash", "/usr/local/sbin/start_failover.sh" ]

