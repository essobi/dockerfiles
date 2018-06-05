FROM alpine:3.3  
MAINTAINER Ryan Parrish <ryan@stickystyle.net>  
EXPOSE 6667  
ADD docker-entrypoint.sh /entrypoint.sh  
  
ENV ZNC_VERSION 1.6.2-r0  
  
# https://github.com/alpinelinux/aports/tree/master/main/znc  
RUN apk add --no-cache \  
znc=$ZNC_VERSION \  
znc-extra=$ZNC_VERSION \  
znc-modperl=$ZNC_VERSION \  
znc-modpython=$ZNC_VERSION \  
znc-modtcl=$ZNC_VERSION \  
znc-dev=$ZNC_VERSION \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /znc-data  
ADD znc.conf.default /znc.conf.default  
RUN chmod 644 /znc.conf.default  
  
RUN apk add --no-cache sudo bash make g++ pkgconfig zlib-dev ca-certificates \  
perl-dev openssl-dev cyrus-sasl-dev python-dev c-ares-dev swig \  
gettext-dev tcl-dev autoconf automake python3-dev \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /znc-data  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

