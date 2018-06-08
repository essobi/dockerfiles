############################################################  
# Dockerfile to build shadowsocks client image  
# Based on aliyun-ubuntu:14.04 trusty  
############################################################  
  
FROM nunchuk/aliyun-ubuntu:14.04  
MAINTAINER XinYe <nunchuk@live.com>  
  
ENV SS_VERSION=2.8.2  
  
# install shadowsocks-python  
RUN apt-get update && \  
apt-get install -y python-pip && \  
pip install shadowsocks==$SS_VERSION && \  
rm -rf /var/lib/apt/lists/*  
  
# configure environments  
ENV SERVER_ADDR= \  
SERVER_PORT=8388 \  
PASSWORD=youpassword \  
METHOD=aes-256-cfb \  
LOCAL_ADDR=0.0.0.0 \  
LOCAL_PORT=1080 \  
TIMEOUT=300  
  
EXPOSE $LOCAL_PORT/tcp  
  
# CMD shell way to run container  
CMD sslocal -s "$SERVER_ADDR" \  
-p "$SERVER_PORT" \  
-k "$PASSWORD" \  
-m "$METHOD" \  
-b "$LOCAL_ADDR" \  
-l "$LOCAL_PORT" \  
-t "$TIMEOUT" \  
\--fast-open  

