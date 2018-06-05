FROM jpizarrom/armv7hf-java:oracle-java8-201703161  
RUN [ "cross-build-start" ]  
  
RUN \  
apt-get update && \  
apt-get install -y dos2unix ifupdown iproute2 isc-dhcp-client isc-dhcp-common
libatm1 libdns-export100 libirs-export91 libisc-export95 libisccfg-export90
libxtables10 netbase telnet unzip net-tools ethtool && \  
rm -rf /var/lib/apt/lists/*  
  
ENV KURA_VERSION 2.0.2  
ENV KURA_ARCH_VERSION beaglebone-nn_debian  
  
## Kura installation  
RUN \  
wget
http://download.eclipse.org/kura/releases/${KURA_VERSION}/kura_${KURA_VERSION}_${KURA_ARCH_VERSION}_installer.deb
&& \  
dpkg -i kura_${KURA_VERSION}_${KURA_ARCH_VERSION}_installer.deb && \  
rm kura_${KURA_VERSION}_${KURA_ARCH_VERSION}_installer.deb  
  
RUN [ -f /lib/arm-linux-gnueabihf/libudev.so.0 ] || ln -sf /lib/arm-linux-
gnueabihf/libudev.so.1 /lib/arm-linux-gnueabihf/libudev.so.0  
  
ENV ZIGBEE_SERIALPORT /dev/ttyS4  
ENV ZIGBEE_CHANNEL 15  
ENV ZIGBEE_PAN 4568  
ENV ZIGBEE_RESET false  
  
RUN mkdir /app  
WORKDIR /app  
  
## Web and telnet  
EXPOSE 80  
EXPOSE 5002  
CMD ["/opt/eclipse/kura/bin/start_kura.sh"]  
  
RUN [ "cross-build-end" ]  

