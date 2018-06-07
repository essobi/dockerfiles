FROM tomesar/armv7hf-debian-qemu  
  
RUN [ "cross-build-start" ]  
  
RUN echo "deb http://archive.raspbian.org/raspbian jessie main contrib non-
free rpi firmware" >> /etc/apt/sources.list \  
&& apt-key adv --keyserver pgp.mit.edu --recv-key 0x9165938D90FDDD2E \  
&& echo "deb http://archive.raspberrypi.org/debian jessie main" >>
/etc/apt/sources.list.d/raspi.list \  
&& apt-key adv --keyserver pgp.mit.edu --recv-key 0x82B129927FA3303E  
  
# wget is used for checking network connectivity. git for cloning sar-config  
RUN apt-get update && apt-get install -y --no-install-recommends \  
less \  
libraspberrypi-bin \  
module-init-tools \  
nano \  
net-tools \  
ifupdown \  
iputils-ping \  
i2c-tools \  
usbutils \  
wget git \  
dnsutils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# install docker + docker-compose  
ADD *.deb /root/  
RUN dpkg -i /root/*.deb  
  
WORKDIR /root  
  
ADD ./bootstrap.sh /root/bootstrap.sh  
  
RUN chmod +x /root/bootstrap.sh  
  
CMD ["/root/bootstrap.sh"]  
  
RUN [ "cross-build-end" ]  

