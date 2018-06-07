FROM hurricanelabs/pfring  
  
RUN apt-get update  
  
RUN apt-get install -y python2.7  
  
RUN cd /usr/local/src && git clone
git://phalanx.openinfosecfoundation.org/oisf.git  
RUN cd /usr/local/src/oisf && git clone https://github.com/ironbee/libhtp.git
-b 0.5.x  
  
# Compile suricata  
RUN cd /usr/local/src/oisf && ./autogen.sh  
RUN cd /usr/local/src/oisf && \  
LIBS="-lrt -lnuma" ./configure --enable-pfring --prefix=/opt/suricata \  
\--with-libpfring-includes=/opt/pf_ring/include \  
\--with-libpfring-libraries=/opt/pf_ring/lib --with-libpcap-
includes=/opt/pf_ring/include \  
\--with-libpcap-libraries=/opt/pf_ring/lib && \  
make && \  
make install && \  
ldconfig  
  
# Create /data  
RUN mkdir /data  
  
# Install sample configs  
RUN cd /usr/local/src/oisf && \  
make install-conf  
  
# Move etc and var to /data  
RUN mv /opt/suricata/etc /data  
RUN mv /opt/suricata/var /data  
RUN sed -i 's|/opt/suricata|/data|g' /data/etc/suricata/suricata.yaml  
  
# Add /opt/suricata/bin to PATH  
ENV PATH /opt/suricata/bin:$PATH  

