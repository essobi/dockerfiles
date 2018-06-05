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
apt-get install -qq -y bareos-client && \  
curl -Lsk
https://github.com/bareos/bareos/blob/master/src/cats/make_catalog_backup.pl.in
-o /usr/lib/bareos/scripts/make_catalog_backup.pl  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod u+x /docker-entrypoint.sh  
RUN tar cfvz /bareos-fd.tgz /etc/bareos/bareos-fd.d  
  
EXPOSE 9102  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/bareos-fd", "-u", "bareos", "-f"]  

