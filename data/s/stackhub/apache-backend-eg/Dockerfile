# Purpose: Demonstrate Apache httpd server as a backend to a load balancer  
FROM httpd  
MAINTAINER Boyd Hemphill <boyd@stackengine.com>  
  
# Place script that hijacks the apache start from the base container  
COPY \  
start.sh \  
/start.sh  
  
RUN \  
chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  

