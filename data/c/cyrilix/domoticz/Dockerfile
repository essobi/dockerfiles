#name of container: docker-domoticz  
#versison of container: 0.1.0  
FROM cyrilix/openzwave  
LABEL MAINTAINER Cyrille Nofficial "cynoffic@cyrilix.fr"  
  
ENV VERSION=3.8153  
#add repository and update the container  
#Installation of nesesary package/software for this containers...  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
build-essential\  
netcat \  
cmake libboost-dev libboost-thread-dev libboost-system-dev \  
libsqlite3-dev curl libcurl4-openssl-dev libusb-dev \  
zlib1g-dev libssl-dev git\  
libudev-dev \  
mplayer2 \  
python3 \  
python3-dev \  
python-libxml2 \  
libxml2-dev \  
python3-pip \  
libxslt-dev \  
lib32z1-dev \  
libboost-python1.55-dev \  
wget \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install caldav  
  
#Compile Domoticz  
RUN git clone https://github.com/domoticz/domoticz.git domoticz ;\  
cd domoticz; git checkout ${VERSION} ;/opt/cmake/bin/cmake -J4
-DCMAKE_BUILD_TYPE=Release -DUSE_PYTHON=YES -DPython_ADDITIONAL_VERSIONS=3.5 .
;\  
make CMAKE_COMMAND=/opt/cmake/bin/cmake && make
CMAKE_COMMAND=/opt/cmake/bin/cmake install &&\  
cd ../ && rm -r domoticz && rm -r /opt/cmake  
  
RUN mkdir -p /opt/domoticz/db/ /opt/domoticz/backup /scripts /opt/domoticz/db  
VOLUME ["/opt/domoticz/scripts", "/opt/domoticz/backups", "/opt/domoticz/db"]  
  
# to allow access from outside of the container to the container service  
# at that ports need to allow access from firewall if need to access it
outside of the server.  
EXPOSE 8080  
# Use baseimage-docker's init system.  
CMD ["/opt/domoticz/domoticz"]  

