#  
# strcrzy/sensor:suricata  
#  
# a debian based docker image that includes:  
#  
# - suricata  
# - oinkmaster  
# designed for use with strcrzy/sink  
FROM debian:jessie  
MAINTAINER strcrzy, https://github.com/strcrzy  
  
RUN apt-get -qq update && apt-get -qq install libpcre3 libpcre3-dbg
libpcre3-dev\  
build-essential autoconf automake libtool libpcap-dev libnet1-dev pkg-config \  
libjansson-dev libyaml-0-2 libyaml-dev zlib1g zlib1g-dev libmagic-dev python \  
libcap-ng-dev libgeoip-dev  
  
WORKDIR /tmp  
  
# suricata  
ADD http://luajit.org/download/LuaJIT-2.0.3.tar.gz /tmp/  
RUN tar -zxvf LuaJIT-2.0.3.tar.gz && cd LuaJIT-2.0.3 && make install  
  
ADD http://www.openinfosecfoundation.org/download/suricata-2.0.3.tar.gz /tmp/  
RUN tar -zxvf suricata-2.0.3.tar.gz && cd suricata-2.0.3 && \  
./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var \  
\--enable-geoip --enable-luajit && make && make install && make install-full
&&\  
apt-get install -y oinkmaster  
ADD /etc/oinkmaster.conf /etc/  
ADD /etc/suricata/suricata.yaml /etc/suricata/  
ADD /bin/suricata_wrapper /usr/bin/  
  
RUN \  
chmod +x /usr/bin/suricata_wrapper && \  
ldconfig && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH /nsm/bro/bin:$PATH  
  
ENTRYPOINT ["/usr/bin/suricata_wrapper"]  
CMD ["-c", "/etc/suricata/suricata.yaml", "-i", "eth0"]  

