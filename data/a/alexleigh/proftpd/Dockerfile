FROM ubuntu:14.04  
MAINTAINER "Alex Leigh"  
RUN apt-get -y update  
RUN echo 'proftpd-basic shared/proftpd/inetd_or_standalone select standalone'
| debconf-set-selections  
RUN apt-get -y install proftpd-basic proftpd-mod-mysql  
RUN apt-get -y --no-install-recommends install openssh-server  
  
COPY proftpd.conf /etc/proftpd/proftpd.conf  
COPY modules.conf /etc/proftpd/modules.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
VOLUME ["/srv/ftp"]  
RUN chown ftp:nogroup /srv/ftp  
  
EXPOSE 21  
EXPOSE 23  
EXPOSE 49152-49407  
ENTRYPOINT ["/docker-entrypoint.sh"]  

