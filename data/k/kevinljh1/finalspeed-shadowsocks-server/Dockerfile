# This dockerfile uses the ubuntu image  
# VERSION 1 - EDITION 1  
# Author: Yourtion, Yale Huang  
# Command format: Instruction [arguments / command] ..  
# Base image to use, this must be set as the first line  
FROM ubuntu  
  
MAINTAINER Yale Huang <calvino.huang@gmail.com>  
  
# Commands to update the image  
RUN apt-get -y update && apt-get -y upgrade  
  
#build-essential  
# Install shadowsocks-libev  
RUN apt-get install build-essential autoconf libtool libssl-dev git
openjdk-8-jre unzip \  
libpcap-dev wget supervisor -y  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git
/root/shadowsocks-libev  
RUN wget -O /root/finalspeed_server.zip
https://github.com/kevinljh11/finalspeed/raw/master/finalspeed_server10.zip  
RUN wget -O /root/ssr.zip
https://github.com/shadowsocksrr/shadowsocksr/archive/akkariiin/dev.zip  
RUN cd /root/shadowsocks-libev && git checkout v2.4.4 && ./configure && make  
RUN cd /root/shadowsocks-libev/src && install -c ss-server /usr/bin  
RUN apt-get purge git build-essential autoconf libtool libssl-dev -y && apt-
get autoremove -y && apt-get autoclean -y  
RUN mkdir -p /opt/finalspeed && cd /opt/finalspeed && unzip
/root/finalspeed_server.zip  
RUN mkdir -p /opt/ssr && cd /opt/ssr && unzip /root/ssr.zip  
RUN rm -rf /root/shadowsocks-libev  
COPY start_finalspeed /opt/finalspeed/start_finalspeed  
COPY supervisord.conf /etc/supervisord.conf  
COPY server_linux_amd64 /root/server_linux_amd64  
RUN chmod +x /root/server_linux_amd64  
#RUN unzip /root/ssr.zip  
ENV SS_PASSWORD ibm123456  
ENV SS_METHOD aes-256-cfb  
  
EXPOSE 150/udp 151/udp 8339/tcp  
  
#ENTRYPOINT /usr/bin/ss-server -s 0.0.0.0 -p 8338 -k ${SS_PASSWORD} -m
${SS_METHOD}  
CMD ["/usr/bin/supervisord"]  

