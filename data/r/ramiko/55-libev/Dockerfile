FROM debian:latest  
  
MAINTAINER ramiko "tao.ramiko@gmail.com"  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y gettext build-essential autoconf
libtool libpcre3-dev asciidoc xmlto libmbedtls-dev libev-dev libudns-dev libc-
ares-dev git automake libnet1-dev libpcap0.8-dev net-tools \  
&& git config --global http.sslVerify false  
  
# install libsodium  
RUN git clone https://github.com/jedisct1/libsodium.git \  
&& cd libsodium \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf libsodium  
  
#install shadowsocks-libev  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git \  
&& cd shadowsocks-libev \  
&& git submodule update --init --recursive \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& cd .. \  
&& rm -rf shadowsocks-libev  
  
WORKDIR /opt  
RUN git clone https://github.com/shadowsocks/simple-obfs.git \  
&& cd simple-obfs \  
&& git submodule update --init --recursive \  
&& ./autogen.sh \  
&& ./configure --disable-documentation \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf simple-obfs  
  
# install net-speeder  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh \  
&& mv net_speeder /usr/local/bin/  
  
# add net-speeder shell  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/net_speeder  
  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

