FROM ubuntu  
  
MAINTAINER Toby Hughes <toby@learnium.net>  
  
RUN apt-get update && apt-get -y install nginx  
  
ADD . /var/www/jitsi-meet  
  
# These can be configured per environment  
ENV XMPP_DOMAIN="example.com"  
ENV XMPP_HOST="localhost"  
ENV XMPP_PORT="5280"  
ENV PORT="80"  
CMD ["/var/www/jitsi-meet/deploy/scripts/run.sh"]  

