FROM livingstoneonline/base:ubuntu  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
RUN apt-install vsftpd && \  
mkdir -p /var/run/vsftpd/empty && \  
cleanup  
  
WORKDIR /srv/ftp  
EXPOSE 20-21  
EXPOSE 21100-21110  
COPY rootfs /  

