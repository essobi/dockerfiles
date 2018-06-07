FROM phusion/baseimage  
MAINTAINER johnodon <johnodon68@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
#Change uid & gid to match Unraid  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody  
  
RUN apt-get update -q  
  
# Install Dependencies  
RUN apt-get install -qy perl libcompress-raw-zlib-perl libhtml-parser-perl \  
libhttp-cookies-perl liblwpx-paranoidagent-perl libconfig-json-perl \  
libjson-xs-perl build-essential cpanminus  
  
ADD files/cron/ /zap2xml/cron/  
ADD files/scripts/ /zap2xml/scripts/  
ADD files/templates/ /zap2xml/templates/  
ADD files/init/ /etc/my_init.d/  
RUN chmod -v +x /zap2xml/scripts/* /etc/my_init.d/*.sh  
  
# Volume mappings  
VOLUME /config /data  

