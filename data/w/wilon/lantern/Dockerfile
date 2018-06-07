#nano Dockerfile  
#docker build -t lihaixin/lantern .  
#docker push lihaixin/lantern:3.0.7  
#docker run -itd --restart=always --name lantern2 -p 8080:8080 -p 3128:3128
ubuntu:16.04 /bin/bash  
#docker run -itd --restart=always --net=host --name lantern -p 8080:8080 -p
3128:3128 lihaixin/lantern  
#docker run -d --name lantern -P lihaixin/lantern  
#export http_proxy=http://your-ip-here3128  
#export https_proxy=http://your-ip-here:3128  
#curl -kvx localhost:3128 http://www.google.com/humans.txt  
  
FROM ubuntu:16.04  
MAINTAINER li haixin <lihaixin@15099.net>  
WORKDIR /root  
RUN apt-get update && \  
apt-get -y install wget libappindicator3-1 && \  
wget https://raw.githubusercontent.com/getlantern/lantern-
binaries/master/lantern-installer-64-bit.deb && \  
dpkg -i lantern-installer-64-bit.deb && \  
rm -rf lantern-installer-64-bit.deb && \  
apt-get -f install && \  
apt-get clean && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  
EXPOSE 3128/tcp 8080/tcp  
  
ENTRYPOINT ["/usr/bin/lantern", "--configdir=/root", "--headless=true", "--
proxyall=true", "--startup=false", "--clear-proxy-settings=false", "--
addr=0.0.0.0:3128", "--uiaddr=0.0.0.0:8080"]  
#/usr/bin/lantern --configdir=/root --headless=true --addr=0.0.0.0:3128
--uiaddr=0.0.0.0:8080 --proxyall=true --startup=false --clear-proxy-
settings=false  

