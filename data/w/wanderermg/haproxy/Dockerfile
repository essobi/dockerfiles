FROM phusion/baseimage:0.9.16  
MAINTAINER Pavel Mironov <wanderermg@gmail.com>  
  
CMD ["/sbin/my_init"]  
  
RUN apt-add-repository ppa:vbernat/haproxy-1.5 -y && apt-get update -y && apt-
get dist-upgrade -y && apt-get install haproxy -y && mkdir /run/haproxy &&
mkdir /etc/service/haproxy  
ADD haproxy.cfg /etc/haproxy/haproxy.cfg  
ADD haproxy.sh /etc/service/haproxy/run  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/etc/haproxy"]  

