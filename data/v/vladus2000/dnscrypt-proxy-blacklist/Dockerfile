FROM vladus2000/ubuntu-base  
MAINTAINER vladus2000 <docker@matt.land>  
  
COPY shiz/ /  
  
RUN \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install wget unzip python && \  
wget https://github.com/jedisct1/dnscrypt-proxy/archive/master.zip && \  
unzip master.zip && \  
mv dnscrypt-proxy-master/utils/generate-domains-blacklists . && \  
rm -rf dnscrypt-proxy-master master.zip && \  
apt-get -y purge wget unzip && \  
apt-get -y autoremove && \  
apt-get clean && \  
chmod +x /startup.sh  
  
CMD /bin/bash -c /startup.sh  

