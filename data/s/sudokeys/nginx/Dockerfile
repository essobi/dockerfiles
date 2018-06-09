FROM sudokeys/baseimage  
MAINTAINER Bertrand RETIF <bertrand@sudokeys.com>  
  
RUN apt-get update && apt-get install -yq \  
nginx \  
python-flup  
  
ENV autostart true  
  
#Nginx daemon  
RUN mkdir /etc/service/nginx  
COPY run_nginx.sh /etc/service/nginx/run  
  
VOLUME ["/etc/nginx/", "/var/log/nginx"]  
  
EXPOSE 80 443  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  
  

