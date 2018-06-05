FROM debian:latest  
MAINTAINER Alejandro Escanero Blanco <aescanero@gmail.com>  
  
LABEL maintainer="Alejandro Escanero Blanco <aescanero@gmail.com>" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.name="Apache2/php7 on Alpine OS" \  
org.label-schema.url="https://www.disasterproject.com" \  
org.label-schema.vcs-url="https://github.com/aescanero/dockerevents/docker-
fusiondirectory-apache.git"  
  
RUN echo "deb http://repos.fusiondirectory.org/debian-jessie jessie main" \  
> /etc/apt/sources.list.d/fusiondirectory-jessie.list \  
&& apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \  
supervisor apache2-bin libapache2-mod-php5 fusiondirectory  
  
RUN apt-cache search smarty &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes\  
fusiondirectory-smarty3-acl-render \  
&& mkdir -p /data/pids && mkdir -p /data/logs \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD etc/fusiondirectory/fusiondirectory.conf
/etc/fusiondirectory/fusiondirectory.conf  
ADD etc/supervisord-fd.conf /etc/supervisord-fd.conf  
  
WORKDIR /data  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord-
fd.conf"]  

