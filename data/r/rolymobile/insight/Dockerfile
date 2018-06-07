FROM ubuntu:14.04  
  
WORKDIR /root  
  
RUN \  
apt-get update -y && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y python-software-properties && \  
apt-get install -y git vim wget curl net-tools supervisor  
  
RUN \  
apt-add-repository -y ppa:bitcoin/bitcoin && \  
add-apt-repository -y ppa:chris-lea/node.js && \  
apt-get update -y && \  
apt-get install -y bitcoind && \  
apt-get install -y nodejs && \  
mkdir /root/.bitcoin && \  
mkdir /root/.insight && \  
npm install -g npm && \  
git clone https://github.com/bitpay/insight.git && \  
cd insight && \  
npm install  
  
COPY bitcoin.conf /root/.bitcoin/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY run-insight.sh /root/insight/run-insight.sh  
  
CMD ["/usr/bin/supervisord"]  
EXPOSE 3000  
EXPOSE 8332  
EXPOSE 8333  

