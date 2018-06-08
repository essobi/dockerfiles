FROM ubuntu:16.04  
ENV HOME /root  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y wget git nodejs npm && \  
npm install -g n && \  
n stable && \  
npm install -g web3 && \  
wget http://d1h4xl4cr1h0mo.cloudfront.net/v1.9.4/x86_64-unknown-linux-
gnu/parity_1.9.4_ubuntu_amd64.deb && \  
apt install /parity_1.9.4_ubuntu_amd64.deb && \  
rm -rf /parity_1.9.4_ubuntu_amd64.deb && \  
git clone https://github.com/cubedro/eth-net-intelligence-api && \  
cd eth-net-intelligence-api && \  
npm install && \  
npm install -g pm2 && \  
npm cache clean --force && \  
apt-get clean && \  
apt-get remove -y wget git && \  
apt-get autoremove -y  
  
ADD files/app.json /eth-net-intelligence-api/app.json  
ADD files/startscript.sh /startscript.sh  
  
RUN chmod +x /startscript.sh  
  
EXPOSE 8545  
EXPOSE 8180  
EXPOSE 30303  
EXPOSE 30303/udp  
  
ENTRYPOINT ["/startscript.sh"]  

