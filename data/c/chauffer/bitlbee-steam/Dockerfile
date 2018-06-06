FROM alpine  
MAINTAINER Simone Esposito <chaufnet@gmail.com>  
  
RUN apk add --no-cache --update bitlbee json-glib libgcrypt \  
&& apk add --no-cache --update --virtual .build-dependencies \  
bitlbee-dev git make autoconf automake libtool gcc g++ json-glib-dev
libgcrypt-dev \  
&& cd /tmp \  
&& git clone https://github.com/jgeboski/bitlbee-steam.git \  
&& cd bitlbee-steam \  
&& ./autogen.sh \  
&& make \  
&& make install \  
&& strip /usr/lib/bitlbee/steam.so \  
&& rm -rf /tmp/* \  
&& apk del .build-dependencies  
  
EXPOSE 6667  
  
VOLUME /var/lib/bitlbee  
ENTRYPOINT [ "/usr/sbin/bitlbee", "-F", "-n" ]  

