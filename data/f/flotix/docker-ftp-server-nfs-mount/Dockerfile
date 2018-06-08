FROM ubuntu:14.04  
  
MAINTAINER Florian Mauduit <flotix@linux.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
######## ENV VARIABLES ########  
  
# DEBUG  
ENV DEBUG 0  
  
  
# FTP  
ENV FTP **NO**  
ENV FTP_LOGIN flotix  
ENV FTP_PASSWD **ChangeMe**  
  
  
################################  
  
  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common
proftpd nfs-common supervisor libfile-nfslock-perl rpcbind  
  
  
RUN mkdir -p /usr/local/bin  
ADD ./bin /usr/local/bin  
RUN chmod +x /usr/local/bin/*.sh  
ADD ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD ./etc/proftpd.conf /etc/proftpd/proftpd.conf  
  
CMD ["/usr/local/bin/run.sh"]  

