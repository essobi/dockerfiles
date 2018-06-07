FROM phusion/baseimage:0.9.11  
MAINTAINER Geoffroy Aubry <gaubry@hi-media.com>  
  
# Set correct environment variables.  
ENV HOME /root  
# Fix for $HOME:  
RUN echo /root > /etc/container_environment/HOME  
  
# Set the locale  
RUN locale-gen en_US.UTF-8 && echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install packages  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
> /etc/apt/sources.list.d/mongodb.list  
RUN echo 'deb http://finja.brachium-system.net/~jonas/packages/graylog2_repro/
wheezy main' > /etc/apt/sources.list.d/graylog2.list  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
--force-yes graylog2-server graylog2-web  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
--force-yes graylog2-stream-dashboard  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
mongodb-org  
  
# Enable graylog init script  
RUN sed -i 's@no@yes@' /etc/default/graylog2-server  
RUN sed -i 's@no@yes@' /etc/default/graylog2-web  
  
ADD ./graylog2-server.conf /etc/graylog2/server/server.conf  
RUN chown _graylog2:_graylog2 /etc/graylog2/server/server.conf  
ADD ./graylog2-web-interface.conf /etc/graylog2/web/graylog2-web-
interface.conf  
RUN chown _graylog2:_graylog2 /etc/graylog2/web/graylog2-web-interface.conf  
  
# Expose Mongodb ports:  
# - 27017: process  
# - 28017: http  
EXPOSE 27017  
EXPOSE 28017  
# Define mountable directories:  
VOLUME ["/var/lib/mongodb"]  
  
# Expose ports:  
# - 9000: Web interface  
# - 12201: GELF (UDP & TCP)  
# - 12900: REST API  
EXPOSE 9000 12201 12201/udp 12900  
ADD ./mongod.conf /etc/mongod.conf  
RUN chown mongodb:mongodb /etc/mongod.conf  
ADD ./mongod.sh /etc/my_init.d/01_mongod.sh  
RUN chmod +x /etc/my_init.d/01_mongod.sh  
  
ADD ./graylog2-server.sh /etc/my_init.d/02_graylog2-server.sh  
RUN chmod +x /etc/my_init.d/02_graylog2-server.sh  
  
RUN echo "#!/bin/sh\n/etc/init.d/graylog2-web start" >
/etc/my_init.d/03_graylog2-web.sh  
RUN chmod +x /etc/my_init.d/03_graylog2-web.sh  
  
# Clean up APT when done:  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

