FROM alpine as BUILD_ENV  
  
RUN apk add --no-cache musl-dev gcc make cmake pkgconf git libusb-dev  
  
WORKDIR /usr/local/  
RUN git clone git://git.osmocom.org/rtl-sdr.git && cd rtl-sdr && git checkout
tags/v0.5.3  
  
RUN mkdir /usr/local/rtl-sdr/build  
WORKDIR /usr/local/rtl-sdr/build  
RUN cmake ../ -DDETACH_KERNEL_DRIVER=ON -DCMAKE_C_FLAGS="-static-libstdc++"  
RUN make  
RUN make install  
  
FROM alpine  
  
RUN apk add --no-cache libusb  
  
COPY \--from=BUILD_ENV /usr/local/rtl-sdr/build/src/rtl_sdr /usr/bin/  
COPY \--from=BUILD_ENV /usr/local/rtl-sdr/build/src/librtlsdr.so.0
/usr/local/lib/  
  
#ENTRYPOINT ["/usr/bin/rtl_sdr"]  

