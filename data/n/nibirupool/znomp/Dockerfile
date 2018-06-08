from node:stretch  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y curl vim wget git libsodium-dev libsodium18 less  
WORKDIR /root  
RUN \  
git clone https://github.com/Punkoivan/z-nomp.git &&\  
cd z-nomp && npm update && npm install &&\  
mkdir /root/z-nomp/logs && \  
touch /root/z-nomp/logs/pool.log  
ADD ./configure_pool.sh /root/  
RUN \  
chmod +x /root/configure_pool.sh &&\  
echo "#!/bin/bash\ncd /root/z-nomp && /root/configure_pool.sh && npm start |
tee --append /root/z-nomp/logs/pool.log && bash" > /root/entry.sh &&\  
chmod +x /root/entry.sh  
ADD ./fullchain1.pem /root/fullchain.pem  
ADD ./privkey1.pem /root/privkey.pem  
CMD ["/root/entry.sh"]  

