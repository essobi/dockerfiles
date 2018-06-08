FROM alpine:3.7  
LABEL maintainer="shoma416@gmail.com"  
  
RUN set -xe \  
&& apk update \  
&& apk add --no-cache \  
samba=4.7.6-r0 \  
samba-common-tools=4.7.6-r0 \  
&& touch /etc/printcap  
  
COPY docker-entrypoint.sh /  
  
VOLUME /share  
  
EXPOSE 137/udp 138/udp 139 445  
ENTRYPOINT ["/docker-entrypoint.sh"]

