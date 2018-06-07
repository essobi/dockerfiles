FROM strobo/docker-arm-build:zerow  
  
RUN [ "cross-build-start" ]  
  
# Install Required Packages  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
tar \  
unzip \  
git \  
autoconf \  
xz-utils \  
gzip \  
libical-dev \  
libdbus-1-dev \  
libglib2.0-dev \  
libreadline-dev \  
libudev-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /work  
  
# Fetch source  
ENV BLUEZ_VERSION 5.42  
RUN wget -O bluez.tar.gz
https://www.kernel.org/pub/linux/bluetooth/bluez-${BLUEZ_VERSION}.tar.gz \  
&& tar xf bluez.tar.gz \  
&& mv bluez-${BLUEZ_VERSION} bluez \  
&& rm bluez.tar.gz  
  
# Apply Patch  
RUN cd bluez \  
&& wget
https://gist.github.com/pelwell/c8230c48ea24698527cd/archive/3b07a1eb296862da889609a84f8e10b299b7442d.zip
\  
&& unzip 3b07a1eb296862da889609a84f8e10b299b7442d.zip \  
&& git apply -v
c8230c48ea24698527cd-3b07a1eb296862da889609a84f8e10b299b7442d/* \  
&& rm 3b07a1eb296862da889609a84f8e10b299b7442d.zip  
  
# Configure  
RUN cd bluez \  
&& ./configure --prefix=/usr \  
\--mandir=/usr/share/man \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--enable-library \  
\--enable-experimental \  
\--enable-maintainer-mode \  
&& make -j4 \  
&& make install  
  
RUN [ "cross-build-end" ]  

