FROM chinch/fedora:atomic  
  
RUN dnf -y autoremove ; dnf -y clean all ; dnf -y update ; dnf -y upgrade ; rm
-rf /etc/dnf/dnf.conf  
  
ADD dnf.conf /etc/dnf/  
  
ENTRYPOINT /bin/bash  

