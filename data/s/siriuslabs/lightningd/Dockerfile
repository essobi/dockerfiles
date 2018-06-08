FROM siriuslabs/alpine:py3-dev  
  
# add community and testing repo  
RUN echo "@community http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
ENV LIGHTNING_VERSION master  
  
ENV LIGHTNING_HOME /home/lightning  
  
ENV LIGHTNING_DATA /home/lightning/.lightning  
  
RUN apk add --no-cache \  
autoconf \  
automake \  
libtool \  
libsodium-dev \  
sqlite-dev \  
gmp-dev \  
bitcoin-cli@testing \  
file \  
git  
  
RUN set -x \  
&& mkdir -p $LIGHTNING_HOME \  
&& addgroup -g 1000 -S lightning \  
&& adduser -u 1000 -h $LIGHTNING_HOME -D -S -G lightning lightning \  
&& chown -R lightning:lightning $LIGHTNING_HOME  
  
RUN git clone https://github.com/ElementsProject/lightning.git /opt/lightningd
\  
&& cd /opt/lightningd \  
&& git checkout $LIGHTNING_VERSION \  
&& sed -i '/#define __BYTE_ORDER __BYTE_ORDER__/c\//REMOVED_BY_DOCKER'
/usr/include/endian.h \  
&& make \  
&& sed -i '/\/\/REMOVED_BY_DOCKER/c\\#define __BYTE_ORDER __BYTE_ORDER__'
/usr/include/endian.h \  
&& cp lightningd/lightning* cli/lightning-cli /usr/bin/  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 9735  
VOLUME ["/home/lightning/.lightning"]  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  

