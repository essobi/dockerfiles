FROM debian:stretch  
MAINTAINER Tobias Haber <kontakt@t-haber.de>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ftp.de.debian.org/debian stretch main" >
/etc/apt/sources.list  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install --fix-missing samba samba-common -y  
  
RUN rm -f /etc/samba/smb.conf  
  
ADD smb.conf /etc/samba/smb.conf  
RUN echo "* soft nofile 16384" >> /etc/security/limits.conf  
RUN echo "* hard nofile 16384" >> /etc/security/limits.conf  
  
EXPOSE 445  
EXPOSE 135  
EXPOSE 138  
EXPOSE 139  
EXPOSE 137/udp  
EXPOSE 138/udp  
ADD start.sh /bin/start.sh  
RUN chmod a+x /bin/start.sh  
CMD ["./bin/start.sh"]  

