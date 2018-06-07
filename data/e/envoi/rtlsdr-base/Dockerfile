# derive from debian wheezy image  
FROM debian:wheezy  
  
MAINTAINER Anton S.  
  
RUN apt-get update  
RUN apt-get install -y libusb-1.0-0-dev pkg-config ca-certificates git-core
cmake build-essential --no-install-recommends  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
RUN mkdir -p /etc/modprobe.d  
RUN echo 'blacklist dvb_usb_rtl28xxu' > /etc/modprobe.d/dvb-blacklist.conf  
RUN git clone git://git.osmocom.org/rtl-sdr.git  
RUN mkdir /tmp/rtl-sdr/build  
  
WORKDIR /tmp/rtl-sdr/build  
RUN cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON  
RUN make  
RUN make install  
RUN ldconfig -v  
  
WORKDIR /tmp  
RUN rm -rf /tmp/rtl-sdr  
  
WORKDIR /  

