FROM alpine:latest  
MAINTAINER Stephane Albert "sheeprine@nullplace.com"  
ENV ZNC_VERSION 1.6.3  
ADD "http://znc.in/releases/archive/znc-${ZNC_VERSION}.tar.gz" /src/  
RUN apk add --no-cache sudo autoconf automake gettext-dev make g++ \  
openssl-dev pkgconfig perl-dev swig zlib-dev ca-certificates \  
&& cd /src \  
&& tar -xzf "znc-${ZNC_VERSION}.tar.gz" && cd "znc-${ZNC_VERSION}" \  
&& ./configure --disable-ipv6 \  
&& make && make install \  
&& cd / && rm -rf "/src" \  
&& rm -rf /var/cache/apk/*  
  
RUN adduser -S znc  
RUN addgroup -S znc  
ADD docker-entrypoint.sh /entrypoint.sh  
ADD znc.conf.default /znc.conf.default  
RUN chmod 644 /znc.conf.default  
  
VOLUME /znc-data  
  
EXPOSE 6667  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

