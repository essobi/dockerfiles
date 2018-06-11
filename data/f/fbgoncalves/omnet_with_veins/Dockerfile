FROM ubuntu:latest  
RUN apt-get update  
RUN apt-get install -y wget  
RUN apt-get install -y unzip  
RUN apt-get install -y build-essential gcc g++ bison flex perl tcl-dev tk-dev
blt libxml2-dev zlib1g-dev default-jre doxygen graphviz libwebkitgtk-1.0-0
openmpi-bin libopenmpi-dev libpcap-dev autoconf automake libtool libproj-dev
libgdal1-dev libfox-1.6-dev libgdal-dev libxerces-c-dev qt4-dev-tools  
RUN apt-get install -y software-properties-common  
  
RUN apt-get install -y qt5-default  
RUN apt-get install -y qtdeclarative5-dev  
RUN apt-get install -y libosgearth-dev  
RUN apt-get install -y libopenscenegraph-dev openscenegraph  
RUN apt-get install -y gedit  
RUN apt-get install -y git  
RUN cd /home && wget -O omnetpp-5.2-src-linux.tgz --referer
https://omnetpp.org/omnetpp https://omnetpp.org/omnetpp/send/30-omnet-
releases/2317-omnetpp-5-2-linux/omnetpp-5.2-src-linux.tgz && tar xvfz
omnetpp-5.2-src-linux.tgz  
RUN mkdir /home/sumo  
VOLUME /home/veins  
VOLUME /home/sumo  
VOLUME /home/omnetpp  
ADD ./script.sh /script.sh  
RUN chmod 777 /script.sh  
WORKDIR /home  
ENTRYPOINT ["/bin/bash","/script.sh"]  

