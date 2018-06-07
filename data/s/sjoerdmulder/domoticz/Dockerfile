FROM ubuntu:14.04  
## packages dependencies  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
libboost-thread1.55-dev libssl-dev libcurl4-openssl-dev libusb-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
## Domoticz installation  
RUN mkdir -p /opt/domoticz \  
&& wget -qO-
http://releases.domoticz.com/releases/release/domoticz_linux_x86_64.tgz | tar
xz -C /opt/domoticz  
  
WORKDIR /opt/domoticz  
  
VOLUME /config  
  
EXPOSE 8080  
ENTRYPOINT ["/opt/domoticz/domoticz", "-dbase", "/config/domoticz.db", "-log",
"/config/domoticz.log"]  
CMD ["-www", "8080"]  

