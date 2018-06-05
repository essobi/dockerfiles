  
FROM ubuntu:14.04  
MAINTAINER rhodri@refactorit.io  
  
ENV SHAIRPORT_VERSION=2.8 SHAIRPORT_NAME=Docker  
  
RUN apt-get update && apt-get install -q -y --no-install-recommends \  
autoconf \  
automake \  
avahi-daemon \  
build-essential \  
ca-certificates \  
git \  
libasound2-dev \  
libavahi-client-dev \  
libconfig-dev \  
libdaemon-dev \  
libpopt-dev \  
libtool \  
libssl-dev \  
libsoxr-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN cd /root \  
&& git clone https://github.com/mikebrady/shairport-sync.git \  
&& cd /root/shairport-sync \  
&& git checkout -q $SHAIRPORT_VERSION \  
&& autoreconf -i -f \  
&& ./configure --with-alsa --with-avahi --with-ssl=openssl --with-soxr --with-
metadata \  
&& make \  
&& make install  
  
COPY start.sh /start  
  
ENTRYPOINT [ "/start" ]  

