FROM ubuntu:16.04  
MAINTAINER : g6nuk  
RUN apt-get update && \  
apt-get install -y keepalived haproxy && \  
apt-get clean && \  
echo "net.ipv4.ip_nonlocal_bind=1" >> /etc/sysctl.conf  
ADD haproxy.conf /etc/haproxy/haproxy.conf  
ADD keepalived-master.conf /tmp/keepalived-master.conf  
ADD keepalived-slave.conf /tmp/keepalived-slave.conf  
ADD haproxy.log /var/log/haproxy.log  
ADD startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
ENTRYPOINT /startup.sh  
  

