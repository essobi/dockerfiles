FROM ubuntu  
MAINTAINER "jinyu121" <jinyu121@126.com>  
  
# Basic environment setting  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN apt update && \  
apt install -y \  
curl \  
git \  
unzip \  
wget  
  
# Port for v2ray  
EXPOSE 10010  
# Port for ShadowSocks  
EXPOSE 10086  
# Copy configuration file  
COPY config.json /etc/v2ray/config.json  
COPY run.sh /etc/v2ray/run.sh  
  
# Have fun  
ENTRYPOINT ["/etc/v2ray/run.sh"]  

