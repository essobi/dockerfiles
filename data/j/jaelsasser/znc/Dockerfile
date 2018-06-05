FROM alpine:3.4  
MAINTAINER Josh Elsasser <josh@elsasser.ca>  
EXPOSE 5000 6667 6697  
ENV ZNC_VERSION 1.6.3-r2  
  
# https://github.com/alpinelinux/aports/tree/master/main/znc  
RUN apk add --no-cache \  
sudo ca-certificates \  
znc=$ZNC_VERSION \  
znc-extra=$ZNC_VERSION \  
znc-modperl=$ZNC_VERSION \  
znc-modpython=$ZNC_VERSION \  
znc-modtcl=$ZNC_VERSION \  
znc-dev=$ZNC_VERSION \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /data  
  
RUN apk add --no-cache make g++ pkgconfig zlib-dev \  
perl-dev openssl-dev cyrus-sasl-dev python-dev c-ares-dev swig \  
gettext-dev tcl-dev autoconf automake python3-dev findutils \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
ADD znc.conf.default /var/lib/znc/znc.conf.default  
RUN chmod 644 /var/lib/znc/znc.conf.default  
  
ADD docker-entrypoint.sh /entrypoint.sh  
  
VOLUME /data  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

