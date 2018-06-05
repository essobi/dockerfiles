FROM nginx:alpine  
MAINTAINER Benjamin Heuer <benjamin.heuer@netresearch.de>  
  
LABEL customer="Akeneo"  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV TERM=xterm  
  
COPY setup/ /  
  
VOLUME ["/var/cache/nginx"]  
  
WORKDIR /var/www/html  
  
RUN chmod u+x /run.sh  
  
CMD ["/run.sh"]  

