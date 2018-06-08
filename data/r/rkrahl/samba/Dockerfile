FROM rkrahl/opensuse:42.3  
MAINTAINER Rolf Krahl <rolf.krahl@helmholtz-berlin.de>  
  
RUN zypper --non-interactive install \  
samba  
  
CMD ["/usr/sbin/smbd", "-D"]  
  
EXPOSE 139 445  

