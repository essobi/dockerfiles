#name of container: docker-domoticz  
#version of container: 0.1.0  
FROM cyrilix/openzwave  
LABEL MAINTAINER None Whatsoever "none@whatsoever.nl"  
  
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
  
#Set timezone and make datadirectories  
RUN sudo rm /etc/localtime ; sudo ln -s /usr/share/zoneinfo/Europe/Amsterdam
/etc/localtime  
  
RUN mkdir -p /opt/domoticz/data/db /opt/domoticz/data/scripts
/opt/domoticz/data/backup  
VOLUME ["/opt/domoticz/data"]  
  
# Port to access domoticz  
EXPOSE 8080  
ENTRYPOINT ["/opt/domoticz/domoticz", "-dbase",
"/opt/domoticz/data/db/domoticz.db", "-www", "8080"]

