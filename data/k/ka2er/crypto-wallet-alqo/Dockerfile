## inspired by : https://github.com/masternodes/vps/  
##  
# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.10.0  
CMD ["/sbin/my_init"]  
  
# upgrade OS  
RUN add-apt-repository ppa:bitcoin/bitcoin  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# crypto dev-tools  
RUN apt-get install --no-install-recommends -y nano git automake build-
essential libtool autotools-dev autoconf pkg-config libssl-dev libboost-all-
dev software-properties-common libdb4.8-dev libdb4.8++-dev libminiupnpc-dev  
  
# ...put your own build instructions here...  
RUN apt-get install -y bsdmainutils  
  
ENV PROJECT alqo  
ENV GIT_URL git://github.com/ALQOCRYPTO/ALQO.git  
ENV HOME_DIR /usr/local/bin  
  
  
RUN mkdir -p /opt/code/ && cd /opt/code/ && git clone ${GIT_URL} ${PROJECT} &&
cd /opt/code/${PROJECT} && ./autogen.sh \  
&& ./configure --enable-tests=no --with-incompatible-bdb --enable-glibc-back-
compat --with-gui=no \  
#CFLAGS="-march=native" LIBS="-lcurl -lssl -lcrypto -lz" \  
&& make -j4 && make install \  
&& rm -rf /opt/code/  
  
# __ EOI __  
#  
RUN apt-get purge -y git automake build-essential libtool autotools-dev
autoconf pkg-config libssl-dev libboost-all-dev software-properties-common
libdb4.8++-dev libminiupnpc-dev  
# Clean up APT when done.  
RUN apt-get autoremove -y && apt-get -y clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  

