#name of container: docker-domoticz  
#versison of container: 0.1.0  
FROM debian:jessie  
MAINTAINER Cyrille Nofficial "cynoffic@cyrilix.fr"  
ENV VERSION=3.5877  
#add repository and update the container  
#Installation of nesesary package/software for this containers...  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
build-essential\  
rsyslog \  
netcat \  
cmake libboost-dev libboost-thread-dev libboost-system-dev \  
libsqlite3-dev curl libcurl4-openssl-dev libusb-dev \  
zlib1g-dev libssl-dev git\  
libudev-dev \  
mplayer2 \  
python3 python3-dev \  
python \  
python-dev \  
python-libxml2 \  
libxml2-dev \  
python-pip \  
python3-pip \  
libxslt-dev \  
lib32z1-dev \  
libboost-python1.55-dev \  
wget \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install caldav && pip3 install caldav  
  
# Rebuild cmake because stable version (3.0.2) incompatible with openssl  
RUN wget -O- https://cmake.org/files/v3.5/cmake-3.5.2.tar.gz | tar xzv \  
&& cd cmake-3.5.2 \  
&& ./configure --prefix=/opt/cmake \  
&& make \  
&& make install \  
&& cd ../  
  
#Compile OpenZWave  
RUN git clone https://github.com/OpenZWave/open-zwave.git ;\  
ln -s open-zwave open-zwave-read-only ; \  
cd open-zwave; \  
make; cd ..  
  
#Compile Domoticz  
RUN git clone https://github.com/domoticz/domoticz.git domoticz ;\  
cd domoticz; git checkout master ;/opt/cmake/bin/cmake -J4
-DCMAKE_BUILD_TYPE=Release . ;\  
make CMAKE_COMMAND=/opt/cmake/bin/cmake && make
CMAKE_COMMAND=/opt/cmake/bin/cmake install &&\  
cd ../ && rm -r domoticz && rm -r /opt/cmake  
  
# Modify Timezone to Asia/Shanghai  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
RUN mkdir -p /opt/domoticz/db/ /opt/domoticz/backup /scripts /opt/domoticz/db  
VOLUME ["/opt/domoticz/scripts", "/opt/domoticz/backups", "/opt/domoticz/db"]  
  
# to allow access from outside of the container to the container service  
# at that ports need to allow access from firewall if need to access it
outside of the server.  
EXPOSE 8080  
# Use baseimage-docker's init system.  
CMD ["/opt/domoticz/domoticz"]  

