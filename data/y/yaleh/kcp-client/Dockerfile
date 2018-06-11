# This dockerfile uses the ubuntu image  
# Author: Yale Huang  
# Command format: Instruction [arguments / command] ..  
  
# Base image to use, this must be set as the first line  
FROM alpine  
  
MAINTAINER Yale Huang <calvino.huang@gmail.com>  
  
# Commands to update the image  
RUN apk add \--update wget make gcc g++ supervisor && rm -rf /var/cache/apk/*
&& \  
wget http://siag.nu/pub/pen/pen-0.33.1.tar.gz && \  
tar xvfz pen-0.33.1.tar.gz && \  
cd pen-0.33.1/ && \  
./configure && make && make install && \  
rm -rf /pen-0.33.1.tar.gz /pen-0.33.1 && \  
mkdir -p /opt/kcptun && \  
wget -O /root/kcptun-linux-amd64.tar.gz --no-check-certificate
https://github.com/xtaci/kcptun/releases/download/v20171021/kcptun-linux-
amd64-20171021.tar.gz && \  
cd /opt/kcptun && \  
tar xvfz /root/kcptun-linux-amd64.tar.gz client_linux_amd64 && \  
rm /root/kcptun-linux-amd64.tar.gz && \  
apk del wget make gcc g++  
  
COPY balanced_kcp_client /balanced_kcp_client  
COPY generate_supervisord_conf /generate_supervisord_conf  
  
ENV SERVER=127.0.0.1 SERVER_PORT=4000 KCP_PASSWORD=password MTU=1350
SNDWND=128 RCVWND=1024 \  
MODE=fast SERVER_COUNT=1  
EXPOSE 1083/tcp  
  
#CMD /opt/kcptun/client_linux_amd64 -r $SERVER:$SERVER_PORT -l ":1083" \--key
"${KCP_PASSWORD}" \--mtu $MTU \  
# --sndwnd $SNDWND --rcvwnd $RCVWND --mode $MODE  
  
CMD /balanced_kcp_client  
  
  

