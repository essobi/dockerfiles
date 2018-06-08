FROM resin/armv7hf-debian-qemu AS armBin  
  
FROM arm32v6/alpine:latest  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
MAINTAINER Andreas Sehr <andreas@softbrix.se>  
MAINTAINER Marc Ammon <marc.ammon@fau.de>  
  
EXPOSE 80  
VOLUME [ "/webdav" ]  
  
ENV HTPASSWD=webdav:kK1eUy0t2agv6 \  
PACKAGE_LIST="lighttpd lighttpd-mod_webdav lighttpd-mod_auth" \  
REFRESHED_AT='2017-10-20'  
ADD files/* /etc/lighttpd/  
ADD ./entrypoint.sh /entrypoint.sh  
  
COPY \--from=armBin /usr/bin/cross-build-start /usr/bin/  
COPY \--from=armBin /usr/bin/cross-build-end /usr/bin/  
COPY \--from=armBin /usr/bin/qemu-arm-static /usr/bin/  
COPY \--from=armBin /usr/bin/resin-xbuild /usr/bin/  
RUN [ "cross-build-start" ]  
  
RUN chmod u+x /entrypoint.sh && \  
apk add --no-cache ${PACKAGE_LIST}  
  
RUN [ "cross-build-end" ]  
  
ENTRYPOINT ["/entrypoint.sh"]  

