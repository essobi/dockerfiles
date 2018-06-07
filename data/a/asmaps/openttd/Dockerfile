FROM debian:jessie  
MAINTAINER asmaps <docker@asmaps.de>  
  
RUN apt-get update && apt-get install -y wget libfontconfig1 libfreetype6
liblzo2-2 libpng12-0 libsdl1.2debian unzip  
WORKDIR /opt  
RUN wget http://binaries.openttd.org/releases/1.5.3/openttd-1.5.3-linux-
generic-amd64.tar.gz  
RUN tar xvf openttd-1.5.3-linux-generic-amd64.tar.gz  
WORKDIR /opt/openttd-1.5.3-linux-generic-amd64/baseset  
RUN wget
http://bundles.openttdcoop.org/opengfx/releases/LATEST/opengfx-0.5.4.zip  
RUN unzip opengfx-0.5.4.zip  
WORKDIR /opt/openttd-1.5.3-linux-generic-amd64  
  
EXPOSE 3978 3979 3978/udp 3979/udp  
  
ENTRYPOINT ["./openttd"]  
CMD ["-D"]  

