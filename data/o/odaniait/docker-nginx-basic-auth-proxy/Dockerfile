FROM odaniait/docker-base:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
RUN add-apt-repository ppa:nginx/stable && apt-get update && apt-get install
-y nginx apache2-utils  
  
## Install nginx runit service  
RUN mkdir /etc/service/nginx  
COPY runit/nginx.sh /etc/service/nginx/run  
COPY config/nginx.conf /etc/nginx/nginx.conf  
  
## Copy vhost configs  
RUN mkdir -p /etc/nginx-vhosts  
COPY config/auth.vhost.conf /etc/nginx-vhosts/auth.vhost.conf  
COPY config/no-auth.vhost.conf /etc/nginx-vhosts/no-auth.vhost.conf  
  
# Set the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# setup nginx log forwarder  
RUN mkdir -p /etc/service/nginx-log-forwarder  
COPY runit/nginx-log-forwarder.sh /etc/service/nginx-log-forwarder/run  
  
EXPOSE 80  
VOLUME ['/etc/nginx/sites-enabled']  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

