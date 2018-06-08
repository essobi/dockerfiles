FROM debian:stretch-slim  
#FROM ubuntu:16.10  
MAINTAINER Juha Kovanen <juha@particl.io>  
  
ARG CONTAINER_TIMEZONE=Europe/Helsinki  
ARG PARTICL_VERSION=master  
  
ENV PARTICL_DATA=/root/.particl  
ENV PATH=/opt/particl-${PARTICL_VERSION}/bin:$PATH  
  
RUN echo "Building $PARTICL_VERSION"  
  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y apt-transport-https ca-certificates wget curl gnupg2
autogen git net-tools \  
&& apt-get install -y build-essential libtool autotools-dev automake autoconf
\  
&& apt-get install -y pkg-config libssl-dev libboost-all-dev ntp ntpdate
libzmq3-dev \  
&& apt-get install -y libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev
qttools5-dev-tools \  
&& apt-get install -y libprotobuf-dev protobuf-compiler libqrencode-dev
autoconf \  
&& apt-get install -y openssl libevent-dev libminiupnpc-dev bsdmainutils
libsodium-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# RUN echo "deb http://deb.torproject.org/torproject.org stretch main" >>
/etc/apt/sources.list  
# RUN echo "deb-src http://deb.torproject.org/torproject.org stretch main" >>
/etc/apt/sources.list  
# RUN gpg --keyserver keys.gnupg.net --recv-keys 886DDD89  
# RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -  
# RUN apt-get update -y \  
# && apt-get install -y tor deb.torproject.org-keyring proxychains \  
# && apt-get clean \  
# && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# RUN usermod -a -G debian-tor root  
RUN echo ${CONTAINER_TIMEZONE} >/etc/timezone && \  
ln -sf /usr/share/zoneinfo/${CONTAINER_TIMEZONE} /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
echo "Container timezone set to: $CONTAINER_TIMEZONE"  
  
RUN ntpdate -q ntp.ubuntu.com  
  
RUN if [ "$PARTICL_VERSION" = "master" ]; then \  
cd /root \  
&& git clone https://github.com/particl/particl-core.git \  
&& cd particl-core; \  
# elif [ "$PARTICL_VERSION" = "0.16" ]; then \  
# cd /root \  
# && git clone https://github.com/particl/particl-core.git \  
# && cd particl-core \  
# && git checkout ${PARTICL_VERSION}; \  
else \  
cd /root \  
&& git clone https://github.com/particl/particl-core.git \  
&& cd particl-core \  
&& git fetch --all --tags --prune \  
&& git checkout tags/v${PARTICL_VERSION} -b v${PARTICL_VERSION}; \  
fi  
  
# RUN cd /root \  
# && git clone https://github.com/particl/particl-core.git \  
# && cd particl-core \  
# && git checkout v${PARTICL_VERSION}  
RUN cd /root/particl-core \  
&& mkdir db4 \  
&& cd db4 \  
&& wget 'http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz' \  
&& tar -xzvf db-4.8.30.NC.tar.gz \  
&& cd db-4.8.30.NC/build_unix \  
&& ../dist/configure --enable-cxx --disable-shared --with-pic
--prefix=/root/particl-core/db4/ \  
&& make install  
RUN cd /root/particl-core \  
&& ./autogen.sh \  
&& ./configure LDFLAGS="-L/root/particl-core/db4/lib/"
CPPFLAGS="-I/root/particl-core/db4/include/" \  
&& make  
  
RUN mkdir /root/.particl  
VOLUME ["/root/.particl"]  
# VOLUME ["/var/lib/tor"]  
RUN mkdir -p /opt/particl/bin \  
&& cp -rf /root/particl-core/src/particl-cli /root/particl-core/src/particl-tx
/root/particl-core/src/particld /opt/particl/bin/  
  
COPY docker-entrypoint.sh /opt/particl/bin/entrypoint.sh  
  
ENV PATH="/opt/particl/bin:${PATH}"  
RUN chmod +x /opt/particl/bin/*  
# RUN /etc/init.d/tor stop  
EXPOSE 51738 51935  
HEALTHCHECK \--interval=5m --timeout=3s --retries=3 \  
CMD particl-cli getinfo || exit 1  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["particld"]  
  

