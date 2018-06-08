FROM node:latest  
MAINTAINER Pierre Prevoteau <p.prevoteau@woody-technologies.com>  
  
RUN apt-get update && apt-get install -y supervisor git gcc clang  
RUN apt-get upgrade -y  
  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN cd /opt && git clone https://github.com/jhuckaby/Cronicle  
RUN cd /opt/Cronicle && npm install  
RUN cd /opt/Cronicle && node bin/build.js dist  
  
EXPOSE 8080  
EXPOSE 443  
CMD ["/usr/bin/supervisord"]  

