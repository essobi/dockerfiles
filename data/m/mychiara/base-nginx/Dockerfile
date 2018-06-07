  
#!/bin/bash  
  
FROM mychiara/webbase:1.0.0  
MAINTAINER Andy Ruck mychiara+docker at gmail com  
  
RUN apt-get update && \  
apt-get install -yq --force-yes --no-install-recommends python-software-
properties && \  
add-apt-repository ppa:nginx/stable && \  
apt-get update && apt-get install -y nginx  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
apt-get autoclean && apt-get -y autoremove && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# nginx config  
ADD /files/nginx.conf /etc/nginx/nginx.conf  
  
  
# using the phusion init system  
RUN mkdir -p /etc/service/nginx  
RUN rm /etc/nginx/sites-enabled/default  
  
EXPOSE 8080  
  
VOLUME "/app-src"  

