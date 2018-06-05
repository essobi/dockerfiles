FROM sameersbn/ubuntu:latest  
MAINTAINER jonas@lediga.st  
  
ENV BIND_USER=bind \  
BIND_VERSION=1:9.10.5 \  
WEBMIN_VERSION=1.850 \  
DATA_DIR=/data  
  
RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \  
&& wget http://www.webmin.com/jcameron-key.asc -qO - | apt-key add - \  
&& echo "deb http://download.webmin.com/download/repository sarge contrib" >>
/etc/apt/sources.list \  
&& apt-get -y update \  
&& apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y bind9* bind9-host*
webmin=* \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 53/udp 53/tcp 10000/tcp  
VOLUME ["${DATA_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["/usr/sbin/named"]  

