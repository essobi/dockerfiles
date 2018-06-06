FROM diginc/pi-hole  
  
MAINTAINER Shaf Ali "github@shaf.net"  
ENV PATCHED="2018-04-10" \  
DNSF1="8.8.8.8" \  
DNSF2="8.8.4.4" \  
DNS1="127.0.0.1#5444" \  
DNS2="127.0.0.1#5445"  
RUN apt-get update && cd / && git clone https://github.com/shaf/utdns \  
&& cd /utdns && chmod +x configure \  
&& apt-get -y install g++ make && ./configure && make -j `nproc` \  
&& apt-get -y purge --auto-remove g++ make && apt-get clean \  
&& sed -i -e 's/^setup_dnsmasq ".*/setup_dnsmasq "127.0.0.1#5444"
"127.0.0.1#5445"/' /start.sh  
  
ADD dns1 /etc/services.d/dns1  
ADD dns2 /etc/services.d/dns2  

