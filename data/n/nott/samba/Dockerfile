FROM fedora:21  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum -y update; yum clean all;  
RUN yum -y install samba  
  
ADD smb.conf /etc/samba/smb.conf  
  
VOLUME ["/data"]  
  
EXPOSE 445  
CMD /usr/sbin/smbd -F  

