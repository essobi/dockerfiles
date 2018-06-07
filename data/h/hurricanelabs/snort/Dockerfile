FROM hurricanelabs/pfring  
  
RUN apt-get update  
RUN apt-get install -y perl libio-socket-ssl-perl libcrypt-ssleay-perl ca-
certificates libwww-perl  
  
# Fetch source  
RUN cd /usr/local/src && \  
wget https://www.snort.org/downloads/snort/daq-2.0.2.tar.gz && \  
tar xzf daq-2.0.2.tar.gz  
RUN cd /usr/local/src && \  
wget https://www.snort.org/downloads/snort/snort-2.9.6.2.tar.gz && \  
tar xzf snort-2.9.6.2.tar.gz  
RUN cd /usr/local/src && \  
wget https://libdnet.googlecode.com/files/libdnet-1.12.tgz && \  
tar xzf libdnet-1.12.tgz  
RUN cd /usr/local/src && \  
wget https://pulledpork.googlecode.com/files/pulledpork-0.7.0.tar.gz && \  
tar xzf pulledpork-0.7.0.tar.gz  
  
# Build DAQ  
RUN cd /usr/local/src/daq-* && \  
ldconfig -v && \  
LIBS="-lrt -lnuma" ./configure \--prefix="/opt/daq" \  
\--disable-nfq-module \  
\--disable-ipq-module \  
\--with-libpcap-includes=/opt/pf_ring/include \  
\--with-libpcap-libraries=/opt/pf_ring/lib && \  
make && \  
make install  
RUN echo "/opt/daq/lib/daq" > /etc/ld.so.conf.d/daq.conf  
RUN ldconfig  
ENV PATH /opt/daq/bin:$PATH  
  
# Build pfring-daq-module  
RUN cd /usr/local/src/PF_RING/userland/snort/pfring-daq-module && \  
autoreconf -ivf  
RUN cd /usr/local/src/PF_RING/userland/snort/pfring-daq-module && \  
LIBS="-lrt -lnuma" ./configure --prefix="/opt/daq" \  
\--with-libdaq-includes=/opt/daq/include \  
\--with-libsfbpf-includes=/opt/daq/include \  
\--with-libsfbpf-libraries=/opt/daq/lib \  
\--with-libpfring-includes=/opt/pf_ring/include \  
\--with-libpfring-libraries=/opt/pf_ring/lib && \  
make && \  
make install  
  
# Build libdnet  
RUN cd /usr/local/src/libdnet-* && \  
./configure --prefix=/opt/snort "CFLAGS=-fPIC" && \  
make && \  
make install  
RUN echo "/opt/snort/lib" > /etc/ld.so.conf.d/snort.conf  
RUN cp /opt/snort/lib/libdnet.1.0.1 /opt/snort/lib/libdnet.so.1.0.1  
RUN ldconfig -v  
  
# Build snort  
RUN cd /usr/local/src/snort-* && \  
./configure --prefix=/opt/snort \  
\--enable-ipv6 \  
\--enable-zlib \  
\--enable-gre \  
\--enable-mpls \  
\--enable-targetbased \  
\--enable-decoder-preprocessor-rules \  
\--enable-pthread \  
\--enable-dynamicplugin \  
\--enable-normalizer \  
\--disable-static-daq \  
\--with-daq-includes=/opt/daq/include \  
\--with-daq-libraries=/opt/daq/lib \  
\--with-dnet-includes=/opt/snort/include \  
\--with-dnet-libraries=/opt/snort/lib \  
\--with-libpcap-includes=/opt/pf_ring/include \  
\--with-libpcap-libraries=/opt/pf_ring/lib \  
\--with-libpfring-includes=/opt/pf_ring/include \  
\--with-libpfring-libraries=/opt/pf_ring/lib && \  
make && \  
make install  
ENV PATH /opt/snort/bin:$PATH  
  
# Install pulledpork  
RUN cp /usr/local/src/pulledpork-*/pulledpork.pl /opt/snort/bin && \  
chmod 0755 /opt/snort/bin/pulledpork.pl  
  
ADD compile_pfring_dna_daq.sh /compile_pfring_dna_daq.sh  
ADD docker-entrypoint.sh /entrypoint.sh  
ADD pulledpork.sh /pulledpork.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["snort"]  

