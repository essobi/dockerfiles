FROM ubuntu:latest  
MAINTAINER sthysel <sthysel@gmail.com>  
ENV REFRESHED_AT 2015-03-06  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
build-essential \  
cmake \  
libusb-1.0-0-dev \  
git \  
pkg-config  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN addgroup --gid 1000 radioman  
RUN adduser --disabled-password --home /data --no-create-home --system -q
--uid 1000 --ingroup radioman radioman  
  
RUN mkdir /data && mkdir /build/  
  
RUN chown radioman:radioman /data  
  
# sdr  
WORKDIR /build/  
RUN git clone git://git.osmocom.org/rtl-sdr.git \  
&& cd ./rtl-sdr \  
&& mkdir build \  
&& cd build \  
&& cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON \  
&& make \  
&& make install \  
&& ldconfig  
  
# dump 1090  
WORKDIR /build/  
RUN git clone git://github.com/MalcolmRobb/dump1090.git \  
&& cd dump1090 \  
&& make  
  
# RUN echo "dvb_usb_rtl28xxu" >> /etc/modprobe.d/blacklist  
# entrypoint config  
COPY sdr.sh /sdr.sh  
RUN chmod +x /sdr.sh  
  
# rtl_tcp port  
EXPOSE 1234  
# dump 1090 ports  
EXPOSE 8080  
EXPOSE 30001  
EXPOSE 30002  
ENTRYPOINT ["/sdr.sh"]  
CMD ["test"]  

