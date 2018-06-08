#softflowd  
FROM debian:jessie  
MAINTAINER mmerrick  
  
RUN apt-get update  
RUN apt-get install -y softflowd  
RUN service softflowd stop  
  
CMD ["/usr/sbin/softflowd", "-v", "9", "-d", "-i", "eth1", "-n",
"192.168.0.91:9999"]  

