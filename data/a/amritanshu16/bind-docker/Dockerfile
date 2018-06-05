############################################################  
# Dockerfile to build BIND DNS server with Webmin GUI  
# Based on Ubuntu  
############################################################  
FROM ubuntu:16.04  
MAINTAINER Amritanshu Pandey <amritanshu.blog@gmail.com>  
RUN cd /tmp  
RUN apt update && apt dist-upgrade -y  
RUN rm /etc/apt/apt.conf.d/docker-gzip-indexes  
RUN apt-get purge apt-show-versions  
RUN rm /var/lib/apt/lists/*lz4  
RUN apt-get -o Acquire::GzipIndexes=false update  
RUN apt install wget perl libnet-ssleay-perl libauthen-pam-perl libio-pty-perl
python -y  
RUN apt install apt-show-versions bind9 -y  
RUN wget "http://prdownloads.sourceforge.net/webadmin/webmin_1.870_all.deb"  
RUN dpkg -i webmin_1.870_all.deb  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
CMD /entrypoint.sh && /usr/bin/tail -f /dev/null  
EXPOSE 10000/tcp 53/tcp 53/udp  

