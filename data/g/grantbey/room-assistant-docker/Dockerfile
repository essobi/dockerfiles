FROM debian:jessie-slim  
  
# homedir  
ENV HOME /root  
  
# workdir  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y \  
bluetooth \  
libbluetooth-dev \  
libudev-dev \  
libusb-1.0-0-dev \  
git \  
curl \  
build-essential \  
wget \  
tar \  
libglib2.0-dev \  
libdbus-1-dev \  
libusb-dev \  
libudev-dev \  
libical-dev \  
systemd \  
libreadline-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir bluez && cd bluez \  
&& wget https://www.kernel.org/pub/linux/bluetooth/bluez-5.47.tar.xz \  
&& tar xvf bluez-5.47.tar.xz && cd bluez-5.47 \  
&& ./configure --enable-library \  
&& make -j8 && make install \  
&& cd .. && rm -rf bluez  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone https://github.com/mKeRix/room-assistant.git \  
&& cd room-assistant \  
&& npm install  
  
WORKDIR /root/room-assistant  
  
CMD ["npm", "start"]

