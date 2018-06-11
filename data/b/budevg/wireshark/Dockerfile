FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get --yes build-dep wireshark \  
&& apt-get --yes install wget libwiretap3 dbus  
  
RUN mkdir /data; cd /data \  
&& wget --progress=bar:force
https://www.wireshark.org/download/src/wireshark-2.0.0rc1.tar.bz2 \  
&& tar -xjf wireshark* \  
&& cd wireshark*; ./configure --with-gtk3=yes && make -j 4 \  
&& make install \  
&& rm -rf /data  
  
RUN dbus-uuidgen > /etc/machine-id && mkdir /pcap \  
&& sed -i 's/dofile = function() error("dofile " .. hint) end//'
/usr/local/share/wireshark/init.lua  
  
RUN ldconfig  
  
ENTRYPOINT /usr/local/bin/wireshark-gtk  

