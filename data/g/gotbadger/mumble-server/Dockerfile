FROM ubuntu:14.04  
MAINTAINER Phil Hayton "p.j.hayton@hotmail.com"  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor mumble-server  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN useradd mumble  
ADD start.sh /  
ADD mumble-server.ini.default /  
RUN chmod +x /start.sh  
  
EXPOSE 64738  
CMD ["/start.sh"]  

