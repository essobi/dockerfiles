from node:8-stretch  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y curl vim wget git libsodium-dev libsodium18 less nano
libboost-system-dev  
RUN mkdir /root/znomp  
WORKDIR /root  
COPY ./znomp /root/znomp  
RUN \  
cd /root/znomp npm install && npm update &&\  
mkdir /root/znomp/logs && \  
touch /root/znomp/logs/pool.log  
ADD ./configure_pool.sh /root/  
RUN \  
chmod +x /root/configure_pool.sh &&\  
echo "#!/bin/bash\ncd /root/znomp && /root/configure_pool.sh && npm start |
tee --append /root/znomp/logs/pool.log && bash" > /root/entry.sh &&\  
chmod +x /root/entry.sh  
VOLUME ["/root/ssl/"]  
CMD ["/root/entry.sh"]  

