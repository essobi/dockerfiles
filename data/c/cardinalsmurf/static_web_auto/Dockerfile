# Version 0.0.1  
FROM ubuntu:16.04  
MAINTAINER Robert Buckley "rbuckley@marvell.com"  
RUN apt-get update && apt-get install -y nginx curl  
RUN echo 'Hi, I am in your container' \  
>/var/www/html/index.html  
EXPOSE 80  
VOLUME [ "/opt/cavalry" ]  
ADD stuff.tar /opt/cavalry/  
HEALTHCHECK \--interval=10s --timeout=1m --retries=5 CMD curl http://localhost
|| exit 1  
ENTRYPOINT [ "/usr/sbin/nginx" ]  
CMD [ "-g", "daemon off;" ]  
  

