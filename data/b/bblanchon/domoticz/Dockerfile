# docker build -t bblanchon/domoticz .  
# docker run --device /dev/ttyACM0 -v /etc/localtime:/etc/localtime:ro -p
80:8080 bblanchon/domoticz  
FROM ubuntu:14.04  
MAINTAINER bblanchon  
  
# install dependencies  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
cmake \  
curl \  
git \  
libboost-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libcurl4-openssl-dev \  
libsqlite3-dev \  
libssl-dev \  
libudev-dev \  
libusb-dev \  
zlib1g-dev  
  
# build OpenZWave static library  
RUN cd /tmp && \  
git clone --depth 1 https://github.com/OpenZWave/open-zwave.git && \  
cd open-zwave && \  
make && make install && \  
cp libopenzwave.a /usr/local/lib/  
  
# build domoticz  
RUN cd /tmp && \  
git clone --depth 1 https://github.com/domoticz/domoticz.git && \  
cd domoticz && \  
cmake -DCMAKE_BUILD_TYPE=Release . && \  
make && make install  
  
# cleanup  
RUN rm -Rf /tmp/* && \  
apt-get remove -y build-essential cmake curl git && \  
apt-get autoremove -y && \  
apt-get clean  
  
EXPOSE 8080  
VOLUME ["/var/lib/domoticz"]  
  
ENTRYPOINT ["/opt/domoticz/domoticz", "-dbase",
"/var/lib/domoticz/domoticz.db"]  

