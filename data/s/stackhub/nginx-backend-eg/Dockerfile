# Purpose: Demonstrate nginx as a backend to a load balancer  
FROM nginx  
MAINTAINER Boyd Hemphill <boyd@stackengine.com>  
  
# Place script that hijacks the command from the base container.  
COPY \  
start.sh \  
/start.sh  
  
RUN \  
chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]

