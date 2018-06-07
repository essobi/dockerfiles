FROM debian:stretch  
MAINTAINER Brian H Wilson <brian@wildsong.biz>  
  
# I added some extremely useful tools in here like ps and less...  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends \  
autoconf \  
binutils-dev \  
build-essential \  
ca-certificates \  
curl \  
less \  
libcurl4-openssl-dev \  
libedit-dev \  
libgsm1-dev \  
libjansson-dev \  
libogg-dev \  
libpopt-dev \  
libresample1-dev \  
libspandsp-dev \  
libspeex-dev \  
libspeexdsp-dev \  
libsqlite3-dev \  
libsrtp0-dev \  
libssl-dev \  
libvorbis-dev \  
libxml2-dev \  
libxslt1-dev \  
libncurses5 ncurses-bin ncurses-term \  
portaudio19-dev \  
procps \  
python-pip \  
python-setuptools \  
unixodbc-dev \  
uuid \  
uuid-dev \  
vim-tiny \  
xmlstarlet \  
&& \  
apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*  
  
RUN useradd --system asterisk  
RUN pip install j2cli  
  
ENV ASTERISK_VERSION=15.3.0  
  
COPY build-asterisk.sh /build-asterisk  
RUN /build-asterisk && rm -f /build-asterisk  
  
# In this image, I leave the Asterisk source files around, you will  
# have to remove them later if you don't want them...  

