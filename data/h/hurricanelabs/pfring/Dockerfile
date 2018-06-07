FROM ubuntu:12.04  
RUN apt-get update  
RUN apt-get -y install libpcre3 libpcre3-dbg libpcre3-dev \  
build-essential autoconf automake libtool libnet1-dev \  
libyaml-0-2 libyaml-dev zlib1g zlib1g-dev libcap-ng-dev libcap-ng0 \  
make flex bison git wget libmagic-dev pkg-config libnuma-dev strace  
  
RUN cd /usr/local/src && git clone https://github.com/xtao/PF_RING.git  
  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/opt/pf_ring/lib  
  
# Build the userland library  
RUN cd /usr/local/src/PF_RING/userland/lib && \  
LIBS="-L/opt/pf_ring/lib -lrt -lnuma" ./configure --prefix=/opt/pf_ring && \  
make && \  
make install  
  
# Build libpcap  
RUN cd /usr/local/src/PF_RING/userland/libpcap-* && \  
LIBS="-L/opt/pf_ring/lib -lpfring -lpthread -lrt -lnuma" \  
./configure --prefix=/opt/pf_ring && \  
make && \  
make install  
  
# Build tcpdump against new libpcap  
RUN cd /usr/local/src/PF_RING/userland/tcpdump-* && \  
LIBS="-L/opt/pf_ring/lib -lrt -lnuma" ./configure --prefix=/opt/pf_ring && \  
make && \  
make install  
  
# Build example userland tools  
RUN cd /usr/local/src/PF_RING/userland/examples && \  
make  
RUN cd /usr/local/src/PF_RING/userland/examples_zc && \  
make  
  
# Copy the pf_ring kernel source header  
RUN cp /usr/local/src/PF_RING/kernel/linux/pf_ring.h
/usr/include/linux/pf_ring.h  
  
# Configure LD_LIBRARY_PATH  
RUN echo "/opt/pf_ring/lib" > /etc/ld.so.conf.d/pfring.conf  
RUN ldconfig  
  
# Add /opt/pf_ring to $PATH  
ENV PATH /opt/pf_ring/bin:/opt/pf_ring/sbin:$PATH  
  
ADD docker-entrypoint.sh /entrypoint.sh  
ADD zerocopy.sh /zerocopy.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/bin/bash"]  

