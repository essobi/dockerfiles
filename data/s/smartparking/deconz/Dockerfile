FROM ubuntu:16.04  
MAINTAINER Yannic Wilkening  
  
EXPOSE 3389  
EXPOSE 8080  
RUN usermod -a -G dialout root  
  
RUN apt-get update && apt-get install -y \  
git \  
usbutils \  
build-essential\  
wget\  
qt5-default \  
libqt5sql5 \  
libqt5websockets5-dev \  
libqt5serialport5-dev  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget https://www.dresden-
elektronik.de/deconz/ubuntu/beta/deconz-2.04.67-qt5.deb && \  
wget https://www.dresden-elektronik.de/deconz/ubuntu/beta/deconz-
dev-2.04.67.deb && \  
dpkg -i deconz-2.04.67-qt5.deb && \  
dpkg -i deconz-dev-2.04.67.deb  
  
RUN git clone https://github.com/dresden-elektronik/deconz-rest-plugin.git &&
\  
cd deconz-rest-plugin && \  
git checkout -b mybranch V2_04_67 && \  
qmake && \  
make -j2 && \  
cp ../libde_rest_plugin.so /usr/share/deCONZ/plugins  
  
ADD start.sh /  
RUN chmod +x ./start.sh  
  
CMD ["./start.sh"]

