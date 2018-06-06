FROM ubuntu:latest  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
  
#install build utils  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential git
autoconf automake libtool pkg-config wget  
  
#install build deps  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libpcre3-dev libyaml-dev
libjansson-dev libpcap0.8-dev libpcap-dev libmagic-dev libz-dev  
  
WORKDIR /usr/src  
RUN git clone https://github.com/inliniac/suricata.git  
  
WORKDIR /usr/src/suricata  
RUN git checkout suricata-3.1.1  
RUN git clone https://github.com/OISF/libhtp.git libhtp  
  
WORKDIR /usr/src/suricata/libhtp  
RUN git checkout 0.5.21  
RUN ./autogen.sh  
  
WORKDIR /usr/src/suricata  
ADD reference.patch .  
RUN patch -p1 < reference.patch  
RUN ./autogen.sh  
RUN ./configure && make && make install && make install-full && make clean  
RUN ldconfig  
  
WORKDIR /pcap  
ENTRYPOINT ["/usr/local/bin/suricata"]  
  
# clean up  
RUN rm -rf /var/cache/apk/*  

