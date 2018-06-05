# BareOS webserver Dockerfile  
FROM debian:latest  
MAINTAINER fjfernandez <fjfc83@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget && \  
apt-get install -y curl  
  
RUN wget -q
http://download.bareos.org/bareos/release/latest/Debian_8.0/Release.key -O- |
apt-key add - && \  
echo "deb http://download.bareos.org/bareos/release/latest/Debian_8.0/ /" >
/etc/apt/sources.list.d/bareos.list && \  
apt-get update -qq && \  
apt-get install -qq -y bareos-webui  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod u+x /docker-entrypoint.sh  
RUN tar cfvz /bareos-webui.tgz /etc/bareos-webui  
  
EXPOSE 80  
# VOLUME /root/bareos-vol/bareos-webui:/etc/bareos-webui  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

