FROM fedora:latest  
  
WORKDIR /root/  
ADD fedora-packages /root/fedora-packages  
ADD installer /root/installer  
  
RUN yum -y update  
RUN yum -y install `cat fedora-packages`  
  
RUN bash /root/installer/*  
  
CMD journalctl -f  

