FROM phusion/baseimage:0.9.19  
MAINTAINER Axel Utech <axel@brasshack.de>  
  
ENV LANG en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
CMD ["/sbin/my_init"]  
  
RUN \  
echo "Acquire::Languages \"none\";\nAPT::Install-Recommends
\"true\";\nAPT::Install-Suggests \"false\";" > /etc/apt/apt.conf ;\  
echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure tzdata ;\  
locale-gen en_US.UTF-8 en_DK.UTF-8 de_DE.UTF-8 ;\  
apt-get -q -y update ;\  
apt-get install -y aria2 nginx-light \  
unzip ;\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
echo "daemon off;" >> /etc/nginx/nginx.conf ;\  
mkdir /etc/service/nginx ;\  
echo "#!/bin/sh\n/usr/sbin/nginx" > /etc/service/nginx/run ;\  
chmod +x /etc/service/nginx/run  
  
ADD nginx-site.conf /etc/nginx/sites-available/default  
  
# create data dir  
RUN \  
mkdir /data  
  
EXPOSE 80  
VOLUME "/data"  

