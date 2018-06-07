FROM ubuntu:15.04  
  
# Prepare to install all the stuff  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# install ruby from source  
RUN \  
wget https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.3.tar.gz -O
ruby-2.2.3.tar.gz && \  
tar -xzf ruby-2.2.3.tar.gz && \  
cd ruby-2.2.3 && \  
./configure && \  
make && \  
make install && \  
cd ../ && rm -rf ruby-2.2.3  

