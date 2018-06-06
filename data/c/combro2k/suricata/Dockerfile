FROM hurricanelabs/pfring  
  
RUN apt-get update  
  
RUN apt-get install -y python2.7 libnetfilter-queue1 libnetfilter-queue-dev
curl cron  
  
RUN cd /usr/local/src && git clone
git://phalanx.openinfosecfoundation.org/oisf.git  
RUN cd /usr/local/src/oisf && git clone https://github.com/ironbee/libhtp.git
-b 0.5.x  
RUN cd /usr/local/src && curl -L
"http://downloads.sourceforge.net/project/oinkmaster/oinkmaster/2.0/oinkmaster-2.0.tar.gz"
| tar zxv  
RUN cd /usr/local/src/oinkmaster-2.0 && cp oinkmaster.pl /usr/sbin/oinkmaster  
  
# Create /data  
RUN mkdir /data  
  
ADD oinkmaster.conf /data/oinkmaster.conf  
ADD update-rules /data/update-rules  
  
RUN chmod u+x /data/update-rules  
  
# Compile suricata  
RUN cd /usr/local/src/oisf && ./autogen.sh  
RUN cd /usr/local/src/oisf && \  
LIBS="-lrt -lnuma" ./configure --enable-pfring --prefix=/opt/suricata \  
\--with-libpfring-includes=/opt/pf_ring/include \  
\--with-libpfring-libraries=/opt/pf_ring/lib --with-libpcap-
includes=/opt/pf_ring/include \  
\--with-libpcap-libraries=/opt/pf_ring/lib \  
\--disable-gccmarch-native \  
\--enable-nfqueue && \  
make && \  
make install && \  
ldconfig  
  
# Install sample configs  
RUN cd /usr/local/src/oisf && \  
make install-conf  
  
# Move etc and var to /data  
RUN mv /opt/suricata/etc /data  
RUN mv /opt/suricata/var /data  
RUN sed -i 's|/opt/suricata|/data|g' /data/etc/suricata/suricata.yaml  
  
# Add /opt/suricata/bin to PATH  
ENV PATH /opt/suricata/bin:$PATH  
  
VOLUME /data  

