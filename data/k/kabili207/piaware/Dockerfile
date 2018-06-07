FROM alpine:latest  
MAINTAINER Andrew Nagle <kabili@zyrenth.com>  
  
ENV VERSION=3.5.3  
  
COPY disable-cert-validation.patch /tmp  
  
RUN apk add \--no-cache libusb ncurses git build-base libusb-dev ncurses-dev \  
tcl-dev tcl tclx tcl-tls autoconf python3 python3-dev && \  
git clone -b v1.6 https://github.com/flightaware/tcllauncher /tmp/tcllauncher
&& \  
cd /tmp/tcllauncher && \  
autoconf && \  
./configure --prefix=/opt/tcl && \  
make && make install && \  
git clone -b tcllib_1_18 https://github.com/tcltk/tcllib /tmp/tcllib && \  
cd /tmp/tcllib && \  
autoconf && \  
./configure && \  
make && make install && \  
git clone -b v${VERSION} --single-branch
https://github.com/flightaware/piaware.git /tmp/piaware && \  
cd /tmp/piaware && \  
patch -p1 < /tmp/disable-cert-validation.patch && \  
make && make install && \  
cp package/ca/*.pem /etc/ssl && \  
update-ca-certificates && \  
git clone https://github.com/flightaware/dump1090.git /tmp/dump1090 && \  
cd /tmp/dump1090 && \  
make faup1090 BLADERF=no RTLSDR=no && \  
cp -a faup1090 /usr/lib/piaware/helpers/ && \  
git clone https://github.com/mutability/mlat-client.git /tmp/mlat-client && \  
cd /tmp/mlat-client && \  
./setup.py install && \  
ln -s /usr/bin/fa-mlat-client /usr/lib/piaware/helpers/ && \  
cd / && rm -r /tmp/piaware /tmp/tcllauncher /tmp/tcllib /tmp/dump1090
/tmp/mlat-client /tmp/disable-cert-validation.patch && \  
apk del git build-base autoconf tcl-dev ncurses-dev python3-dev  
  
EXPOSE 30105  
  
ENV USER=  
ENV PASSWORD=  
ENV FEEDID=  
ENV GPSD=  
  
COPY piaware.conf /etc  
COPY start.sh /  
  
ENTRYPOINT ["/start.sh"]  

