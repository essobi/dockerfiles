FROM alpine:3.6  
RUN apk --no-cache add automake autoconf build-base libtool libusb-dev
openssl-dev git  
  
WORKDIR /src  
  
RUN git clone https://github.com/libimobiledevice-win32/libplist \  
&& git clone https://github.com/libimobiledevice-win32/libusbmuxd \  
&& git clone https://github.com/libimobiledevice-win32/libimobiledevice \  
&& git clone https://github.com/libimobiledevice-win32/usbmuxd  
  
WORKDIR /src/libplist  
RUN ./autogen.sh --without-cython --prefix=/usr \  
&& make \  
&& make install \  
&& make install DESTDIR=/out  
  
WORKDIR /src/libusbmuxd  
RUN ./autogen.sh --without-cython --prefix=/usr \  
&& make \  
&& make install \  
&& make install DESTDIR=/out  
  
WORKDIR /src/libimobiledevice  
RUN ./autogen.sh --without-cython --prefix=/usr \  
&& make \  
&& make install \  
&& make install DESTDIR=/out  
  
WORKDIR /src/usbmuxd  
RUN ./autogen.sh --prefix=/usr \  
&& make \  
&& make install \  
&& make install DESTDIR=/out  
  
FROM alpine:3.6  
WORKDIR /  
  
RUN apk --no-cache add libusb openssl  
  
COPY \--from=0 /out/usr/ /usr/  
  
# Start the server by default  
CMD [ "/usr/sbin/usbmuxd", "-f", "-v", "-w", "-t", "-a" ]  
  
EXPOSE 27015  

