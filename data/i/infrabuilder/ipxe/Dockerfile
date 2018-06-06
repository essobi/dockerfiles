FROM alpine  
MAINTAINER alexis@infrabuilder.com  
RUN apk --update add dhcp tftp-hpa && rm -rf /var/cache/apk/* && mkdir /tftp  
ADD entrypoint.sh /entrypoint.sh  
ADD http://boot.ipxe.org/undionly.kpxe /tftp/  
ENTRYPOINT ["/entrypoint.sh"]

