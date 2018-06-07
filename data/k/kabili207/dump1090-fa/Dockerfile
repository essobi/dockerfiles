FROM kabili207/rtl-sdr:latest  
MAINTAINER Andrew Nagle <kabili@zyrenth.com>  
  
RUN apk add --no-cache libusb ncurses git build-base libusb-dev ncurses-dev &&
\  
git clone https://github.com/flightaware/dump1090.git /tmp/dump1090 && \  
cd /tmp/dump1090 && \  
make dump1090 BLADERF=no && \  
cp -a dump1090 /usr/bin && \  
cd / && rm -r /tmp/dump1090 && \  
apk del git build-base libusb-dev ncurses-dev  
  
EXPOSE 30001 30002 30003 30004 30005 30104  
ENTRYPOINT ["/usr/bin/dump1090"]  

