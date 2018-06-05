# BareOS storage Dockerfile  
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
apt-get install -qq -y bareos-storage  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod u+x /docker-entrypoint.sh  
RUN tar cfvz /bareos-sd.tgz /etc/bareos/bareos-sd.d  
  
EXPOSE 9103  
# VOLUME /root/bareos/bareos-sd/config:/etc/bareos  
# VOLUME /root/bareos/bareos-sd/storage:/var/lib/bareos/storage  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/bareos-sd", "-u", "bareos", "-f"]  

