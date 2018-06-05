FROM node:4.2.1  
MAINTAINER Brandon Papworth <brandon@papworth.me>  
  
RUN echo "deb http://httpredir.debian.org/debian/ experimental main contrib
non-free" \  
>> /etc/apt/sources.list; \  
echo "deb-src http://httpredir.debian.org/debian/ experimental main contrib
non-free" \  
>> /etc/apt/sources.list; \  
apt-get update; \  
apt-get install -y libzmq5-dev; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*; \  
rm -rf /tmp/*; \  
rm -rf /var/tmp/*;  

