FROM ubuntu:bionic  
ENV DEBIAN_FRONTEND noninteractive  
LABEL maintainer="Joost van den Broek <jvandenbroek+docker@gmail.com>"  
  
RUN apt-get update \  
&& apt-get -y install libssl-dev libevent-dev build-essential \  
libtool autotools-dev automake pkg-config libssl-dev \  
libevent-dev bsdmainutils python-dev libxml2-dev libxslt-dev \  
libbz2-dev wget software-properties-common git \  
&& add-apt-repository ppa:bitcoin/bitcoin \  
&& apt-get update \  
&& apt-get install -y libdb4.8-dev libdb4.8++-dev \  
&& git clone https://github.com/Gulden/gulden-official.git /gulden-official \  
&& mkdir /boost165 \  
&& chmod -R a+rwx /boost165 \  
&& cd /boost165 \  
&& wget -N
https://sourceforge.net/projects/boost/files/boost/1.65.0/boost_1_65_0.tar.bz2
\  
&& tar -xf boost_1_65_0.tar.bz2 \  
&& cd boost_1_65_0/ \  
&& ./bootstrap.sh \  
&& ./b2 --prefix=/boost165 cxxflags=-fPIC cflags=-fPIC link=static install \  
&& cd /gulden-official \  
&& git checkout old_autotools \  
&& ./autogen.sh \  
&& ./configure --with-boost=/boost165/ LDFLAGS="-L/boost165/lib/"
CPPFLAGS="-I/boost165/include" \--prefix=/usr \  
&& make V=1 -j $(expr $(grep MemTotal /proc/meminfo | awk '{print $2}') /
2000000) \  
&& make install \  
&& rm -rf /boost165 /gulden-official /var/cache/apt/* /var/log/* \  
&& apt-get -y remove libssl-dev libevent-dev build-essential \  
libtool autotools-dev automake pkg-config libssl-dev \  
libevent-dev bsdmainutils python-dev libxml2-dev libxslt-dev \  
libbz2-dev wget software-properties-common git \  
libdb4.8-dev libdb4.8++-dev \  
&& apt-get -y autoremove \  
&& apt-get -y install libevent-pthreads-2.1-6 libdb4.8 libdb4.8++
libevent-2.1-6  
  
ENTRYPOINT ["/usr/bin/GuldenD"]  
CMD ["-datadir=/data", "-pid=/data/Gulden.pid"]  
  
EXPOSE 9231 9232  

