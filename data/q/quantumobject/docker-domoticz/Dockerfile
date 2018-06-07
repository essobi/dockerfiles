#name of container: docker-domoticz  
#versison of container: 0.3.1  
FROM quantumobject/docker-baseimage:16.04  
MAINTAINER Angel Rodriguez "angelrr7702@gmail.com"  
ENV TZ America/New_York  
  
#Update the container  
#Installation of nesesary package/software for this containers...  
RUN apt-get update && echo $TZ > /etc/timezone &&
DEBIAN_FRONTEND=noninteractive apt-get install -y -q build-essential\  
cmake libboost-dev libboost-thread-dev libboost-system-dev \  
libsqlite3-dev curl libcurl4-openssl-dev libusb-dev \  
zlib1g-dev libssl-dev git\  
libudev-dev python3-dev python3-pip \  
fail2ban \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/* ;\  
#Compile OpenZWave  
git clone --depth 2 https://github.com/OpenZWave/open-zwave.git ;\  
ln -s open-zwave open-zwave-read-only ; \  
cd open-zwave; \  
make; cd .. ; \  
  
#Compile Domoticz  
git clone --depth 2 https://github.com/domoticz/domoticz.git domoticz ;\  
cd domoticz ; git fetch --unshallow ; cmake -DCMAKE_BUILD_TYPE=Release . ;\  
make ; \  
mkdir /domoticz/backup ; sync ; cp -R /domoticz/scripts /domoticz/backup ;\  
cp -R /domoticz/plugins /domoticz/backup ; \  
  
# ouimeaux  
pip3 install -U ouimeaux ;\  
  
# remove git and tmp dirs  
apt-get remove -y git cmake linux-headers-amd64 build-essential libssl-dev
libboost-dev libboost-thread-dev libboost-system-dev libsqlite3-dev
libcurl4-openssl-dev libusb-dev zlib1g-dev libudev-dev ;\  
apt-get autoremove -y ;\  
apt-get clean ;\  
rm -rf /var/lib/apt/lists/*  
  
##startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container
run the first time .. using a flag to don't  
#run it again ... use for conf for service ... when run the first time ...  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
## used the finish scrip of cron to create a backup copy of the configuration
when container is stopped or terminate.  
COPY finish_cron /etc/service/cron/finish  
RUN chmod +x /etc/service/cron/finish  
  
#  
VOLUME /domoticz/scripts /domoticz/plugins  
  
# to allow access from outside of the container to the container service  
# at that ports need to allow access from firewall if need to access it
outside of the server.  
EXPOSE 8080  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

