FROM alpine:3.2  
MAINTAINER Armin Vogt avogt@s-und-n.de  
  
# http://wiki.alpinelinux.org/wiki/Setting_up_Transparent_Squid_Proxy  
#  
  
RUN set -x \  
&& apk add --update curl gettext acf-squid &&\  
rm -rf /etc/ssl /usr/share/man /tmp/* /var/cache/apk/* /var/lib/apk/*
/etc/apk/cache/*  
  
ENV SQUID_VERSION=3.3.8 \  
SQUID_CACHE_DIR=/var/spool/squid \  
SQUID_LOG_DIR=/var/log/squid \  
SQUID_USER=squid \  
proxy_pass= \  
proxy_user= \  
parent_proxy= \  
https_parent_proxy= \  
parent_port=80 \  
disk_cache_mb=500 \  
access_log_uri=/var/log/squid/access.log  
  
ADD /assets/squid.conf /etc/squid/squid.conf  
  
ADD entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENV http_proxy="" \  
https_proxy=""  
  
EXPOSE 3128  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

