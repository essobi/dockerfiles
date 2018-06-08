FROM ubuntu:latest  
MAINTAINER = Aman Mangal <amanmangal@gatech.edu>  
  
# install depedencies from standard repos  
RUN apt-get update && apt-get install -y wget iptables g++ build-essential
flex bison libpcap-dev libpcre3-dev libdumbnet-dev zlib1g-dev
libluajit-5.1-dev pkg-config autoconf libtool git-core libnetfilter-queue-dev
libnetfilter-queue1 libnfnetlink-dev libnfnetlink0  
  
# install custom dependencies  
RUN wget https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz && tar xf
daq-2.0.6.tar.gz && cd daq-2.0.6 && ./configure && make && make install &&
ldconfig  
  
# install snort  
RUN git clone https://github.com/snortadmin/snort3.git && cd snort3 && git
checkout 3e1b6a92aa855bfcc442148ab7f2f0ff72ef3d3a && autoreconf -isvf &&
./configure && make -j 8 && make install  
  
# copy run script  
COPY run_snort.sh /  
RUN chmod +x /run_snort.sh  
  
# command to run snort  
CMD ["/bin/sh", "/run_snort.sh"]  
  
# data  
VOLUME /log  
  
# clean up  
RUN rm -r daq-2.0.6.tar.gz daq-2.0.6/ snort3/  

